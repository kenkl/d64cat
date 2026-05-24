# d64cat

## Story time...

In the mid-late 80's, I was a Commodore 64 enthusiast, playing games, exploring productivity, haunting BBSs, etc. - all the things we did in the heady days at the beginning of the "personal computing revolution". Along the way, I did make contacts that yielded many "greyware" copies of software that I could not, as a teenager, easily afford. 

At the time, I'd developed a cataloguing scheme to organize my collection, as well as to make writing those little labels on diskettes. So, instead of having to wrestle with my shitty handwriting to fit 'Epyx Winter Games' on the label, I concocted a cataloging scheme where that would become something like 'F023' - a 'full' game, 23rd disc in the sequence/collection. As my collection grew, I branched out, creating categories for Cracks ('C0xx'), Utilities ('U0xx'), Applications ('A0xx'), and so on.

Being a "genius", I kept a "secret decoder ring" of the collection in a three-ring binder so I could "easily" pick a title for an afternoon's play session, locate the diskette, and go. This was, of course, quite a few years before hard-drives became A Thing™ in my environment, not that the C64 could easily deal with them when they did arrive.

Anyway, somewhere along the way/years, the blue three-ring binder I used for this task disappeared, likely a casualty of moving house at some point. Somehow, the collection of diskettes survived, and I came across them in 2013 or thereabouts, and spent a few weeks imaging them to .d64 files for use in emulators if I fancied, to relive the "good ol' days" of a simpler, more innocent time.

Of course, having lost the blue notebook, I'd no idea what disc was what, so I simply labeled the images with whatever was written on the label. I imagined using the emulator to mount the disc, figure out what's there, and reconstruct my "secret decoder ring" by hand. I discovered pretty quickly that that was going to be a tedious, time-consuming slog, and I just couldn't be arsed to deal with the task. 

Skip forward to present day... [EmulationStation](https://emulationstation.org/) is a solid way to run retro games on [Steam Deck](https://store.steampowered.com/steamdeck), presenting a good reason to unwind/decode/catalog my collection, to pick a handful of titles that I could play there. But, the manual slog of cataloging them by hand is still a barrier/roadblock.

## Enter "AI"

A number of my coworkers have been seduced by "AI" tools to build code, and frequently proselytize the wonders of using Grok, Gemini, Ollama, etc. for letting them, as non-coders, craft interesting/useful things. Feeling a lack of inspiration, one of them advised identifying "pain points" as a thing to point the various tools at to construct things that would lessen the pain. Slogging through a few hundred megs of .d64 files qualifies, I think.

I know Python well enough, maybe I could get one of the engines to give me a starting-point for this project. Asking Gemma4 (running in Ollama locally), I asked "can we construct a Python script to retrieve the directory/contents of .d64 (for Commodore 64/128) disc images?" After a couple minutes, it spat out some primitives (primitives.py) that gave me a starting point for decoding the directories on the .d64 files I've had hanging around for over a decade.

While I have a general distrust/distaste for "AI" tools, I do feel the appeal of becoming a Doctorow-esque [centaur](https://pluralistic.net/2025/05/27/rancid-vibe-coding/#class-war) - solving a decades-old problem of my own making.

So yes - while parts of this little project are "vibe coded", I admit it, much of it won't need to be. 

## Goals

Having played with the primitives.py a little with a handful of .d64 files to sanity-check what Gemma4 turned up, I'm imagining/aspiring a few things that I could do here:

1. iterate through all the files in a given directory to extract the directory contents
2. make a guess at the theme/content of the volume, based on filenames revealed by read_d64_directory()
3. collect the guess (and complete output) in a searchable corpus - a database of some description
4. add logic to deal with .d81 images - I have a few that the current primitives.py doesn't know what to do with

Although I wouldn't expect to get a C&D for sharing .d64/.d81 files here, I'm not gonna take the chance; disc images will _not_ be included in this repo.

## Changelog things

Although a separate changelog is probably a good idea if/when I spend a bunch of time with this, I'm happy to tack things here for now.

2026-05-17@1238 - I updated the pylsecrets_sample.py to include value/key pairs as a "just in case" thing for myself. Unlikely that this thing will ever send emails, but it's a simple copypasta from [lights](https://github.com/kenkl/lights) and [certcheckweb](https://github.com/kenkl/certcheckweb) versions; I'll clean this up later.

2026-05-22@2034 - I added buildlist.py to grind through a directory structure, parsing all the .d64 files found there, and spitting the contents into a .csv file. It occurred to me that a database was probably overkill; this list will be static. I'd briefly thought about using openpyxl to natively create an .xlsx, but realised - I really only need a .csv to do what I'm after here, so.

Anyway, that was easy enough to put together (see build_csv()) some bits to do just that, but after grinding through a couple dozen .d64 files, my code breaks during parsing file_type (line 59) with an IndexError exception. Probably will put things in try/except block(s) to fail a little more... gracefully.
