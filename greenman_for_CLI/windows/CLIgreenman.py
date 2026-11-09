#!/usr/bin/env python3

from greenmancore import *
import argparse

# GREENMAN!

helpDict = {"help": "you seriously need help with the help command?",
"organize": "this command organizes files within the directory that you link afterwards \n\naliases:\n organize / o \n\nargs: \n-p / --path - the path to the dir you want organized. Defaults to current dir.\n\n-o / --only - used to filter for filetypes that you want organized. List the filetypes that you want organized after the path. make sure to seperate with commas. \n\nexamples:\ngreenman o   - organizes everything in current dir\ngreenman o .txt,.py   - only organizes python and text files in current dir \ngreenman o -p /home/user/Downloads   - organizes the downloads folder."}
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
p.set_defaults(func=unwrap)

args = parser.parse_args()

commands = {"organize": ["path","only"],"o": ["path","only"],"help": "item","unwrap":["path","only","deep","known"],"u":["path","only","deep","known"]}
if args.command in commands.keys():
    commandContents = commands.get(args.command)
    if isinstance(commandContents, list):
        paramlist=[]
        for i in commandContents:
            paramlist.append(getattr(args,i,"nope"))
        params=tuple(paramlist)
    else: 
        params = ((getattr(args,commands.get(args.command), "nope")),)
    args.func(*params)