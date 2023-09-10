---
draft: false
date: 2022-08-16
categories:
  - Data Science
authors:
  - ingo
tags:
  - Data Science
  - git
  - Versioning
  - DVC
  - Version Control
---

<!--
Title: Version control for data science projects
Date: 2022-08-16 11:00
Category: Data Science
Tags: Data Science, Git, Version Control, DVC, Versioning
Slug: version-control-for-data-science
Authors: Ingo Fruend
Summary: Data science projects consist of code, data and algorithmic ideas. If these three factors play together there is a tendency that your projects ends up being a total mess.
status: published
-->

Data sciens projects have a lot of moving parts&mdash;code, data, configuration, hypotheses, modeling assumptions, ... All of these change at different time scales and with different impact on what and how much needs to be stored. As a result, data science projects often diverge into some sort of chaos. This doesn't have to be the case!

<!-- more -->


For the purpose of this poist, we will group the changes that happen in data science projects roughly into three categories

1. The *data* itself. A typical data science project searches for an algorithm that can model or predict certain aspects of the data. However, in many cases the data itself changes to some extent. With new and different data, different algorithms may result in good predictions.
2. The *choice of algorithm*. There is [no generally "best" algorithm for everything](https://en.wikipedia.org/wiki/No_free_lunch_theorem). Usually, it isn't even possible to decide in advance which algorithm might be best or even just really good. In addition, there may be additional considerations beyond prediction accuracy, such as run time, memory demands, etc. This means that a typical data science project will change the entire algorithm being implemented a few times in its course.
3. Finally, there is *code* that implements the data cleaning and the chosen algorithm(s). As we work on a project, the code changes, we may add new functionality, logging, fix bugs, maybe even add an entirely new algorithm.

This differs from classical software projects where a good algorithm can usually be chosen in advance and where we mostly care about the flow of data rather than the actual content of the data (Skiena, 2017). Together, this makes data science projects much more prone to drift off into a chaotic mess: There is some (almost) abandoned code to read data from an old format that we might want to revisit again, there are a few hundred lines implementing an algorithm that turned out to be useless, but we want to keep it for reference. There might be an algorithm that works fairly well, but somewhere half way, we want to write out an intermediate result and add a little additional transformation of an auxiliary variable.

In classical software projects, there is a tendency to run into a mess as well and the solution is (i) discipline and (ii) a version control system such as [git](https://git-scm.com). For data science projects, discipline plays an important role as well. But while git is great for managing versions of code or small text and configuration files, git is pretty bad at tracking really big data files or changes in algorithmic choices. This is where a tool like data version control (short [DVC](http://dvc.org)) comes into play.

In this blog post, I will sketch out a basic set up for data science projects using DVC and I will explain how to get started.

# What does DVC do that git does not?

DVC builds on top of git to provide version control for data science projects. It does so in mainly four ways:

1. A separate storage option for large files such as datasets or models.
2. A notion of a lightweight pipeline that versions the correct sequence in which your scripts run.
3. Support for running and tracking experiments.
4. Versions (and diffs) for model metrics and plots.

Point 1 is probably the main selling point here. If you ever had to work with a git repository that also included a few gigabytes of binaries, you will know what I mean: It takes ages to complete any interaction with the remote repository. The solution here isn't really new: Define a separate (potentially very big, like an s3 bucket) storage area for large files and have git track just metadata (e.g. where is the file, under what name should it appear in the local file system, ...).

Point 2 is a bit similar to [make](https://www.gnu.org/software/make/) and there are many [other tools](https://pydoit.org) that address this problem or similar ones. What makes DVC stand out here, is that DVC pipelines clearly separate between data (i.e. big files) and code dependencies on one side and outputs such as plots and metrics on the other side. In addition, they are designed to be easily stored and versioned in git. However, that's really it. Having pipelines bundled with the rest of DVC lets you also version the flow of data through your scripts, but you would probably use other tools like [airflow](https://airflow.apache.org) or [prefect](https://www.prefect.io) in a production setting.

Point 3 is actually quite an interesting point. There are many tools that offer experiment tracking. However, most of them will store every run into a database, which is probably not really what you want. Firstly, you may have failed runs that you (in hindsight) didn't want in the database, and you may have runs that just confirmed that your code doesn't crash (again nothing you want to keep). Secondly, you may not want to store this information in a separate database and rather track it in git. DVC stores experiments that you run in a temporary storage area (similar to `git stash`) and there is separate step on which experiments you want to persistently store in git and which ones you don't. In addition, the experiments are stored in git so that you don't need to switch tools for viewing "code history" and "run history" (the two are closely interlinked in data science projects anyway).

Point 4 takes the point serious that, in data science projects, the main difference between two different versions isn't necessarily the code itself, but the outputs that it created. And those outputs are learning curves, plots, accuracies, ...

# Setting up a minimal DVC project

First, you need to install DVC from pip.
One of the key features of DVC is that it manages a separate storage area for you.
That storage area could be on your local hard drive (useful for testing), but in most realistic scenarios it will be remote storage on a different machine or in the cloud. Given that some of these remote storage options have a potential to come with lots of dependencies, you need to tell pip to install the dependencies for a given remote storage along with DVC. For example, to support google cloud storage, you would install DVC like this:
```
pip install dvc[gs]
```
Of course if you just want to play around with DVC on your local machine, and you don't need any cloud support, then you can omit the additional dependencies altogether and just run `pip install dvc`.

To set up DVC for your git repository, simply run
```
dvc init
```
This will generate a couple of files (and tell you which ones it created). You can safely add those files to git.

If you want to store your large files, like data, models, ... in remote storage, you would next have to setup that remote storage. Do you need remote storage? If you are using DVC for academic projects or if you are only playing around with DVC on your local computer, the answer is likely "no". In almost all other settings, the answer is "yes". In particular, you need remote storage if you need to share your progress with others (e.g. co-workers, production systems, ...). Similar to git, you can of course also have multiple DVC remotes. To set up a remote, you run
```
dvc remote add <NAME> <URI>
```
where you replace `<NAME>` by the name you want to use to refer to the remote and `<URI>` by the URI of the storage bucket. For example to add the gcloud storage bucket at a URI `gs://ml-projects/dvcremote` under the name "gcloud", you would run
```
dvc remote add gcloud gs://ml-projects/dvcremote
```
Do not attempt to edit this bucket by hand (or delete it). This bucket is equally important for the integrity of your version history as (for example) the content of your `.git/objects/` folder&mdash;and I don't think you edit that by hand either.

# Working with DVC and good strategies for structuring your code

Other tools that provide tracking of data science projects make much stronger assumptions about how you structure your code. When working with DVC, you can basically do whatever you want. That means you don't really need to change much about your workflow. However, there are a few things that I personally find useful.

## Tracking large files in DVC

The first thing is that having DVC installed, you probably want to make use of the large file tracking and remote storage functionality.
To add a large file `data/db-dump.json` to DVC, you run
```
dvc add data/db-dump.json
```
This will analyze the file and create an additional file `data/db-dump.json.dvc`. Afterwards, you can add `data/db-dump.json.dvc` to git. Under the hood, DVC has copied `data/db-dump.json` to a location inside the `.dvc/` folder that it created when you ran `dvc init`. The file that you see as `data/db-dump.json` is just a link to the real file. As a consequence, DVC can quickly switch between different versions of your db dump. If you are using remote storage, then you also need to run `dvc push` to copy the local file(s) to remote storage.

To go back to an old version, you first check out the respective git-commit with `git checkout`, and then you run `dvc checkout` to bring all the files up to date that are tracked by DVC. If you are working with remote storage, and you use `git pull`, then you should probably use `dvc pull` right after too.

## Project structure

I find it useful to use a different structure for DVC projects than I would use for (e.g.) a python package. This is a fairly subjective choice and something else might work well for you. Just keep in mind: It helps to have the same structure for all your projects or all of your team's projects.

My DVC projects usually have the following folder structure:
```
data/
    raw/
    processed/
    final/
src/
    scripts/
    visualizations/
params.yaml
dvc.yaml
```
(I'm omitting operational folders like `.git/` or `.dvc/` here).
I have separate subfolders inside the `data/` folder. Data science pipelines typically transform one dataset to another to yet another. The `data/` folder partly reflects this by having separate subfolders for different stages. Usually, the raw folder doesn't change much (unless I want to re-train on an entirely new dataset) but the other folders may change over time. The `data/final/` subfolder contains datasets that are "ready to be consumed"; in some cases, that may mean that they've had enough preprocessing to be visualized or that they are ready for training a model (although notably many modern approaches like neural networks would train on raw or almost raw data).

The `src/` folder contains the actual analysis code. I have two subfolders `scripts/` and `visualizations/` here. Let's start with the first. Here, I have scripts that do separate steps of analysis. I try to keep these scripts as self-contained as possible (that way I don't need to re-run everything just because I wanted to change a small thing in the last step of a pipeline). Furthermore, I design these scripts as data transformations: Their input is a dataset (or csv file or ...) and their output is another dataset (or csv file or ...). For example, a training/validation/test split would take a dataset as input and write three separate index files into that dataset. This strategy makes intermediate steps become persistent on my hard disk (or for larger files in some remote storage), which in turn means that their versions can be tracked by DVC.

DVC has great support for [vega-lite](https://vega.github.io/vega-lite/). For a couple of standard scenarios (learning rate, confusion matrix, ...) there are already templates that come with DVC. If you only use those, you will be fine without the `visualizations/` folder. However, I find that most of these pre-packaged visualizations are build with a very specific usecase in mind (neural network training), but they don't really go very deep, and they often don't support more complex or high dimensional data exploration scenarios. DVC allows you to add [your own vega-lite templates](https://dvc.org/doc/command-reference/plots) and I often find that useful. These custom templates are supposed to be stored in `.dvc/plots/`, but I keep forgetting how that folder is supposed to be called, and I find that my plot templates change in similar ways as other code, so it makes more sense to me to have them in a location that clearly says "this is code".

I reserve the `out/` folder for the outputs of my scripts. These would normally be something like metrics or checkpoints as a lot of output also goes to the `data/` folder. Keep in mind any file can be tracked by DVC or git. So the decision what you want to use to track a file should not determine where you save it.

There are also two files, `params.yaml` and `dvc.yaml` that I will talk about in the next section.

## Reproducible runs

Many data science projects consist of multiple scripts that need to be run in a particular order. For example, data cleaning should usually run before model training. Keeping these steps separate makes sense, because each of these steps may take a long time and it is usually a good thing to stop at an intermediate result and store everything to disk. However, this can also be a source of errors: If you changed something in the data cleaning script but forget to re-run it, you may end up with very confusing errors&mdash;or end up with incorrect results. Furthermore, this makes things complicated for somebody else entering your project: They may not even know the correct order to reproduce your scripts. Putting the order into a README file addresses the second point, but not the first. Furthermore, the README might get out of sync with the actual order of running scripts.

DVC provides a better way of specifying the order in which different scripts should run. You simply specify which script depends on what, and then you call all your scripts with
```
dvc repro
```
The nice thing about this is, that DVC figures out, which parts of your data pipeline you still need to run and skips the others. So developing a habit of running `dvc repro` (or `dvc exp`, see below) usually helps you keep everything up to date and reproducible.

But how would you set up things so that `dvc repro` works? How do you specify which script depends on what? The solution is that you define it in a file called `dvc.yaml`. DVC can edit that file automatically, but you can also do so by hand. One of the key commands to put a script into `dvc.yaml` is the command
```
dvc run [options] python src/scripts/myscript.py
```
Instead of `[options]` you would enter a number of options are you just leave this part blank and fill it later by hand. The `dvc run` command can take options to specify dependencies on other files (`-d`) or specify output files (`-o`) or other things. If you type `dvc run --help` you will see a full list of all the options. I usually just specify a few on the first run and then edit the `dvc.yaml` file by hand to add the dependencies and outputs. Importantly, `dvc run` does nothing else than editing the `dvc.yaml` file. So you really do the exact same thing if you edit the file by hand.


## Experiments

When we build models or play with different ways to build features from our raw data, we usually try out a lot of different things. It's easy to lose track of what we tried and what the result of each attempt was. DVC can track these experiments for you; you mostly need to replace `dvc repro` with `dvc exp run` (after [a little bit of setup](https://dvc.org/doc/user-guide/experiment-management)). One advantage of DVC over similar tools is that you can first run your experiments and then pick the ones that you want to commit, much like you can select changes that go into a git commit.

One common form experimentation is playing with multiple parameters. DVC supports a central parameter file (or multiple ones). The default parameter file is called `params.yaml` and pipeline steps can depend on individual parameters in this file rather than the whole file. As a consequence, you don't need to re-run the whole pipeline just because one parameter in `params.yaml` changed.

Using a yaml configuration makes it easy to read parameters in your script. For example, you could read them with [PyYaml](https://pyyaml.org/wiki/PyYAMLDocumentation). A common tool for reading parameter files from python code is [hydra](https://hydra.cc). However, I don't quite like hydra, because it is fairly implicit about the parameters that a script depends on&mdash;with hydra any script could technically access all parameters. A more explicit way of dealing with parameter files is to use [pydantic](https://pydantic-docs.helpmanual.io) like this:
```python
from pydantic import BaseModel
from yaml import safe_load


class Config(BaseModel):
    modeltype: str
    learning_rate: float
    number_of_epochs: int


def read_config(filename: str) -> Config:
    with open(filename) as f:
        return Config(**safe_load(f))

config = read_config('params.yaml')
```
With this, you can access all the contents of your config file as `config.modeltype` or `config.learning_rate`. This is quite similar to the way you would access parameters with hydra, but it differs in two ways:

1. Only the parameters specified in the `Config`-class are actually available inside your code. So parameter dependencies are made explicit through the declarations in the `Config`-class. This makes it quite easy to keep the dependencies in the `dvc.yaml` file up to date.
2. The resulting parameters are guaranteed to have the exact types that you expect. So there is no risk that somebody puts for example `learning_rate: auto` into their config file if your code doesn't explicitly declare that it can handle this setting. This way, your code will fail very fast if something unexpected is coming from your config file.

# Conclusion

In this article, I argued that data science projects differ from classical software projects, because there are more factors that can make them change. Specifically, these factors are code structure, algorithmic logic, and data. I sketched a useful structure for data science projects and illustrated how to use DVC to track different versions of such a project.

I provide a cookiecutter template for a data science project at [igordertigor/templates](https://github.com/igordertigor/templates) on github.


# References
- Skiena, S (2017). *The Data Science Design Manual*. Springer. I'm mostly referring the first chapter here.
