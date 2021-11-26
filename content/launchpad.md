Title: Launchpad Pro Mk3 with Bitwig on Linux
Date: 2020-08-25 21:45
Category: Music
Tags: Bitwig Studio, Launchpad Pro
Slug: launchpad-with-bitwig-on-linux
Authors: Ingo Fruend
Summary: I recently bought a Launchpad Pro Mk3 and noticed that it wasn't all that easy to integrate into my linux setup. Here is how I got it working.
status: published

For my birthday this year, I got a [Launchpad Mini Mk3](https://novationmusic.com/en/launch/launchpad-mini).
It's the first time I've used what is called a grid controller and I really found the workflow incredibly intuitive.
Thanks to the really [good key bindings](http://www.mossgrabers.de/Software/Bitwig/Bitwig.html), navigating [Bitwig](https://www.bitwig.com/en/home.html) felt way more direct.

However, I noticed quite soon, that I often tried to play chords, melodies and beats with the pads on the Launchpad Mini.
Emphasis should probably be on "tried" here:
The pads of the Launchpad Mini are definitely not made for actually playing music on them.
So although the Launchpad Mini is great for triggering scenes in Bitwig, playing with some of the effects and generally navigating the interface, the lack of velocity sensitive pads seriously limits it as a musical instrument and I soon began eyeing for the bigger siblings of the Launchpad Mini&mdash;the [Launchpad X](https://novationmusic.com/en/launch/launchpad-x) and the [Launchpad Pro Mk3](https://novationmusic.com/en/launch/launchpad-pro).
I ended up purchasing the "Pro" version&mdash;those additional buttons seemed quite tempting.

Unfortunately, getting this to work wasn't really a plug and play experience.
It turned out that not all steps are well documented (or documented at all) online.
Here is how I ended up getting it to work (and yes it's been great since then).

## Step 1: Mossgraber's controller scripts

The first step in the process was to download J&uuml;rgen Mossgraber's most recent version of his controller scripts from [here](http://www.mossgrabers.de/Software/Bitwig/Bitwig.html).
I already knew these keybindings from the Launchpad Mini and they seem to be kind of the go-to solution for all Launchpads.
They are really well [documented](https://github.com/git-moss/DrivenByMoss-Documentation/blob/master/Novation/Novation-Launchpad.md) and the documentation is [super easy](https://github.com/git-moss/DrivenByMoss-Documentation/blob/master/Installation.md).

Unfortunately, the Launchpad didn't work after installing the scripts.
Bitwig reported that "my controller" was now "ready to use", but in fact that was about it.
Lights on the Launchpad worked, but it seemed to be in the documented standalone mode.
Although that's certainly a nice feature about the Launchpad Pro, I wanted this thing to work with Bitwig on my computer.
I tried all kinds of things, but there seemed to be no way to get this thing to communicate with my computer.

## Step 2: Upgrade firmware

[This redit post](https://www.reddit.com/r/Bitwig/comments/hm4vfu/linux_bitwig_novation_launchpad_pro_mk_3/) was the key to getting it to work.
mmntmtrnstn reports that updating the Launchpad's firmware solved the problem for them.
Too bad they didn't say how they upgraded the firmware.
After a lot of looking around, I found [this website](https://fw.mat1jaczyyy.com/firmware) that uploads a "hacked" firmware to the Launchpad.
This website uses Chrome's ability to run midi to flash the Launchpad (so obviously it doesn't work with Firefox).

The website asks to put the Launchpad in "Bootloader" mode.
In order to get there, you need to press the "Setup" button on the Launchpad while connecting the device.
After that, you can simply flash the new firmware.

Obviously, the first attempt ended up uploading an incomplete firmware version and now the Launchpad wasn't working at all&mdash;neither in standalone mode nor with Bitwig.
There seemed to be no way back, so I chose the way forward and just tried installing again.
And this time it worked!
And with that, interaction with Bitwig also worked flawlessly.

**UPDATE**: mmntmtrnstn has in the meantime pointed out that Novation has a [similar website](https://components.novationmusic.com/launchpad-pro-mk3/firmware) where you can do an official firmware update.
I haven't tried Novation's firmware update and can't comment on it, but I'm confident that it will work too.
