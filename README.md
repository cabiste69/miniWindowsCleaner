# miniWindowsCleaner
this is a small scripts that cleans windows from useless files (temp folder)

# how to use
download the code and run `app.py`
you don't need to download any modules 

# intent 
obviously this app sounds stupid "huh? it just deletes the temp folder? i can do that manually"
well yeah but it's meant to run once one you turn on your machine, clean it then you never see it again
and for that you need to build it

# how to build

1. Install pyinstaller `pip install pyinstaller`
2. compile it `pyinstaller -F app.py`

this should give you an exe that you'll find in `dist/app.exe`
copy that app to another folder so you don't forget about it just in case

# how to make it run on windows start
it's actually very simple 

1. make a shortcut for the app
2. then go to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
   - *if you don't have the `StartUp` folder then just create it*
3. paste the shortcut in there

# known issues 
some folders in the temp folder require admin level to delete them and so you can just give admin perm to this app
1. right click on the exe 
2. click *properties*
3. go to the *compatibility* tab
4. check "Run this program as an administrator* and click ok
done

# FAQ
Q: does this just moves the files to the bin and i have to manually empty it?
A: nope, it deletes it immediately :)

Q: is a virus?
A: no :(, you can read the code yourself in `app.py` literally 20 lines of code