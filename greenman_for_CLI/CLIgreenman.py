#!/usr/bin/env python3

VERSION = "DevModeVersion"

from greenmancore import *
import argparse

# GREENMAN!

#TODO help documentation!!!!
#TODO colorize outputs!

helpDict = {"me":"Here's some general tips & tricks for using greenman.\n\nNOTE: to see further help entries, type 'greenman help list'\n\nthe base components to use greenman are the ORGANIZE and UNWRAP functions.\nto receive further information on each, type 'greenman help organize' or 'greenman help unwrap'\n\nThe order of arguments does not matter!\n'greenman u -d -p /here' will have the same effect as 'greenman u -p /here -d'.\n\nLove, greenman!","help": "getting help for the help command is crazy...\n\nAnyway, use 'greenman help' followed by a command to receive help for it\nDo 'greenman help list' to list all comands you can get help with.",
"organize": "this command organizes files within the directory that you link afterwards \n\nALIASES:\norganize / o \n\nARGS: \n-p / --path :\nthe path to the dir you want organized. Defaults to current dir.\n\n-o / --only :\nused to filter for filetypes that you want organized. make sure to seperate with commas. \n\n--onedir :\nused to move all files in a directory into a singular further directory. Naming it is imperative.\nExample: greenman o --onedir everything   - Here, the name would be 'everything'\n\nEXAMPLES:\ngreenman o   - organizes everything in current dir\ngreenman o .txt,.py   - only organizes python and text files in current dir \ngreenman o -p /home/user/Downloads   - organizes the downloads folder.",
"unwrap": "this command unwraps files from all Directories inside the target, meaning that it will return all files from further Directories back into the target. \n\nALIASES:\nunwrap / u\n\nargs:\n-p / --path :\nthe path to the dir you want unwrapped. Defaults to current dir.\n\n-o / --only :\nused to filter for filetypes that you want unwrapped. make sure to seperate with commas.\n\n-d / --deep :\nUsed to unwrap all directories within your target recursively. if you set your target to '/target', greenman won't naturally search further than 2 layers, so '/target/stuff/morestuff' would get ignored. -d avoids this by searching everything recursively.\n\n-k / --known :\nThis command is used to filter the unwrapping process so it only includes directories that greenman created itself, So to say directly reverting the organize function without unwrpaping anything else.\nNOTE: It is recommended to use the knownlist to see if any of your unwanted firectories will be affected. Display it using 'greenman kl'.\n\n-d / --onlyDir :\nOnly unwraps directories that are named after this argument.\nExample: 'greenman u -D stuff,morestuff'. This would only unwrap the 'stuff' and 'morestuff' directories.\nMake sure to seperate with commas.\n\nEXAMPLES:\ngreenman u   - unwraps current directory.\ngreenman u -p /path/to/stuff   - unwraps the '/path/to/stuff' directory\ngreenman u -d   - will recursively unwrap all directories in current dir.\ngreenman u -k   - will only unwrap known directories in current directory.\ngreenman u -D stuff,otherstuff,morestuff   - will only unwrap the 'stuff', 'otherstuff' and 'morestuff' Directories in current Directory."}

#unit: "item": "(infotext)\n\nALIASES:\n(aliases)\n\nARGS:\n(args)\n\nEXAMPLES:\n(example)   - (explanation)"

helpAliases = {"o": "organize","u":"unwrap"}
def GmanHelp(command):
    if command in helpDict.keys():
        print(helpDict.get(command))
    elif command == "list":
        print("list of help items:\n-------------------")
        for i in helpDict.keys():
            print(i)
        print("-------------------\nuse - 'greenman help (item)' - to open its help entry")
    elif command in helpAliases.keys():
        print(helpDict.get(helpAliases.get(command)))
    else:
        print("unknown command")

def knownlist():
    for i,u in buzzwords.items():
        print(f"{i} -> {u}")

def smile():
    print("\033[32m"+r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠛⠛⠋⠉⠛⠛⠷⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⣴⣶⡆⠀⠀⠀⠀⢠⣶⣦⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀
⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠛⠟⠃⠀⠀⠀⠀⠘⠻⠛⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⠘⣿⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⣿⠇⠀⠀⠀
⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠙⢷⣦⣀⡀⠀⣀⣠⡾⠋⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀⠀⠀⠈⠉⠙⠋⠉⠉⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢶⣤⣄⣀⣀⣀⣀⣠⣤⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀
"""+"\033[0m")

def ver(Isinit):
    if Isinit:
        print("Installing greenman...")
        print("\033[32m"+r"""
 ██████╗ ██████╗ ███████╗███████╗███╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║████╗ ████║██╔══██╗████╗  ██║
██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║██╔████╔██║███████║██╔██╗ ██║
██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║██║╚██╔╝██║██╔══██║██║╚██╗██║
╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║██║ ╚═╝ ██║██║  ██║██║ ╚████║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """+"\033[0m")
        print("Greenman successfully installed!")
    print("Greenman is at " + VERSION)


parser = argparse.ArgumentParser(prog='greenman')
subparsers = parser.add_subparsers(dest='command', required=True)

p = subparsers.add_parser('organize', aliases=['o'], help='Organize a directory')
p.add_argument("-p", "--path", type=str, default=".",help="the path to the dir you want organized. Default is your current dir")
p.add_argument("-o", "--only",type=str,default="all",help="'only' is used if you want to only organize certain files by filetype/extension.")
p.add_argument("--onedir", type=str,default="off",help="puts all files in only one directory. Set the directory's name right after the argument.")
p.add_argument("-k", "--keyword",type=str,default="nil",help="'keyword' is used if you want to only organize certain files by name. This searches if the name INCLUDES the given string.")
p.add_argument("-n", "--name",type=str,default="nil",help="'name' is used if you want to only organize certain files by name. This searches if the name IS the given string. If it's any different, It'll be ignored.")
p.set_defaults(func=organize)

p=subparsers.add_parser("help", help="better way of receiving help. follow up by command you need help with")
p.add_argument("item", nargs="?",default="me",help="the command you need help with.")
p.set_defaults(func=GmanHelp)

p=subparsers.add_parser("unwrap",aliases=["u"], help="unwrap organized files back to their original state.")
p.add_argument("-p", "--path", type=str, default=".",help="the path to the directory that will be unwrapped")
p.add_argument("-o","--only",type=str,default="all",help="'only' is used if you want to only unwrap certain files.")
p.add_argument("-d","--deep", action="store_true")
p.add_argument("-k","--known", action="store_true")
p.add_argument("-D","--onlydir",type=str,default="all",help="only unwraps dirs mentioned in here")
p.set_defaults(func=unwrap)

p=subparsers.add_parser("version", aliases = ["v","ver"],help="displays current version")
p.add_argument("--init", action="store_true")
p.set_defaults(func = ver)

p=subparsers.add_parser("knownlist", aliases = ["kl","klist"],help="list all entries to the known list. important for 'greenman u -k'.")
p.set_defaults(func = knownlist)

p=subparsers.add_parser("smile",help="let greenman smile at you :)")
p.set_defaults(func = smile)

args = parser.parse_args()

commands = {"organize": ["path","only","onedir","keyword","name"],"o": ["path","only","onedir","keyword","name"],"help": "item","unwrap":["path","only","deep","known","onlydir"],"u":["path","only","deep","known","onlydir"],"kl":None,
"v": "init","ver": "init","version":"init","smile":None}
if args.command in commands.keys():
    commandContents = commands.get(args.command)
    params = False
    if isinstance(commandContents, list):
        paramlist=[]
        for i in commandContents:
            paramlist.append(getattr(args,i,"nope"))
        params=tuple(paramlist)
    else:
        if commandContents is not None:
            params = ((getattr(args,commandContents, "nope")),)
    if params:
        args.func(*params)
    else:
        args.func()

