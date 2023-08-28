Title: Building a model registry in GitHub
Date: 2022-08-26 12:00
Category: Data Science
Tags: Machine Learning, Data Science, MLOps
Slug: github-model-registry
Authors: Ingo Fruend
Summary: Data science projects can be messy, however we don't want to carry that mess over to our production environments.
status: published

> Note: This post refers to an outdated version of mlem which is not compatible with the current mlem version. Hence, most code examples won't work.

Data science projects can be [messy]({filename}/content/2022-08-07-version-control-for-data-science.md).
We try out something here, just to find out that it didn't really help.
Then we try out another thing, and maybe it does improve performance a little bit.
Most of the code that we write in these projects needs to run once and can be forgotten afterwards.
As long as we know what the general outcome (e.g. a trained model) of this approach was, we don't need to actually maintain it.
The only exception is that we occasionally need to re-train a model as new data has been collected.

Production software systems are quite different from this.
New requirements usually mean that we need to be able to change the code in one place without affecting other parts of the system.
Running machine learning models in production therefore requires a fairly clear separation between the data science world of experimentation and the rigid world of maintainable production code.
This separation can be achieved by treating machine learning models as&mdash;more or less&mdash;abstract, exchangeable artifacts, while the backend, on which these models run, only operates on these abstractions.

A model registry can work as the connection between these two worlds: Here we have a single point where other software components can retrieve machine learning models from and where we can manage which models run in which system.
For a model registry, we expect that the following should be fairly straight forward:

- get an overview of all models that are currently available
- change which models are currently active in which environment
- retrieve (and load) the currently active model for an environment
- find out which version of a model was running in which environment at a given time.

This article describes how to use [mlem](https://mlem.ai) and [gto](https://github.com/iterative/gto) as a model registry on top of a regular GitHub repository.
You can install both tools into your python environment with `pip install mlem gto`.

# A minimal setup

Create a new repository on GitHub and set up a local clone of it.
Inside that repository, run
```
  $ mlem init
```
this command will create a file `.mlem.yaml`, which contains configuration for mlem.
Commit that file to the git repository and push to GitHub, and you're done.
Your model registry is now ready to use.

# Using the registry

We will now cover a few use cases for the model registry. This will to some extent cover the lifecycle of a model from research to development to production.

## Registering a model

It is a good practice to develop individual machine learning models in separate repositories. It is also useful to have the artifacts created from each of these repositories to be linked to the repository. This keeps the stored model close to the logic and the data that went into it.

In order to avoid copying models to the model registry (and thus storing them twice), we can just link them. For example, we could make the model "linear_regression" from the commit tagged as "v1" in the GitHub repository "mycompany/cost-prediction" available in our model registry under the name "cost_predictor" with the following command:
```
  $ mlem link --source-project https://github.com/mycompany/cost-prediction \\
        --rev v1 \\
        linear_regression cost_predictor
```
The result of this is a new file `cost_predictor.mlem` inside the model registry. We could now make a pull request to request merging this link to the master branch.

There are a few things to notice here

- The new link file is pretty small and can easily be tracked with git.
- We model is available under different names in the research/development repository and in the model registry. Of course, we could have chosen different names, but given that these are in different contexts, it is likely that they would go by different names in the different contexts.
- We can specify a specific version of the model by using a git tag. Although you don't have to do this, it is a good idea to do so. Without the tag, the link will always be to the most recent version on the master branch, which may have changed considerably in the meantime. Unfortunately, this doesn't work by just specifying a commit's sha1, and it also only seems to work for GitHub repositories. In a research repository, different model versions might also go by different names so that they can be compared side by side. However, any version that goes to a central model registry should still be tagged.

Ideally, every new version of a model should go through a separate pull request in the model registry, and it should correspond to an explicit tag in the source repository. This way your model specifications are unambiguous. You could enforce this by [protecting your main/master branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches) and having a GitHub action that runs on every pull request which runs the following validation script:
```python
import sys
from itertools import chain
import mlem.api

ok = True
for m in chain(*mlem.api.ls().values()):
    if m.rev is None:
        sys.stderr(f'Model at {m.location.path} has no --rev specified')
        ok = False

if not ok:
    sys.exit(1)
```
The exit code `sys.exit(1)` will signify to GitHub actions that there was an error here.

You could similarly add more checks for the respective models, for example to check that a model's interface matches downstream expectations.
In principle, you could also run more involved validation code here.
For example, you might want to verify that a new model improves a certain key performance indicator (KPI).
However, these kinds of tests are often better left to the research repositories.

## Supporting separate model versions within the same registry

It is generally a good idea to tag every new release of some software. However, in a model registry, you technically make releases for many different software components. Although you could technically still use release tags like "v1" or maybe "v2.0.3" to mark the release of a certain bundle of software, it is usually nicer to have the tags contain both, the released model *and* the version (e.g. cost_predictor@v1.0.3 or transcription@v1.0.0).

Things become more complicated if you also have more than one environment (e.g. development and production or something more elaborate). Maybe you want to run cost_predictor@v1.0.3 in development, but run cost_predictor@v1.0.0 in production. And once cost_predictor@v1.0.3 prove reliable enough, you want to have it run in production as well and replace cost_predictor@v1.0.0. Managing these kinds of things with git tags quickly becomes a nightmare. A tool that makes this very easy, while still mostly using plain git-tags is [gto](https://github.com/iterative/gto). It will simply increment the version of for example the cost_predictor-model if you run
```
gto register cost_predictor
```
This will just create the next tag of the form cost_predictor@vX.Y.Z on the currently checked-out commit. These versions are *purely descriptive*. In other words, gto won't check which models are in the model registry and will happily allow you to release versions of models that are not in your model registry. However, if you make sure that your released tags refer to actual models, this is already a useful way of tracking versions of multiple artifacts inside a single model registry.

On top of model versioning, gto allows you to assign models to "stages". Such a stage could be (for example) different environments. For example, you could use
```
gto assign cost_predictor dev
```
to assign the cost_predictor model from the current commit to the "dev" environment.
More elaborate use of `gto assign` also allows assignments for commits that are not currently checked out.

All these version and stage assignments can be recovered from git tags and gto helps you with a few helper functions. For example,
```
gto latest cost_predictor
```
will give you the most recent cost_predictor version and
```
gto which cost_predictor dev
```
will give you the most recent cost_predictor version that has been assigned to the stage "dev". Note that stages don't need to be physical environments in your system. You could have some stages that refer to actual infrastructure (e.g. staging and prod) and others that refer to different stages in your development and model assessment process (e.g. research or testing).


## Reading a model from a downstream system

One of the key benefits of a model registry is that downstream systems have one single point of truth for machine learning artifacts. There are a couple of ways to deploy models directly from the model registry (e.g. to a docker container or by packaging them as python wheels), but I often find that these deployment scenarios don't match the particular use case I'm in.
However, downstream code can also directly load a model from the model registry. Let's say we want to load our "cost_predictor" from above and let's also assume the model registry is in the repository "mycompany/model-registry", then we can load the most recent "cost_predictor" from any python script by
```python
import mlem.api

cost_predictor = mlem.api.load(
    'cost_predictor',
    project='https://github.com/mycompany/model-registry',
)
```
Neat, isn't it?

Even nicer, we can use the tags from the previous section to load the current production version like this
```python
import mlem.api
import gto.api

model_registry = 'https://github.com/mycompany/model-registry'
model_name = 'cost_predictor'

cost_predictor = mlem.api.load(
    model_name,
    project=model_registry,
    rev=gto.api.find_versions_in_stage(registry, model_name, 'prod'),
)
```
This way, we are pretty free to build systems that rely on machine learning models without knowing much about the internals of those models.

# Conclusion

In this article, I highlighted the benefits of a central model registry and I described how to build such a model registry on top of a regular git repository. I further outlined some specific ways how GitHub features such as pull requests or actions can be used to ensure that models in the registry satisfy certain downstream requirements.
