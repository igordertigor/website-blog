Title: Semantic versioning and semv
Date: 2023-08-30 16:04
Category: Software Development
Tags: Versioning
Slug: semantic-versioning-and-semv
Authors: Ingo Fruend
Summary: It is somewhat clear that software releases should carry a version like v3 or v1.1 or something. But this often seems more or less arbitrary, and you might feel that just counting git-commits or adding the current date would do equally well.
status: draft

It is somewhat clear that software releases should carry a version like v3 or
v1.1 or something. But this often seems more or less arbitrary, and you might
feel that just counting git-commits or adding the current date would do equally
well. After all, these would be easy to create automatically and once set up,
you would never have to think about versioning again.

In fact, I used to think that way. I don't think so anymore though. In fact, I
believe that versions are a key ingredient in decoupling different software
components. At least if the versions are done right.

## Why do we have versions? Dependencies and releases

Let's take a step back and think for a moment: Why do people create version
identifiers for their software? Apart from a number of marketing reasons ("Wow,
look at this, we just did a major release. Expect lots of cool new features!"),
there are actually very valid technical reasons too.

Versions are a means of communicating changes to your users. Of course,
this only really applies to technical users who want to use your software as an
API or a library (and this post will mostly focus on libraries with a few
mentions of APIs). Ultimately, what you are telling your users is: "This is a
new version, expect things to change". Based on this information, your users
can decide if and when they want to switch to using the new software. Maybe,
they say to themselves: "You know everything is working fine for us. We don't
want to respond to things changing. We'll just stick with the old version." And
that's of course a perfectly valid decision.

In this example, I assumed that version identifiers can only carry this one
message: "Things may change." Is there more that, that could be conveyed? It
depends.

## How should we assign version identifiers?

There are in fact a number of ways how "things may change". Hence, it makes
sense to broaden the vocabulary for communicating with your users.

## Sounds like this could be done automatically...

## Introducing semv, a semantic version commit parser

## Conclusion
