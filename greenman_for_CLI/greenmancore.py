#!/usr/bin/env python3


import os
import math
import time
from pathlib import Path
# GREENMAN!

GREEN = "\033[32m"
RESET = "\033[0m"
RED="\033[31m"
YELLOW= "\033[93m"
BLUE="\033[94m"
GRAY = "\033[38;5;244m"
SUBTLEGRAY = "\033[38;5;251m"

buzzwords = {
".png": "images",
".jpg":"images" ,
".webp": "images",
".bmp":"images",
".tiff": "images",
".tif": "images",
".heic": "images",
".heif": "images",
".avif": "images",
".jxl": "images",
".psd": "images",
".svg": "vector_images",
".ico": "icons",
".gif": "gifs",

".mov": "videos",
".mp4": "videos",
".webm": "videos",
".mkv": "videos",
".avi":"videos",
".flv":"videos",
".wmv": "videos",
".m4v":"videos",


".mp3": "audio",
".wav":"audio",
".flac": "audio",
".ogg":"audio",
".m4a":"audio",
".aac": "audio",
".opus":"audio",
".aiff":"audio",


".zip": "ZIPs",
".tar.gz": "tarball_archives",
".tar": "tarball_archives",
".7z":"archives",
".rar":"archives",
".gz":"gzip_archives",
".bz2": "bzip2_archives",
".xz": "xz_archives",
".zst":"zstd_archives",


".exe":"executables",
".msi":"windows_installers",
".apk":"android_packages",
".deb":"debian_packages",
".rpm":"rpm_packages",
".appimage": "linux_appimages",
".dmg": "macos_disk_images",
".pkg":"macos_packages",


".pdf": "pdf_documents",
".docx":"word_documents",
".xlsx":"spreadsheet_files",
".pptx":"presentation_files",
".epub": "ebook_files",
".rtf":"rtf_documents",
".txt":"text_files",
".md": "markdown_files",


".py":"python_scripts",
".sh":"shell_scripts",
".js": "javascript_files",
".ts": "javascript_files",
".html":"web_files",
".css":"web_files",
".java":"source_code",
".cpp": "source_code",
".c":"source_code",

".json": "config_files",
".yaml":"config_files",
".yml":"config_files",
".xml":"config_files",
".csv": "data_files",
".tsv":"data_files",
".sqlite": "database_files",


".ttf": "font_files",
".otf":"font_files",
".woff": "font_files",
".woff2":"font_files",


".iso": "ISO_images",
".vhd":"virtual_disk_images",
".vmdk":"virtual_disk_images",
".qcow2":"virtual_disk_images",
}   

def organize(path,only,OneDir,keyword,strictName):
    if not os.path.isdir(path):
        print(RED+"FATAL:"+RESET+" target isn't a directory!")
    else:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        ventBuzzWords = {}
        vent = False
        do_not_execute = False
        if len(files) == 0:
            print(RED+"FATAL:"+RESET+" No files in target directory!")
            do_not_execute = True
        if not only =="all":
            only = only.replace(" ","").split(",")
            for i in only:
                for u in buzzwords.keys():
                    if i == u:
                        ventBuzzWords[u] = buzzwords.get(u)
                    vent = True
            if vent == False:
                print(YELLOW+"WARNING:"+RESET+" couldn't find only-item "+BLUE+f"'{only}'"+RESET)
                do_not_execute = True
        if not do_not_execute:
            loc = "current dir" if path =="." else path
            if vent:
                print("only organizing " + BLUE+ " , ".join(ventBuzzWords.keys()) + RESET+f" files {"including "+BLUE+f"'{keyword}' "+RESET if keyword != "nil" else ""}{f"named "+BLUE+f"'{strictName}' "+RESET if strictName != "nil" else ""}in " +BLUE+ loc + RESET+"...")
            else:
                print(f"organizing files {f"including "+BLUE+f"'{keyword}' "+RESET if keyword != "nil" else ""}{"named "+BLUE+f"'{strictName}' "+RESET if strictName != "nil" else ""}in "+BLUE+f"{loc}"+RESET+"...")
            curCyc = 0
            for i in files:
                curCyc += 1
                fileamt = len(files)
                progress = math.floor(curCyc/len(files)*30)
                remainder = 30 - progress
                prprint=progress-1 if progress != 30 else progress
                Oprint = 1 if prprint != 30 else 0
                print(f"({BLUE}{curCyc}{RESET}/{BLUE}{fileamt}{RESET}) [{GREEN}{prprint*'='}{Oprint*'O'}{GRAY}{remainder*'-'}{RESET}]", end="\r")
                time.sleep(0.5/fileamt)
                finder = ventBuzzWords if vent else buzzwords
                onedirisFalse = False if OneDir != "off" else True
                if not vent and keyword!= "nil" or not vent and strictName != "nil":
                    if keyword!= "nil" and keyword in i:
                        os.makedirs(os.path.join(path,keyword
                    ), exist_ok=True)
                        os.rename(os.path.join(path,i), os.path.join(path,keyword
                    ,i))
                    elif Path(i).stem == strictName:
                        os.makedirs(os.path.join(path,strictName), exist_ok=True)
                        os.rename(os.path.join(path,i), os.path.join(path,strictName,i))
                else:
                    for u in finder.keys():
                        if i.endswith(u):
                            if keyword != "nil" and keyword in i:
                                os.makedirs(os.path.join(path,keyword
                            ), exist_ok=True)
                                os.rename(os.path.join(path,i), os.path.join(path,keyword
                            ,i))
                            elif Path(i).stem == strictName:
                                os.makedirs(os.path.join(path,strictName), exist_ok=True)
                                os.rename(os.path.join(path,i), os.path.join(path,strictName,i))
                            elif onedirisFalse:
                                selDir= finder.get(u)
                                os.makedirs(os.path.join(path,selDir), exist_ok=True)
                                os.rename(os.path.join(path,i), os.path.join(path,selDir,i))
                                break
                            else:
                                os.makedirs(os.path.join(path,OneDir), exist_ok=True)
                                os.rename(os.path.join(path,i), os.path.join(path,OneDir,i))
                                break
                    else:
                        if not onedirisFalse:
                            os.makedirs(os.path.join(path,OneDir), exist_ok=True)
                            os.rename(os.path.join(path,i), os.path.join(path,OneDir,i))
                        elif os.access(os.path.join(path,i), os.X_OK):
                            carryOn = True
                            for a in buzzwords.keys():
                                if i.endswith(a):
                                    carryOn = False
                                    break
                            if carryOn:
                                os.makedirs(os.path.join(path,"executables"),exist_ok = True)
                                os.rename(os.path.join(path,i),os.path.join(path,"executables",i))
            print()

            print(GREEN+"done!"+RESET)

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
        print(RED+"FATAL:"+RESET+" target isn't a directory!")
    else:
        firstOnlydir=onlydir.replace("/","").split(",")
        onlydir =onlydir.split(",")
        dirs = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))] if onlydir[0] == "all" and len(onlydir) == 1 else [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and f in firstOnlydir]
        if onlydir[0] != "all" and not set(dirs) == set(onlydir) and len(onlydir) > len(dirs):
            diff = [x for x in onlydir if x not in dirs]
            print(YELLOW+f"WARNING:"+RESET+" unresolved dirnames: '{",".join(diff)}' not found!\nContinuing with existing ones...")
        s = "s" if len(onlydir) > 1 else ""
        if len(dirs) == 0:
            if onlydir[0] == "all":
                print(RED+"FATAL:"+RESET+" No directories found to unwrap.")
            else:
                print(RED+f"FATAL:"+RESET+" No dirs by the name{s} '{",".join(onlydir)}' were found.")
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
                print(YELLOW+"WARNING: "+RESET+f"couldn't find only-item '{only}'")
                do_not_execute = True
        if not do_not_execute:
            loc = "current dir" if path =="." else path
            if vent:
                print("only unwrapping " + BLUE+" , ".join(ventBuzzWords.keys()) +RESET+ " in " +BLUE+ loc +RESET+ "...")
            elif onlydir[0] != "all":
                print(f"only unwrapping the '{BLUE+",".join(onlydir)+RESET}' dir{s}...")
            elif known:
                print("only unwrapping known dirs in " + BLUE+loc +RESET+"...")
            else:
                print(f"unwrapping {BLUE+loc+RESET}...")
            curCyc = 0
            for i in dirs:
                curCyc += 1
                diramt = len(dirs)
                progress = math.floor(curCyc/len(dirs)*30)
                remainder = 30 - progress
                prprint=progress-1 if progress != 30 else progress
                Oprint = 1 if prprint != 30 else 0
                print(f"({BLUE}{curCyc}{RESET}/{BLUE}{diramt}{RESET}) [{GREEN}{prprint*'='}{Oprint*'O'}{GRAY}{remainder*'-'}{RESET}]", end="\r")
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
                for z in finder.keys():
                    if known or only != "all":
                        do = True if i == finder.get(z) else False
                    else:
                        do = True
                    if do:
                        if os.path.exists(os.path.join(absopath,i)):
                            empty = True
                            for _ in os.scandir(os.path.join(absopath,i)):
                                empty = False
                                break
                            if empty:
                                os.rmdir(os.path.join(absopath,i))
            print()    

            print(GREEN+"done!"+RESET)

#test