# miniWindowsCleaner
this is a small script that cleans windows from useless files (temp folders)

# how to use
download the latest release from here https://github.com/cabiste69/miniWindowsCleaner/releases/latest

then make a shortcut of the app and place it in the windows startup folder `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`

that way it will run when the pc turns on

# intent 
obviously this app sounds stupid "huh? it just deletes the temp folder? i can do that manually"
well yeah but it will save you a bit of time so why not ¯\\_(ツ)_/¯
the app is meant to run once one you turn on your machine, clean it then you never see it again

# how to build

1. Install pyinstaller `pip install pyinstaller`
2. compile the source code `pyinstaller -F app.py`
   - `-F` so it compiles everything into 1 single file

this should give you an exe that you'll find in `dist/app.exe`
copy that app to another folder so you don't forget about it just in case

# known issues 
none :)

# FAQ
Q: does this just moves the files to the bin and i have to manually empty it?

A: nope, it deletes it immediately :)

Q: is a virus?

A: no :(, you can read the code yourself in `app.py` literally 20 lines of code

Q: what folders are deleted exactly?

A: as of right now it only deletes the normal temp folder (`C:\Users\comp\AppData\Local\Temp`), but i'll be adding these other folders in the near future
   - C:\Windows\Temp
   - C:\Windows.old
   - C:\Windows\Downloaded Program Files
   - C:\Windows\Prefetch
   - C:\Windows\Offline Web Pages
   - recycle bin

  *I'll also make a config file where you can choose which folders to be deleted easily*