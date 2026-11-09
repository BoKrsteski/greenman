#!/usr/bin/env python3


import os
import math
import time
# GREENMAN!

#TODO add theme search (e.g. "coolstuff": coolstuff.txt,coolstuff.py etc will be put into /coolstuff/ )

buzzwords = {".iso":"ISO_images",".py": "python_scripts", ".png": "images", ".jpg": "images",".webp": "images", ".gif": "gifs", ".ico":"icons", ".exe": "executables",".deb": "debian_packages",".zip": "ZIPs",".txt": "text_files",".tar.gz":"tarball_archives",".mov":"videos",".mp4":"videos",".mp3":"audio",".wav":"audio"}

def organize(path,only):
    if not os.path.isdir(path):
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
                        os.makedirs(os.path.join(path,selDir), exist_ok=True)
                        os.rename(os.path.join(path,i), os.path.join(path,selDir,i))
                        break
                else:
                    if os.access(os.path.join(path,i), os.X_OK):
                        os.makedirs(os.path.join(path,"executables"),exist_ok = True)
                        os.rename(os.path.join(path,i),os.path.join(path,"executables",i))
            print()

            print("done!")

def unwrapunit(i,absopath):
    for x in [f for f in os.listdir(os.path.join(absopath,i))]:
        aix = os.path.join(absopath,i,x)
        if os.path.isdir(aix):
            unwrapunit(x,os.path.join(absopath,i))
            empty = True
            for _ in os.scandir(aix):
                empty = False
                break
            if empty:
                os.rmdir(aix)
        elif os.path.isfile(aix):
            number=2
            fileExists = True if os.path.isfile(os.path.join(absopath,x)) else False
            renamed = False
            while fileExists:
                renamed = True
                number += 1
                newname = f"{number}{x}"
                fileExists = True if os.path.isfile(os.path.join(absopath,newname)) else False
            if renamed:
                os.rename(aix,os.path.join(absopath,newname))
            else:
                os.rename(aix,os.path.join(absopath,x))
    


def unwrap(path,only,deep,known,onlydir):
    absopath = os.path.abspath(path)
    do_not_execute = False
    if not os.path.isdir(path):
        print("FATAL: target isn't a directory!")
    else:
        firstOnlydir=onlydir.replace("/","").split(",")
        onlydir =onlydir.split(",")
        dirs = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))] if onlydir[0] == "all" and len(onlydir) == 1 else [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and f in firstOnlydir]
        if not set(dirs) == set(onlydir) and len(onlydir) > len(dirs):
            diff = [x for x in onlydir if x not in dirs]
            print(f"WARNING: unresolved dirnames: '{",".join(diff)}' not found!\nContinuing with existing ones...")
        s = "s" if len(onlydir) > 1 else ""
        if len(dirs) == 0:
            print(f"FATAL: No dirs by the name{s} '{",".join(onlydir)}' were found.")
            do_not_execute = True
        ventBuzzWords = {}
        vent = False
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
            elif onlydir[0] != "all":
                print(f"only unwrapping the '{",".join(onlydir)}' dir{s}...")
            elif path == ".":
                print("unwrapping current dir...")
            else:
                print(f"unwrapping {path}...")
            curCyc = 0
            for i in dirs:
                curCyc += 1
                diramt = len(dirs)
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
                            for x in [f for f in os.listdir(os.path.join(absopath,i)) if os.path.isfile(os.path.join(absopath,i, f))]:
                                aix = os.path.join(absopath,i,x)
                                number=1
                                fileExists = True if os.path.isfile(os.path.join(absopath,x)) else False
                                renamed=False
                                while fileExists:
                                    renamed=True
                                    number += 1
                                    newname = f"{number}{x}"
                                    fileExists = True if os.path.isfile(os.path.join(absopath,newname)) else False
                                if renamed:
                                    os.rename(aix,os.path.join(absopath,newname))
                                else:
                                    os.rename(aix,os.path.join(absopath,x))
                empty = True
                for _ in os.scandir(os.path.join(absopath,i)):
                    empty = False
                    break
                if empty:
                    os.rmdir(os.path.join(absopath,i))
            print()    

            print("done!")