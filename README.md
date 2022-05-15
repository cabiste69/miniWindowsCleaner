# miniWindowsCleaner
This is a small script that cleans windows from useless files (temp folders)

# intent 
Obviously this app sounds stupid, "huh? it just deletes the temp folders? i can do that manually"  
Well yeah that's correct but this app will save you a bit of time so why not ¯\\\_(ツ)\_/¯  
The app is meant to run once one you turn on your machine, clean it then you never see it again

# how to use
Download the latest release from here https://github.com/cabiste69/miniWindowsCleaner/releases/latest

Then make a shortcut of the app and place it in the windows startup folder `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`

That way it will run when the pc turns on

# how to build

1. Install the dependencies 
   - `pip install winshell`
   - `pip install pypiwin32`

2. Run `python app.py`

# how to Compile

1. Install pyinstaller `pip install pyinstaller`
2. Compile the source code `pyinstaller -F app.py`
   - `-F` so it compiles everything into 1 single file

This should give you an exe that you'll find in `dist/app.exe`,  
Copy that app to another folder so you don't forget about it just in case

# known issues 
None :)

# FAQ
Q: Does this app just move the files to the recycle bin and i have to manually empty it?

A: Nope, it deletes them completely :)

---

Q: Is it a virus?

A: no :(, you can read the code yourself in `app.py` it's less than 100 lines of code

---

Q: Why is the file size so large? (10Mb)

A: idk, i'm using pyinstaller and upx `pyinstaller -F --onefile --upx-dir=upx-3.96-win64/ app.py`, if you know how to do it better then please create an issue

---

Q: What folders are deleted exactly?

A: It deletes the windows temp folders that are known to be safe:
   - C:\Users\comp\AppData\Local\Temp
   - C:\Windows\Temp
   - C:\Windows\Downloaded Program Files
   - C:\Windows\Prefetch
   - C:\Windows\Offline Web Pages
   - C:\Windows.old (disabled by default)
   - recycle bin (disabled by default)

  *The app will creat a config file in the folder you place it in*  
  *You can enable/disable the folders to be deleted by adding a `#` before them*  
  *You can add your own folders by just typing them in a new line*  