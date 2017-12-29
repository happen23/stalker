# stalker
a photo image viewer which can automatically traverse all sub-directories

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


One day I wantted to look back my good old days, I found all free image viewers which are available in windows desktop can't traverse the sub-directoried described above, so I decided DIY a handy image [pre]viewer. 

## usage

### open toplevel photo directory
It is recommended to generate a exe file by [pyinstaller](www.pyinstaller.org), then right click the toplevel photo directory, choose that exe to open.
If you are a developer, you can run `python path/to/stalker.py path/to/images/`

### browsering
Just click you mouse and the show goes.

## caution
Only Python3 is supported

## misc

Developed and tested in windows, but it is highly probable to running in other platforms
