---
draft: true
date: 2023-09-13
categories:
  - General
authors: [ingo]
cover_image: 2023-09-new-blog-layout.jpg
comments: true
---

# New blog layout

With this I'm switching to a new blog layout based on [material for
mkdocs](https://squidfunk.github.io/mkdocs-material/) rather than the old
layout based on [pelican](https://getpelican.com). I tried to keep the mostly
white layout from the previous blog, but still went with a generally more
modern look and feel. In addition, the new and shiny blog provides a couple of
new features that I feel are improvements.

## Cover images

As you can see at the top of this page, blog posts can now have a "cover
image". I also added cover images for all past blog posts. All the cover images
have some connection to the actual post, but the connection is usually quite
loose&mdash;an association I had with a word in the title or something of that
sort. Usually, the cover images also are parts of larger images that contained
the association. Hence, it may not always be obvious how the link is. I don't
think that's necessarily an issue: I mostly added the cover images to add
something a bit more visual to the posts and maybe add some color as well.

## Avatar in the blog summary

In an effort to add more visual items to the blog, I also added small avatars
of the author to each blog post. At the moment, there is always just one
author, so this is slightly redundant (although I think it looks nice). I hope
the occasionally have guest authors in the future. By then, the avatars might
also help tell the different authors apart.

## Preview of the reading time

Each blog post now has an associated "expected reading time". This should make
it easy enough to get a rough idea if a post fits into your break or if you
should schedule time for it. I didn't invent the reading time feature: It's
just part of the default material for mkdocs blog template, but I kind of like it.

## Summaries are the start of the post

In the past, I wrote separate summaries for the different blog posts. This
appears to be part of the [pelican](https://getpelican.com) logic for writing
blog posts. The new template takes a different stance here and assumes that
summaries are the initial sentences of a post. I didn't want to overly change
past posts, so some of the teaser texts might appear a little weird. I'm not
entirely sure about this. Maybe it is just another way of writing that I have
to get used to, but maybe it's a little limiting. What do you think?

## Comments

And that gets me to the next point: You can now write comments and "reactions"
(i.e. smilies). I feel that adding this feature is overall an improvement, but
I'm not sure if this particular commenting solution is ideal. On the one hand,
it's based on GitHub discussions and is therefore quite easy to set up and has
the comments stored very transparently. On the other hand, it requires a GitHub
login, which I find a little ugly. I'm also not really familiar with the
moderation tools for this. But the good thing is: You can tell me what you
think of this. Please do!

I enabled comments for all past posts (was that a mistake?) and that meant that
I had to add a small paragraph to the end of each post to encourage comments.
Apart from that, I tried to keep the original post intact. Many of these posts
are time specific: They may refer to problems that I don't have anymore, or they
may answer questions in a way that I wouldn't answer them anymore. I think
that's fine. I like going back in time occasionally.

## Public repository

I write all blog posts as markdown posts and I store previous versions in a git
repository hosted on GitHub. The comments-functionality required that I made
the repository public. As a result, anybody can now see my drafts and all
history of drafts. Initially, I didn't really feel comfortable with that. After
all, some of the drafts are really far from how the final thing should look
like. They may even contain opinions that aren't really my own or that are
easily misunderstood.

On the other hand, a public repository also means that (in theory) you could
write a post and make a pull request. If you have something that you would like
to see on this page, please do so. I'd love to take a look and expand the range
of authors.

## Easier handling

This is mostly for me: The pelican template I used was a little obscure. I
found it difficult to add functionality to it, and it always took a lot of
effort to figure out what went where. Hence, I tried to never change it. Most
of the changes that came with the switch to material for mkdocs would have been
possible with pelican as well. But they all seemed extremely complicated.

## Things that went

One functionality that I really liked about pelican is their "draft"
functionality. Drafts can be hosted along with other posts, but their URL is a
little hard to guess, and they don't appear in indexes. As a result, you would
have to know the correct link to see a draft post. I used that a lot to share
early versions for some of these posts with friends and have them comment.
I'm not sure how much I will miss this and how I will handle this in the
future. However, I believe that the other points really outweigh this one.


--

How do you feel about the new blog layout? Do you think it's an improvement? Do
you run a blog as well? How is your setup? You can now answer all of this in
the comments!
