---
draft: true
date: 2022-08-12
categories:
  - Tech
tags:
  - test driven development
authors:
  - ingo
cover_image: /images/2022-08-12-pragmatic-approach-to-testing.jpg
---
# A pragmatic approach to software testing

The other day, a colleague asked me about a good testing strategy for a new service he was developing.
In general, I find that tests are extremely important.
They give confidence when making changes and tend to push me into writing code that has fewer dependencies and is easier to understand.
However, writing good tests that really cover all use cases and all branches through your code is a lot of work.
As a result, taking up technical debt tends to affect tests quite early on.
Is there a pragmatic approach to testing? Like a testing core that should not be sacrificed in order to quickly squeeze out a few more features?
<!-- more -->
I think there is.

Here are a few points for building up test coverage as a service is developing over time.
The first four points contribute to building an initial MVP-version of the service (I'm writing service here, but the same obviously applies for command line tools or libraries as well):

1. Build an initial version against a few high-level scenarios that an MVP needs to cover.
2. Test components that you are unsure about.
3. Use code checkers/linters from the beginning.
4. Use few mocks.

You can now probably release an initial version of your service.
After an initial release, I try to increase coverage&mdash;both in terms of unit tests (5) and in terms of high-level scenarios (6).
In the following, I will address these six points in a bit more detail and recommend a couple of tools in the python world.

# The path to the initial release

The standard way to run tests in python is by using [tox](https://tox.wiki).
Tox is a test runner for python, and it supports a lot of different options, such as running different kinds of tests, with different python versions and different other packages installed.
Tox is configured through a file `tox.ini` and I will in the following occasionally refer to this file.
However, the details of how this is set up can be found on the [tox website](https://tox.wiki).
I'm also providing a very opinionated [cookiecutter](https://www.cookiecutter.io) template on [GitHub](https://github.com/igordertigor/templates) that contains (among others) a useful `tox.ini` file.

## Automatic tests

In particular, when there are almost no users, it can be tempting to start out by just doing some manual testing and then shipping a new release and hoping that nothing breaks.
Resist the temptation!
If your tests don't run automatically, you have to assume that they don't run.
If the testing procedure is not written in code, you have to assume that steps are skipped.
Services like [GitHub actions](https://docs.github.com/en/actions) or [travis](https://www.travis-ci.com) allow running test code in response to triggers such as opening a pull request or merging code to certain branches.
They are almost always worth the money.


## High-level scenarios

Usually, we have one or two common use cases in mind when we write a piece of software.
While we work on an initial release, we ideally want to check these use cases regularly and not write code that doesn't help with this core functionality.
For example, we might want a command line tool to be usable in one particular way, or we want to ensure that a neural network quantization library maintains prediction accuracy of one or two fixed networks.
For an application programming interface (API) that we want to provide through a web server (e.g. [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), [GraphQL](https://graphql.org) or [JsonRPC](https://www.jsonrpc.org)), we may have a few common usage flows that we want to test.
In any case, these high-level tests should be *specified in code* and there should be a *clear indication of success of failure*.
Taken together, these two criteria mean that these high-level test scenarios can be run repeatedly by just calling the respective piece of code.

High-level tests of a library or an API can be written in [pytest](https://docs.pytest.org/), but it is good practice to mark these tests in some way.
You would need to define these markers in your [`pytest.ini`](https://docs.pytest.org/en/7.1.x/reference/customize.html?highlight=configure).
Good marker names are `scenario` or `workflow`.
Some people also refer to these tests as "integration" tests, but I feel that this term implies testing that is more focussed on the interaction of different services.
However, if the service you are testing depends on a running database, scenario tests should actually start a real database locally (this is also emphasized in the [12 factor methodology](https://12factor.net/dev-prod-parity)).
If the service you are testing involves contact with data or machine learning, scenario tests should use a real dataset (potentially down-sampled).
Runtime isn't super critical here.
It's fine if your scenario tests take a bit of time to run&mdash;as long as they are deterministic and capture a real use case with sufficient detail.
In some cases, it may be an option to have two versions of the same test: One that takes 15&ndash;30 minutes and gives a realistic picture of the ML accuracy and one that takes 30&ndash;60 seconds and gives a realistic idea of weather or not the code still runs at all.
It's a good idea to capture the full setup of your scenario tests inside your `tox.ini`, but to keep the slow running ones out of the `tox.envlist` (the list of tests that run automatically when you run tox).
This way, slow running scenario tests won't discourage you from running your other tests as often as possible.

Writing scenario tests for a library or an API can usually be done within the programming language you are targeting&mdash;after all, they are expected to be called in code.
For command line tools, this is different.
These tools are expected to be (predominantly) called in an interactive session.
Often, the output that these tools produce on the console is particularly important.
A good tool to specify test scenarios for command line tools is [cram](https://bitheap.org/cram/).
With cram, you can simulate a user's input on the command line and test the tool's output in well-defined scenarios.
Other tools for testing command line tools are [BATS](https://github.com/bats-core/bats-core) and [shunit](https://github.com/kward/shunit2), but both are more focussed on unit testing than actually testing whole usage scenarios.

## Unit tests if you are unsure

The term "unit test" refers to tests that target an individual component (e.g. a function or class) of your code.
It sometimes appears that unit tests are seen as a kind of silver bullet among (often more junior) developers.
Some of this is justified: Writing unit tests usually happens concurrently with writing the actual production code and thinking about isolated testability often steers a developer quite naturally toward better encapsulation of different code components.
Quite a bit of the excitement about unit tests is unjustified: Passing unit tests are never a guarantee that the system works as a whole, writing unit tests that really cover all corner cases is difficult and takes lots of time, and unit tests have a tendency to make a code base more rigid, slowing down future changes.

In practice, we all write unit tests in a very natural way.
If we write a function where we aren't entirely sure if it works as expected, we all test it out in isolation.
We may use an interactive python session for this or (for compiled languages) write a small and isolated program to try out the functionality and make sure it works as we expect.
Keep these ad-hoc tests and directly enter them in your suite of unit tests.
This way, you can run them automatically.

Unit tests should be fast to run, and you should trigger them with a single short command.
If you develop in python, it's a good idea to use [tox](https://tox.wiki) to run your tests (short command) and to configure tox to have your unit test suite inside the `tox.envlist` for at least one python version.


## Use code checkers

For most programming languages, there are a bunch of tools to validate your code without running or compiling it.
For example with python, there are tools like [flake8](https://flake8.pycqa.org/en/latest/), [pylint](https://www.pylint.org) or [ruff](https://beta.ruff.rs/docs/) that ensure that your code is (i) syntactically correct and reasonably well formatted.
In addition, there are static type checkers like [mypy](https://mypy-lang.org) that verify that functions are called with the arguments for which they are intended.
These tools are great (if configured correctly).
They run within less than a second and catch most of the really stupid errors&mdash;forgot to import a library (flake8), mixed up the order of arguments (mypy), ...

In addition to code *checkers*, there are also code *formatters*.
Examples for these are [black](https://black.readthedocs.io/en/stable/index.html) or [autoflake8](https://github.com/fsouza/autoflake8).
Many people love these tools, and I've had heated discussions regarding their usefulness.
I've recently started using one of them ([blue](https://blue.readthedocs.io/en/latest/)) and I find it much better than I expected.
However, auto-formatting will not detect missing imports or syntactic errors&mdash;it will only change the format of already syntactically correct code.

## Few mocks

A "mock" or "mockup" is a class that allows you to replace parts of your system by an empty shell. For example, the mockup of a database could be just a class that returns predefined values when called, so that you can check if the rest of your system responds to these values correctly.
In your scenario tests, you aim to test realistic interactions with your code on a high-level.
Mocks will take away from the realism of these tests.
It is therefore a good idea to use them as little as possible.
Instead, you can often use techniques such as [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) to avoid a lot of mock objects.
Ideally, you wouldn't need any mocks, but it might make sense to replace non-essential external services by a mockup.
A typical example would be third party services that handle [feature flags](https://martinfowler.com/articles/feature-toggles.html) or [performance monitoring](https://sentry.io/welcome/).

# Conclusion

I described a core testing strategy for an early, fast moving software product.
My focus here was on static code analysis and high-level automatic tests.
This isn't supposed to imply that there is no value in denser test coverage or that one shouldn't strive for higher test coverage.
However, given the choice between features and tests, most companies will go for features.
My attempt here is to point out somewhat of a minimum level of automatic testing that still supports the strong feature focus that is usually needed to get a software product off the ground.
