#!/usr/bin/env python3

from greenmancore import *
import argparse

# GREENMAN!

#TODO help documentation!!!!

helpDict = {"me":"Here's some general tips & tricks for using greenman.\n\nNOTE: to see further help entries, type 'greenman help list'\n\nthe base components to use greenman are the ORGANIZE and UNWRAP functions.\n\nto receive further information on each, type 'greenman help organize' or 'greenman help unwrap'\n\nLove, greenman","help": "you seriously need help with the help command?",
"organize": "this command organizes files within the directory that you link afterwards \n\naliases:\norganize / o \n\nargs: \n-p / --path - the path to the dir you want organized. Defaults to current dir.\n\n-o / --only - used to filter for filetypes that you want organized. List the filetypes that you want organized after the path. make sure to seperate with commas. \n\nexamples:\ngreenman o   - organizes everything in current dir\ngreenman o .txt,.py   - only organizes python and text files in current dir \ngreenman o -p /home/user/Downloads   - organizes the downloads folder."}
helpAliases = {"o": "organize"}
def GmanHelp(command):
    if command in helpDict.keys():
        print(helpDict.get(command))
    elif command == "list":
        print("list of help items:\n-------------------")
        for i in helpDict.keys():
            print(i)
        print("-------------------\nuse - 'greenman help (item)' - to open it's help entry")
    elif command in helpAliases.keys():
        print(helpDict.get(helpAliases.get(command)))
    else:
        print("unknown command")

def knownlist():
    for i,u in buzzwords.items():
        print(f"{i} -> {u}")


parser = argparse.ArgumentParser(prog='greenman')
subparsers = parser.add_subparsers(dest='command', required=True)

p = subparsers.add_parser('organize', aliases=['o'], help='Organize a directory')
p.add_argument("-p", "--path", type=str, default=".",help="the path to the dir you want organized. Default is your current dir")
p.add_argument("-o", "--only",type=str,default="all",help="'only' is used if you want to only organize certain files.")
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

p=subparsers.add_parser("knownlist", aliases = ["kl","klist"],help="list all entries to the known list. important for 'greenman u -k'.")
p.set_defaults(func = knownlist)
args = parser.parse_args()

commands = {"organize": ["path","only"],"o": ["path","only"],"help": "item","unwrap":["path","only","deep","known","onlydir"],"u":["path","only","deep","known","onlydir"],"kl":None}
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


#test
