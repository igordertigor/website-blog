---
draft: false
date: 2021-11-17
categories: [Tech]
tags: [Technology, Startups]
authors: [ingo]
cover_image: 2021-11-17-lessons-for-startups.jpg
comments: true
---
# Technology lessons for startups

Almost no startup sets out with the right idea from the beginning.
It is quite common to change almost everything about what the company's product should do within a few weeks.
From a technology perspective, this is quite challenging: We are used to thinking about creating software that is meant to last, but a startup environment likely means that things won't last very long. Yet, adopting careless attitude towards quality software can be equally fatal, often resulting in a gridlock where nothing can move forward nor backward.

<!-- more -->

Last winter, I read the book [The Lean Startup](http://theleanstartup.com) by Eric Ries.
In that book, Ries defines a startup as an instution creating innovation in an uncertain, high-risk environment.
Amoung other things, he points out that one of the key concept for a startup is "runway", or in other words: "How much longer can we go?"
I was a (part time) product owner at [untether](https://www.untether.ai) by then and mostly looked at this from a product perspective.
A lot has been written about runway from a product perspective, for example in the [great book](https://svpg.com/inspired-how-to-create-products-customers-love/) by Marty Cagan.
And indeed, solid product work is&mdash;although important for any software compony&mdash;particularly important for startups.

As good as this experience as a product owner was, as clear is it to me that I enjoy engineering just as much.
How can an engineering team contribute to stretching out a startup's runway?
I'm explicitly addressing this question from an engineering perspective, but I hope that the essence of these thoughts is accessible to people with a product or business background as well.

One of the key points here is something that Eric Ries already emphasizes: Although we often think of runway as a time (typically in months), it makes much more sense to define runway as the number of iterations that can still be done on the product.
This is useful, because a key challenge for an early stage startup is to find its product niche.
Most ideas for what that niche could be, are wrong.
Ries therefore suggests to (i) make sure that (at least some) customers interact with the product as early as possible and (ii) that changes to the product can be done as quickly as possible.
Point (i) is mostly in the domain of the product owner/manager and ensures that there is a way to actually learn from customers, point (ii) ensures that we can try out as much as possible before the money runs out.
I belive that point (ii) is the responsibility of the engineering team.

# API first

When I worked at [zalando](https://en.zalando.de/?_rfl=de), one of the mantra's in the technology department was "API first".
It made sense at the time, but back then, I wasn't aware how important this point was.
API is short for "application programming interface" and describes the part of a software component that other components interact with.
This is where different teams, different stakeholders and typically different technologies interact.
There is a strong temptation to simply go ahead and write something that "just works".
Resist that temptation.
Get everybody together and discuss which component needs to interact with which component.
What are the minimal points of contact.
If you find out after several [pivots](https://fi.co/insight/what-pivoting-is-when-to-pivot-and-how-to-pivot-effectively) that part of your infrastructure can't support your new usecase, then it is much easier to exchange that part of infrastructure if it has only very few points of contact to the rest.

APIs are particularly important for databases.
It is tempting to simply reach into the database and get out whatever you need.
However, your database will very likely grow rapidly.
Soon every component will depend on some part of the database and changing anything about the database would risk breaking everything else.
However, your database should be adaptable.
Pivots usually mean that some bit of information from your database becomes more (or less) important than before.
You may want to add columns to tables or maybe add new tables.
So you can't apply that change easily and end up wasting a lot of energy and time making it work somehow.
Importantly, this problem becomes more severe with time, as the database grows.
By starting with the API, you ensure that there are no "shortcuts".
You may still evolve the API, but that would usually be something that follows a conscious decision and that involves all stakeholders of the API.


# Deployments

Deployments are a risky business.
It is easy to postpone deployments to the production system because "it is to risky" or because "it takes too much time right now".
However, if you don't deploy your code, there is no chance that customers will interact with it, feedback comes too late and you risk wasting lots of development cycles on something that is conceptually flawed.
Plus, it's quite motivating to have your code run in the production system.
Below are four measures that facilitate regular deployments.

## Agree on a minimum release cycle

Deployments to the production system always feel risky.
Even if you took every precaution and tested everything rigorously, there are usually many aspects that can only really be tested in the real world.
This makes production deployments appear daunting.
It often feels as if your time would be better invested creating new code.
To get used to regular deployments, it can be a good strategy to schedule a fixed time at which a release happens.
For example, you might agree to make a new release at least once per week, for example on Thursdays.
That doesn't mean you can't also deploy on Monday, but it means that you still go through the deployment process on Thursday.
Just make it a habit.

## Continuous Integration / Continuos Delivery

Ideally, deployments should be a no brainer.
In the best case, a deployment should happen automatically while the developer takes a bathroom break.
Continuous Integration and Continuous Delivery (short CI/CD) refers to a number of techniques that support this.
CI/CD systems usually trigger running a number of automatic tests, building a new version of the software and then replacing the running software by the new version.
Making this process fully automatic, including a comprehensive suite of automatic tests, is a lot of work.
Focus on getting most of it to work, maybe cover the most critical cases by a few high level tests.
You might have deployments to your development environment work automatically, but deployments to the production environment still needing one or two (not more) manual steps.
Don't go over board here.
Set up the basic system and evolve it over time like you evolve your other systems too.

CI/CD used to be dominated by Jenkins, which proved kind of difficult to set up.
However, there are more modern systems, such as [github-actions](https://docs.github.com/en/actions), [circle-ci](https://circleci.com), or [travis](https://www.travis-ci.com).

## Feature flags

If you regularly deploy to the production system, you will either need to build very small features (so they can be finished before the next Thursday) or you need a way to hide incomplete features in the production system.
Feature flags provide ways to control access to incomplete features in the production system.
That means that (for example) a developer can access the incomplete feature, but regular user will not see the feature.
Do not go through the hassle of developing feature flags inhouse.
Instead, sign up for a service such as [configcat](https://configcat.com), [launchdarkly](https://launchdarkly.com), or [split.io](https://www.split.io).
All of them have an initial free tier but offer slightly different features in that free tier.
Once set up, feature flags usually also support other things like gradual rollouts by country or just to a small percentage of users.


## Infrastructure

Many real-world computer systems are distributed: Multiple computers work together to support a company's products.
For example, there might be one computer that runs a database, another computer that serves a website and a third computer that provides backend computations for the website.
Managing this kind of infrastructure is a specialist job and takes up a lot of time.

Containers are small, lightweight "quasi virtual machines".
Using containers, instead of actual computers, a distributed system can be abstracted from the actual hardware.
This means, that a developer can prepare a container locally on their laptop and test it rigorously.

*EDIT*: Here I used to advocate [kubernetes](https://kubernetes.io).
Although I still believe that kubernetes is an impressive tool, I find it too large for a small startup.
A much better alternative are often fully managed, serverless offerings from the usual cloud vendors.
For example [Google Cloud Run](https://cloud.google.com/run) or [AWS Fargate](https://aws.amazon.com/fargate/) can run containers in the cloud&mdash;much like kubernetes, but without having to maintain a kubernetes cluster.
If you feel that docker containers are too much overhead for you, you could try out [Google Cloud Functions](https://cloud.google.com/functions)/[AWS Lambda](https://aws.amazon.com/lambda/) or [Google App Engine](https://cloud.google.com/functions)/[AWS Beanstalk](https://aws.amazon.com/elasticbeanstalk/).
All of these will run code in the cloud without the notion of an explicit container or even of infrastructure in the first place.
If the infrastructure is abstracted away/managed by your cloud provider, that means that you don't need to waste person hours handling kubernetes or event virtual machines.


# Considerations about databases

At the beginning, you may not know much about your final database layout.
However, traditional databases (for experts: by traditional, I mean relational) assume that you know a lot about your data format in advance.
If you change your database layout after a pivot, you need to migrate your database.
Database migrations can be equally daunting as production deployments.
This is particularly true for cases where the data consists of a lot of interlinked entities.
Over the past approximately 10 years, a different class of database systems has become popular.
These systems are sometimes called schema-less, non-relational or NoSQL.
Their main strength is usually in their ability to scale to very big datasets.
However, they also have the advantage that they are much more flexible with the required database layout.
In fact, one could store entirely different data elements together in the same "table".
Practically, that usually means that any backward compatible change to the database works without having to migrate any data, thereby providing additional flexibility during the early stages of development.

# MLOps

MLOps refers to a set of practices to deploy and maintain machine learning models in production reliably and efficiently.

This final section is kind of a bonus: If your systems rely critically on machine learning, then you may want to set up a rudimentary MLops system early on.
MLOps systems usually have three components:

1. Practical machine learning is a lot of trial and error.
    A *tracking system* can automatically keep track of every machine learning experiment that was run, making it easier to go back to "that run" that worked really well 2 months ago.
2. An *automatic deployment mechanism* for new model versions.
    For example, after re-training, you may want to use the new version of the model.
    But maybe, you first want to try it out on a limited set of customers, before having a biased or badly generalizing version of the model be released to all customers.
3. Systems for *dataset and model versioning*.

In the beginning, the most important feature here is point 1.
It is possible to write your own tracking system (e.g. just copy logs to an s3 bucket), but tools like [mlflow](https://mlflow.org) or [wandb](https://wandb.ai/site) are much more powerful and usually also offer nice tools for interactively visualizing the results of multiple experiments together.

Points 2 and 3 are somewhat debatable.
Although they address important points, most solutions that I'm aware of are kind of narrow in scope (except for the approach that [DVC](http://dvc.org) is taking, which will be covered in a different article).
You will have to decide yourself if they help in your particular usecase.
Typically, you can add these points later on, after you already have used a tracking system for a while.

*Edit*: After writing this blog post, I wrote two other blog posts that expand upon this topic.
The first is about [using dvc for dataset and model versioning as well as experiment tracking](2022-08-16-version-control-for-data-science.md), the second is somewhat addressing the [topic of model deployment by combining tools like mlem and gto](2022-08-26-github-model-registry.md).

# Summary

I described a number of technical steps that a startup team can take to accelerate their development process and thereby indirectly increasing their runway (was measured in product iterations).
Specifically, I have emphasized the importance of APIs and a smooth deployment process and I have given some hints for how to make the deployment process smoother.
Finally, I pointed out some considerations about data and machine learning architecture.


Do you have experience setting up a technology framework for a startup? What are your experiences? Which points do you think matter most in this post? Where do you disagree? Please let me know all of these things in the comments section.
