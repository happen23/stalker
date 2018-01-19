# stalker
a photo image viewer which can traverse all sub-directories automatically.

## introduction
I have many photos imported from my digital cameras, which are scattered in date-named sub-directories like this:

```
canon/
|
----2009/
	|
	----04/
		|
		----2009-04-25/
			|
			----IMG_0239.jpg
```


One day I wantted to look back my good old days, I found all free image viewers which are available in windows desktop can't traverse the sub-directoried described above, so I decided to make a handy image [pre]viewer by myself.

I'm wrong, you can do the metioned operation in [FastStone Image Viewer](http://www.faststone.org/FSViewerDetail.htm), just do some setting:
1. Press F12, and the `Settings` dialog will show up
2. Select `Viewer` Tab (actually it's the default tab ;) )
3. check the `Auto Next Folder` cehckbox
4. Press `OK` and taht's Done

So, this repo has no reason to develop, **Goodbye**!

## usage

1. open toplevel photo directory
It is recommended to generate a exe file by [pyinstaller](www.pyinstaller.org), then right click the toplevel photo directory, choose that exe to open.
If you are a developer, you can run `python path/to/stalker.py path/to/images/`

2. browsering
Just click your mouse and the show goes.

## caution
Only Python3 is supported.

## misc

Developed and tested on windows10, but it is highly probable to running in other platforms.
