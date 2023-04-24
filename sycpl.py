#!/usr/bin/python
from colors import *
import interp
import sys
import pprint 

args = sys.argv
default_text = """usage: sycpl [file] [option] [-h | --help]

Options:
    -h      |  --help       Shows this menu 
    -c  -i  |  --interpret  Runs the specified file
"""

def PrintError(name="Program Error", err="NULL", extra="-"):
    return f"""{BOLD}{name}: {extra}
    {RESET}{RED}{err}"""

def cli(arg):
    if len(arg) <= 1:
        print(default_text)
    elif arg[1] in ["-h", "--help", "-help", "--h"]:
        print(default_text)
    elif arg[1] in ["-c", "-i", "--interpret"]:
        if len(arg) > 2:
            with open(arg[2], 'r') as file:
                run = interp.Interpreter(file.read()) 
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(run.Interprete())
        else:
            print(f"{PrintError('User Error', 'File argument required')}")     
    else:
        print(arg[1])

if __name__ == "__main__":
    cli(args)
