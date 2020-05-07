Title: Playing with Elm
Date: 2020-04-27 12:41
Category: Programming
Tags: Elm, Front-End, Functional Programming
Slug: functional-programming-with-elm
Authors: Ingo Fruend
Summary: Functional, type save, elegant, ... and it all works in a browser.

When it comes to adding dynamic functionality to websites, [javascript](https://www.javascript.com/) is the number one technology.
And javascript is not as bad as its reputation (or as it used to be).
You can do really nice things with javascript&mdash;in particular in combination with css.
Of course, javascript is not flawless, but it does the job.
And after all, when it comes the dynamic functionality in websites, there isn't really that much competition...

About a year and a half ago, I came accross a tweet that said something like "Oh, Elm is so nice".
For some reason, I [looked it up](https://elm-lang.org/).
"A delightful language ..." is the first thing you see on their website.
And oh&mdash;you need to compile it? To javascript?
Doesn't that more or less defeat the purpose?

I still gave it a try and played with it a bit.
In the meantime, I have written a number of small web-apps in Elm: A submission platform for student assignments (no longer online), a super simple [training app for jazz scales](http://scales.ingofruend.net), and a [pomodori timer](http://pomodoringo.ingofruend.net).
The latter two took somewhere between two and three hours to get up and running (their also quite simple).
Yes, you could do that in javascript as well, but for some reason, Elm makes the problem appear more structured and makes it easy to write code that you can later modify without ever breaking anything (well, you see right away if it's broken and can fix it).

I believe that the key feature of Elm are *limits* (technically "boundaries" would be a better word here).
There are certain things that you just can't do with it.
For those, you have to call out to "low level" javascript.
That might sound useless. After all you still have to use javascript for some things.
It's actually quite good.
Elm's strict boundaries ensure that you always deal with very limited scope and within that limited scope your problem usually isn't so hard anymore.
You also don't loose track of global variables, because there are none.

Elm has fairly strict types and much of Elm programming consists of reasoning about types.
In fact, instead of runtime errors, you get special types.
Functions that might fail when determining, say, an `Int` just don't return an `Int`, but a `Maybe Int`.
If something went wrong, and you do not happen to get your expected value, that `Maybe Int` takes the value `Nothing`, otherwise it takes a value like `Just 3`.
This means that you can't really do anything useful with your `Int` until you properly handled the `Nothing` case.
Super-annoying for the first 45 minutes or so, but at some point, you notice that it's actually not so bad at all.
Javascript often gives up on runtime errors.
Elm detects most of them even before you manage to run the code and it guides you to fixing it.

At first sight, Elm code looks almost like [Haskell](https://www.haskell.org/) so it might need some acclimatisation for many.
But like Haskell, Elm is so much of a functional language, that there is basically no difference between variables and functions.
In fact, the statement `f = 5` could be understood as either "the variable `f` is assigned a value of 5" or "the function `f` takes no arguments and always returns 5".

In conclusion, Elm won't replace javascript, but it is fun to use and is less error prone than javascript.
It's worth trying out and luckily, it interacts quite smoothly with regular javascript.
So it's totally possible to just write a single component of a bigger application in elm.
Or of course use Elm for a smaller project like it did.
