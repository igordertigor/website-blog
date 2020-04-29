Title: Comparing scala, python and c++
Date: 2020-04-26 16:58
Category: Programming
Tags: Python, C++, Scala
Slug: scala-python-cpp
Authors: Ingo Fruend
Summary: Types are really cool
status: published

In an ancient time, I wrote code in C++ ([see here for a now dead project I was involved in](http://psignifit.sourceforge.net/)).
Since then, [python](https://www.python.org/) has clearly dominated much of my programming and I came to really love it:
Python is concise, readable and easy to learn (and teach).
And I really liked python's duck typing approach, which basically meant that you never really had to worry about types.
Then, over the past maybe 5 years, a number of different people kept praising the elegance and power of [scala](https://scala-lang.org/) and they often highlighted one particular strength of scala: static types.
What!? Wasn't that something that I had never liked about C++ and that I was glad to leave behind?

In the past couple of weeks, I made it a point to do a number [coding katas](https://en.wikipedia.org/wiki/Kata_(programming)) in all three of these languages.
Not surprisingly, all three of them have their advantages.

# Python

Things that are really cool about python

- Crazy ecosystem: With libraries ranging from [pytorch](https://pytorch.org/) to [pandas](https://pandas.pydata.org/) to [hug](http://www.hug.rest/) to [pillow](https://python-pillow.org/) to [psychopy](https://www.psychopy.org/) to [saltstack](https://repo.saltstack.com/) it feels like anything you can think of is already there&mdash;and often pretty good. If you have some time to kill, take a look at the extensive (yet far from complete) list at [python awesome](https://github.com/vinta/awesome-python).
- Writing tests with python is *really* easy. Why? Because everything is duck typed and mock objects come almost for free.
- You write code to fit your problem and not an abstract programming paradigm. Specifically, you are free to use object oriented programming for object problems and functional programming for function problems. Obviously, that doesn't free you from having to write readable and maintainable code but that's another problem in itself.

Unfortunately, some things are also really annoying about python.

- The *global interpreter lock* (GIL) is certainly the first thing that comes to mind. Yes, some libraries manage to get around it, but for the most part, the GIL means that it isn't really easy to make full use of even fairly standard hardware (i.e. dual core processors). Yes, one could use [separate processes](https://docs.python.org/3/library/multiprocessing.html) or even more [heavyweight solutions](http://www.celeryproject.org/), but it is always either ugly or feels like overkill.
- Unit tests need to cover a lot of cases of the form "What happens if I call this function with the wrong type". Often, these tests don't really test any meaningful application logic, they just make sure that things behave reasonable if users don't really pay attention.

# C++

Some things are cool about C++.

- Performance: Well written C++ code is highly performant.
- C++ allows writing template code. That is code which instructs the compiler how to write (often quite optimized) code for the types that are ultimately used.
- C++ can access low-level properties of your hardware and perform fairly specific low-level tasks. Obviously, that includes creating multiple parallel threads of execution.

Yet, C++ has a bunch of disadvantages.

- Verbosity: There is so much stuff that you need to specify that the code ultimately becomes more difficult to understand than it would have to be.
- There are different categories of code files. This is probably hard to grasp for people coming from a more high-level language: C++ has two types of code files. On the one hand, there are "header" files, that (loosely) contain only the function names (a bit more) and on the other hand, there are proper code files that typically contain the implementations of these functions.
- Manual memory management and pointer arithmetic. C++ requires that the programmer allocates memory for variables before using them *and later de-allocates that memory* when the variable is no longer needed. Related to that, C++ can access variables either by their name or by their memory location. In fact, memory locations are stored in a special type of variables called pointers. Experienced C++-programmers do calculations even with pointers to pointers. Although this pointer business helps with the performance (see above), it is a great opportunity to make mistakes&mdash;really subtle mistakes that don't immediately break everything, but lurk in the background and hurt you right when you think you have it all under control.
- Unit tests beyond the most basic level are a pain.

# Scala

I agree, scala is really awesome. In a way, it brings together the performance and multi-threading capabilities of C++ with the high-level thinking of the python world.

- Variables are statically typed, so you don't need to write a ton of tests for incorrect types.
- Running things in parallel (threads, processes or [whatever else you like](https://akka.io/)) is really not hard.
- There is an extensive and mature ecosystem that was inherited from [java](https://www.java.com/en/).
- Mock objects aren't for free, but [they're not very costly either](https://scalamock.org/).
- Your problem calls for an object oriented approach? No problem, scala can do that. Your problem is best thought of in terms of functional programming? Scala does that too&mdash;and really well.

Turns out, the disadvantages of scala didn't immediately come to me. Here are some

- Lightweight projects are clumsy&mdash;a few lines of code that you put into your `PATH` to do something useful&mdash;are not quite so quick and easy with scala. But maybe it wasn't designed for that anyway.
- Interactive coding is a little clumpsy. Yes, there is a [repl](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), but nobody would really try to solve problems in it (unlike in [ipython](https://ipython.org/)).

# Conclusion

Different programming languages have different strengths and weaknesses.
Here I summarized some experiences that I had with Python, C++ and Scala.
Scala is fairly new to me and I am positively surprised by it, but it certainly won't act as the [glue](https://www.python.org/doc/essays/omg-darpa-mcc-position/) that python is and it is more removed from low-level computing than C++.
