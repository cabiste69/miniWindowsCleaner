import os
import sys
import tempfile
from shutil import rmtree
from winshell import recycle_bin


sp = os.sep
emptyBin = False

def CreateConfigFile(path):
    print("creating config file in: "+path)
    # get windows' folder's path
    winpath = os.environ['WINDIR']
    x = [
            os.path.dirname(tempfile.mkdtemp()), # normal temporary folder (%temp%)
            winpath + sp + "Temp", # windows specific temp folder
            winpath + sp + "Downloaded Program Files",
            winpath + sp + "Prefetch",
            winpath + sp + "Offline Web Pages",
            "# " + winpath + ".old", # older version of windows
            "# recycleBin"
        ]

    with open(path,"w") as f:
        for row in x:
            f.write(row+"\n")

def ReadConfigFile():
    print("reading the config file")
    
    cfgPath = os.path.dirname(os.path.abspath(sys.executable)) + sp + "config.cfg"
    folders = []
    
    if not os.path.exists(cfgPath):
        CreateConfigFile(cfgPath)
        
    with open(cfgPath) as file:
        for line in file:
            line = line.strip()
            if not line.startswith("#"):
                if line == "recycleBin":
                    global emptyBin
                    emptyBin = True
                else:
                    folders.append(line)
    
    return folders


def DeleteTemps(folders):
    print("trying to delete "+ str(len(folders))+ " folders")
    for folder in folders:
        if not os.path.isdir(folder):
            continue
        
        print("\n--------deleting: "+ folder+"--------")
        
        print("Deleting files...")
        # ... delete every file in the folder
        for root, dirs, files in os.walk(folder):
            for file in files:
                # so it doesn't delete the desktop by mistake :)
                if file == "desktop.ini":
                    continue
                
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(str(e))

        print("Deleting folders..")
        # delete every subfolder in the folder
        for file in os.listdir(folder):
            if os.path.isdir(folder + sp + file):
                try:
                    rmtree(folder + sp + file)
                except Exception as e:
                    print(str(e))
    
    # finally empty recycle bin if specified
    if emptyBin:
        print("trying to empty recycle bin")
        try:
            recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        except Exception as e:
            print(str(e))

# i have it so it deletes the files then then folders individually because windows sometimes doesn't allow you
# to delete folders with files in them but if you delete those files individually you can then delete the folder (yes windows is damn weird)


if __name__ == "__main__":
    foldersToDelete = ReadConfigFile()
    DeleteTemps(foldersToDelete)
