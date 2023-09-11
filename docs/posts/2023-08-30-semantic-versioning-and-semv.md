---
draft: false
date: 2023-08-30
categories:
  - Tech
tags:
  - Versioning
authos:
  - ingo
cover_image: 2023-08-30-semantic-versioning-and-semv.jpg
---
# Semantic versioning and semv

It is somewhat clear that software releases should carry a version like v3 or
v1.1 or something. But this often seems more or less arbitrary, and you might
feel that just counting git-commits or adding the current date would do equally
well. After all, these would be easy to create automatically and once set up,
you would never have to think about versioning again.

In fact, I used to think that way. I don't think so anymore though. More yet, I
believe that versions are a key ingredient in decoupling different software
components. At least if the versions are done right.

<!-- more -->

## Why do we have versions? Dependencies and releases

Let's take a step back and think for a moment: Why do people create version
identifiers for their software in the first place? Apart from a number of
marketing reasons ("Wow, look at this, we just did a major release. Expect lots
of cool new features!"), there are actually very valid technical reasons too.

Versions are a means of communicating changes to your users. Of course,
this only really applies to technical users who want to use your software as an
API or a library (and this post will mostly focus on libraries with a few
mentions of APIs). Ultimately, what you are telling your users is: "This is a
new version, expect things to change". Based on this information, your users
can decide if and when they want to switch to using the new software. Maybe,
they say to themselves: "Well, everything is working fine for us. We don't
want to respond to things changing. We'll just stick with the old version." And
that's of course a perfectly valid decision.

In this example, I assumed that version identifiers can only carry this one
message: "Things may change." Is there more, that could be conveyed? It
depends.

## How should we assign version identifiers?

There are in fact a number of ways how "things may change". Hence, it makes
sense to broaden the vocabulary for communicating with your users. Different
versioning *schemes* attempt to do that. For example, one can use dates as
version numbers to communicate when the release was published. If a user than
finds that they are running their software on release 1998-06-01.1, they know
that it might be a good idea to think about upgrading eventually.

Some software uses version numbers like 1.3 or 2.0. Most people somewhat
intuitively understand that version 1.3 was before version 2.0 and that
incrementing the part before the dot indicates something more significant than
incrementing the part after the dot. However, what do they indicate?
For many software projects the distinction is somewhat arbitrary.

So what could we as developers attempt to tell our users with a version
identifier? Can we try to be more specific about the kind of change that
happend between the two versions? [Semantic versioning](https://semver.org)
attempts to do just that. It classifies possible changes between software
versions into three classes

1. *Major* changes are anything that breaks the interface of the software. In
    other words, after a major change, a downstream user (an imaginary
    downstream user who uses all features) *must* change the way they use the
    software. Of course in reality not everybody has to change the way they use
    the software, but if a major change is communicated it is a good idea for users to
    check if the changes will affect them.
2. *Minor* changes add functionality. Typically this will be a
    new feature. Minor changes offer a chance to use the software
    differently&mdash;after all you could now use the new feature&mdash;but
    whatever you did before will still work fine.
3. *Patch* changes mostly affect the inner workings of the software.
    These are usually bug fixes or performance improvements. There is no reason
    to change your code really, but you can expect things to just work a little
    more smoothly and efficiently.

With semantic versioning, we encapsulate these three kinds of changes into a
version number: vX.Y.Z, where X=Major version, Y=Minor version and Z=Patch version.
Often, there are additional qualifiers, for example in
[python](https://peps.python.org/pep-0440/), there are several postfixes to
indicate things like release candidates in which the actual version is altered
but the major, minor and patch components remain the same.

Semantic versions are useful, because they mean that you know in advance what's
going to happen if you upgrade to a new version. You can also specify that
you want a version between v1.3.0 but less then v2.0.0. For example in a
python requirements file, you would state this as `~=1.3`. If you rely on a
fix that was introduced in version 1.3.2, you could write `>=1.3.2,<2.0`.
This allows freely installing packages without risking to get something that
will break your code.

> A brief remark on APIs: For APIs, hosting multiple concurrent versions can be a
> lot of hassle. It is therefore common, to only host separate versions for each
> major version, but apply minor and patch releases as they come. This tends to
> be an ok compromise between compatibility and hosting many separate API
> versions.

## Sounds like this could be done automatically...

You may be wondering if semantic versioning could be done automatically. And
the answer is both, yes and no. "No", because no version identification tool can
know if the changes in the code are implementing a new feature or fixing a bug.
"Yes", because it would in principle be possible to [convey that information
through commit messages](https://www.conventionalcommits.org/en/v1.0.0-beta.4/).
Once commits contain the information about what kind of change has been committed, a
[versioning](https://www.npmjs.com/package/semantic-release) [tool](https://python-semantic-release.readthedocs.io/en/latest/) could parse
the information from the commit messages and generate new software versions
based on this information.

Do you want to do this automatically? Although I strongly recommend using
semantic versions, I don't think that all packages must be automatically
versioned. Specifically, if a dedicated person is responsible for managing the
features that should go into the next release and planning when that release
would be, then it might be a valid decision to leave the version number to that
person. After all, that person might feel that it is a good idea to group
multiple breaking changes together into one big major release and add features
incrementally in separate releases (I would also agree with that person).
However, planning releases like this is quite a lot of work and it might not be
worth it for a small open source project. Furthermore, even a dedicated release
manager might still decide to generate the version identifiers automatically.

If your project or organization is to small to have someone who specifically
manages releases, then automatic semantic versioning is likely great. For
example, one could setup a continuous integration system to create a new
release every time a pull request gets merged&mdash;of course this setup would
need to automatically generate version numbers.

## Introducing semv, a semantic version commit parser

In the previous paragraph, I linked two software tools that perform semantic
releases above. One is the "original" [semantic release npm
package](https://www.npmjs.com/package/semantic-release). However, my main
language is python and the npm package only releases to npm. I therefore also
linked the package [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) which
performs something similar for the python world of pip and pypi.org.

I personally found the semantic release packages to attempt to do too much.
They create new versions, but they also add commits with version specifiers and
potentially even push them to GitHub without you knowing. In addition, they
upload packages to a central repository and make releases on GitHub. Although
this can be great, it can also be in your way&mdash;a lot! Furthermore, when
playing with python-semantic-release, I felt that I would often mess up the
commit format or (worse yet!) forget to mark a breaking change correctly.
Often I found out about my mistake after python-semantic-release had done its
thing. As a result, I had to even roll back an accidentally released minor
version.

What I want is a tool that simply determines the next release number but leaves
the releasing to my discretion. In fact, I want a tool that does not change
anything by itself and requires minimal configuration. After I didn't find that
tool, I wrote it myself and called it
[semv](https://semv.readthedocs.io/en/latest/) like semantic version parser.
I can run semv as part of an [automatic release
process](https://github.com/igordertigor/semv/blob/master/.github/workflows/attempt-release.yml)
or as a [`commit-msg`
hook](https://semv.readthedocs.io/en/latest/alternative-usage/). It has
absolutely no *required* configuration (although it can be configured via
`pyproject.toml`) and it will *never* change anything about your repository.

Using semv is dead simple:
```bash
  $ semv
```
This command will print the version that your software should get *if you would want
to release from the current commit*. There is just one requirement: If you
decide to actually do a release, you should tag it with a message of the form
vX.Y.Z. These tags will be used by semv to analyze only commits since the last
version tag.

One issue with automatic semantic releases is, that people may accidentally
forget to mark a change as "breaking". As a result, the new version would be
marked a minor (or patch) release and people would install that breaking change
without much consideration. Of course afterwards their dependent software is
broken. [Stephan Bönnemann](https://www.youtube.com/watch?v=tc2UgG5L7WM), one
of the authors of the original semantic release npm package, suggests an
additional step to verify a version identifier: Running the tests of the
previous version on a new release candidate. If the previous version's tests
fail, then the release is almost certainly broken.

In semv I added an option to include [additional verification
checks](https://semv.readthedocs.io/en/latest/checks/). However, only one such
check is implemented so far: running the previous version's tests against the
new release candidate (using [tox](https://tox.wiki/en/4.11.0/)).

## Conclusion

In this post, I pointed out that version identifiers are a way for api and
library developers to *communicate changes* to their users. I further argued
that semantic versioning is a versioning schema that compactly conveys the most
important information about the changes that go along with a software release.
I then introduced semv as a tool to automatically create version identifiers by
parsing commit messages.
