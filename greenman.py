#!/usr/bin/env python3


import os
import math
import time
# GREENMAN!

buzzwords = {".iso":"ISO_images",".py": "python_scripts", ".png": "images", ".jpg": "images",".webp": "images", ".gif": "gifs", ".ico":"icons", ".exe": "executables",".deb": "debian_packages",".zip": "ZIPs",".txt": "text_files",".tar.gz":"tarball_archives",".mov":"videos",".mp4":"videos",".mp3":"audio",".wav":"audio"}

def organize(path,only):
    if not os.path.isdir:
        print("target isn't a directory!")
    else:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        ventBuzzWords = {}
        vent = False
        do_not_execute = False
        if not only =="all":
            only = only.replace(" ","").split(",")
            for i in only:
                for u in buzzwords.keys():
                    if i == u:
                        ventBuzzWords[u] = buzzwords.get(u)
                    vent = True
            if vent == False:
                print(f"couldn't find only-item '{only}'")
                do_not_execute = True
        if not do_not_execute:
            if vent:
                loc = "current dir" if path =="." else path
                print("only organizing " + " , ".join(ventBuzzWords.keys()) + " files in " + loc + "...")
            elif path == ".":
                print("organizing current dir...")
            else:
                print(f"organizing {path}")
            curCyc = 0
            for i in files:
                curCyc += 1
                fileamt = len(files)
                calcCurCyc = curCyc *100/fileamt/10
                progress = math.floor(curCyc/len(files)*30)
                remainder = 30 - progress
                prprint=progress-1 if progress != 30 else progress
                Oprint = 1 if prprint != 30 else 0
                print(f"({curCyc}/{fileamt}) [{prprint*"=" + Oprint*"O"+remainder * "-"}]", end="\r")
                time.sleep(0.5/fileamt)
                finder = ventBuzzWords if vent else buzzwords
                for u in finder.keys():
                    if i.endswith(u):
                        selDir= finder.get(u)
                        os.makedirs(selDir, exist_ok=True)
                        os.rename(i,f"{path}/{selDir}/{i}")
                if os.access(f"{path}/{i}", os.X_OK):
                    os.makedirs("executables",exist_ok = True)
                    os.rename(i,f"{path}/executables/{i}")
            print()

            print("done!")

def unwrapunit(i,absopath):
    for x in [f for f in os.listdir(absopath + f"/{i}")]:
        if os.path.isdir(f"{absopath}/{i}/{x}"):
            unwrapunit(x,f"{absopath}/{i}")
            empty = True
            for _ in os.scandir(f"{absopath}/{i}/{x}"):
                empty = False
                break
            if empty:
                os.rmdir(f"{absopath}/{i}/{x}")
        elif os.path.isfile(f"{absopath}/{i}/{x}"):
            number=2
            fileExists = True if os.path.isfile(f"{absopath}/{x}") else False
            renamed = False
            while fileExists:
                renamed = True
                number += 1
                newname = f"{number}{x}"
                fileExists = True if os.path.isfile(f"{absopath}/{newname}") else False
            if renamed:
                os.rename(f"{absopath}/{i}/{x}",f"{absopath}/{newname}")
            else:
                os.rename(f"{absopath}/{i}/{x}",f"{absopath}/{x}")
    


def unwrap(path,only,deep,known):
    absopath = os.path.abspath(path)
    if not os.path.isdir(path):
        print("target isn't a directory!")
    else:
        dirs = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        ventBuzzWords = {}
        vent = False
        do_not_execute = False
        if not only =="all":
            only = only.replace(" ","").split(",")
            for i in only:
                for u in buzzwords.keys():
                    if i == u:
                        ventBuzzWords[u] = buzzwords.get(u)
                    vent = True
            if vent == False:
                print(f"couldn't find only-item '{only}'")
                do_not_execute = True
        if not do_not_execute:
            if vent:
                loc = "current dir" if path =="." else path
                print("only unwrapping " + " , ".join(ventBuzzWords.keys()) + " in " + loc + "...")
            elif path == ".":
                print("unwrapping current dir...")
            else:
                print(f"unwrapping {path}...")
            curCyc = 0
            for i in dirs:
                curCyc += 1
                diramt = len(dirs)
                calcCurCyc = curCyc *100/diramt/10
                progress = math.floor(curCyc/len(dirs)*30)
                remainder = 30 - progress
                prprint=progress-1 if progress != 30 else progress
                Oprint = 1 if prprint != 30 else 0
                print(f"({curCyc}/{diramt}) [{prprint*"=" + Oprint*"O"+remainder * "-"}]", end="\r")
                time.sleep(0.3 /diramt)
                finder = ventBuzzWords if vent else buzzwords
                for u in finder.keys():
                    if known or only != "all":
                        do = True if i == finder.get(u) else False
                    else:
                        do=True
                    if do:
                        if deep:
                            unwrapunit(i,absopath)
                        else:    
                            for x in [f for f in os.listdir(absopath + f"/{i}") if os.path.isfile(os.path.join(absopath+f"/{i}", f))]:
                                number=1
                                fileExists = True if os.path.isfile(f"{absopath}/{x}") else False
                                renamed=False
                                while fileExists:
                                    renamed=True
                                    number += 1
                                    newname = f"{number}{x}"
                                    fileExists = True if os.path.isfile(f"{absopath}/{x}") else False
                                if renamed:
                                    os.rename(f"{absopath}/{i}/{x}",f"{absopath}/{newname}")
                                else:
                                    os.rename(f"{absopath}/{i}/{x}",f"{absopath}/{x}")
                empty = True
                for _ in os.scandir(i):
                    empty = False
                    break
                if empty:
                    os.rmdir(i)
            print()    

            print("done!")