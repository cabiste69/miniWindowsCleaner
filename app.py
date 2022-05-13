import tempfile
import os
import shutil

# get the temp folder's path
temppath = tempfile.mkdtemp()
temppath = os.path.dirname(temppath)

print("-----Deleting files-----")
# ... delete every file in the temp folder
for root, dirs, files in os.walk(temppath):
    for file in files:
        try:
            os.remove(os.path.join(root, file))
        except Exception as e:
            print(str(e))

print("-----Deleting folders-----")
# ... delete every folder in the temp folder
for folder in os.listdir(temppath):
    if os.path.isdir(temppath + os.sep +folder):
        try:
            shutil.rmtree(temppath + os.sep + folder)
        except Exception as e:
            print(str(e))

# i have it so it delete files then folders individually because windows sometimes doesn't allow you
# to delete folders with files in them but if you delete those files individually you can then delete the folder (yes windows is damn weird)
