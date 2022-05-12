import tempfile
import os

# get the temp folder's path
temppath = tempfile.mkdtemp()

# ... delete every file in the temp folder
for root, dirs, files in os.walk(os.path.dirname(temppath)):
    for file in files:
        try:
            os.remove(os.path.join(root, file))
        except Exception as e:
            print(str(e))

# ... delete every folder in the temp folder
for root, dirs, files in os.walk(os.path.dirname(temppath)):
    for dir in dirs:
        try:
            os.remove(root)
        except Exception as e:
            print(str(e))

# i have it so it delete files then folders individually because windows sometimes doesn't allow you
# to delete folders with files in them but if you delete those files individually you can then delete the folder (yes windows is damn weird)