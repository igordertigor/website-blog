Title: Vim vs. Emacs
Date: 2020-02-27 21:41
Category: Technology
Tags: vim, emacs
Slug: vim-vs-emacs
Authors: Ingo Fruend
Summary: Two different philosophies
status: published

The other day, I had lunch with my friend [Ori Barbut](https://www.oribarbut.com/) and it turns out, we both seem to have a passion for a fairly mouse-free computer experience. However, the center pieces of our interaction with a computer are quite different; Ori uses [emacs](https://www.gnu.org/software/emacs/) and I use [vim](https://www.vim.org/). Ori is certainly interested in vim and I have quite extensively used emacs in the past, so much of the conversation circled around the why-and-why-not of the editors we are using.

I couldn't imagine writing any text on a computer without vim. Yet, the conversation with Ori made me think. Ori's environment can effortlessly do all kinds of things that sound really interesting.

It took me a couple of days to be able to express what exactly it is that makes vim stand out for me: Motion (and Text objects). When learning vim, most people focus on using the hjkl keys to move the cursor around and they try to avoid the arrow keys. You often hear people praise the fact that by using hjkl navigation, you never have to take your hands of the "main" keyboard. Although that's true, it isn't the main part for me. Vim offers a great number of ways to navigate and refer to content in *semantic chunks* rather than line by line or character by character. The keywords here are *motion* (moving around) and *text objects* (referring to entities). I believe that these two are what makes vim feel like an extension of my body rather than a tool that I choose to use or not.

When using vim (at a non-trivial level), you typically construct commands that consist of three components

    [count]<action><motion or text object>

For example, you might type `4gk` to (g)o to the location (4) lines up (k). (In fact, in this case, you could omit the "g".)
Similarly, you could type `4dk` to (d)elete from the current position to 4 lines up.
So the `count` specifies *how often* you want to do something (if omitted we do it once), the `action` specifies *what* you want to do and the `motion or text object` specifies the *target of your action* &mdash; on what you want to apply your action.

When we think about how we want to edit a file, we typically think in terms of sentences of text, in terms of functions, classes, and variables. Yet when we actually want to perform that edit, we have to ultimately tell our editor something of the sort of "delete this character", "replace the next 5 characters by this", ... That's where motions and text objects enter the game. To extend the example above, vim understands `w` as a motion forward to the beginning of the next word, so `4dw` will delete from the current cursor position up to the fourth word to the right.

Text objects can be thought of in a similar way, but without the movement. For example `aw` is the "outer word" text object, which means "the word under the cursor *and* the surrounding spaces" (`iw`, the inner word is without surrounding spaces). Although, I can't *move* by a text object, I can apply an action such as "delete" to a text object. For example, I can say `4daw` to apply (4) times the (d)elete action to the outer word (aw). Similarly, `4dis` deletes four sentences (specifically "inner sentences", leaving trailing spaces).

There are text objects for stuff in single quotes, double quotes, parentheses, brackets, braces, function bodies, class definitions, html-tags, variable names, ... Using motions to move around and text objects to specify the target of an action skips that additional step of translating intention into character-by-character operations. And I believe *that* is what sets vim apart.
