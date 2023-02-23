# Imports
import os
import configparser

# Constants
NAME = "EOS"
DEFAULT = "<default>"
DEFAULT_PROMPT = "> "
FORMAT_SCRIPT = '.py'
CORE = 'python'
FORMAT_HELP = '.help'

# Pathes
ROOT_PATH = os.path.realpath(os.path.dirname(__name__))
DOC_DIR = '.\\doc'
BIN_DIR = '.\\bin'
WELCOME_PATH = '.\\welcome.txt'
CONSOLE_HELP_PATH = os.path.join(DOC_DIR, NAME+FORMAT_HELP)

# Settings
DISABLE_EXPLORER = False
SHOW_FOUND_PROGRAMS = True

# Variables
exitis = False
prompt = "> "
command = ""
name = ""
args = []
prg_list = []

def stop(exit_code):
    global exitis, DISABLE_EXPLORER, SHOW_FOUND_PROGRAMS
    if DISABLE_EXPLORER:
        os.system('start explorer.exe')
    exitis = True
    exit(exit_code)
    

def init():
    global NAME, DISABLE_EXPLORER, prg_list
    os.system(f"cd \" + {ROOT_PATH} + \"") 
    os.system(f'title Initialization {NAME}...')
    if DISABLE_EXPLORER:
        os.system('taskkill /f /im explorer.exe')
    print("Testing files...")

    try:
        if not os.path.isdir(BIN_DIR): raise FileNotFoundError
        if not os.path.isdir(DOC_DIR): raise FileNotFoundError
        if not os.path.isfile('.\\'+CONSOLE_HELP_PATH): raise FileNotFoundError
        if not os.path.isfile(WELCOME_PATH): raise FileNotFoundError
        
    except FileNotFoundError:
        print("System heat is damaged.")
        stop(1)
        
    print("Test compile!")
    
    print("Finding programs...")
    prg_list = os.listdir(BIN_DIR)
    if SHOW_FOUND_PROGRAMS:
        for prg in prg_list:
            print(f"  {prg}")

    print("Initialization codepage...")
    os.system('mode con CP SELECT=866')

    print("Starting console...")

def NotArgumentsError():
    print("Arguments not found.")
  
def main():
    global prompt, exitis, NAME
    os.system('cls')
    os.system(f'title {NAME}')
    print(open(WELCOME_PATH, 'r').read())
    while not exitis:
        try:
            command = input(prompt).lower().split()
            prg_list = os.listdir(BIN_DIR)
            if command != []:
                name = str(command[0])
            else:
                name = ""
            args = command[1: ]
            if args == []:
                args = None
        except EOFError:
            stop(0)
        if name == "help":
            if args == None:
                print(open(CONSOLE_HELP_PATH, 'r').read())
            else:
                work_H = False
                try:
                    txt_H = open(os.path.join(DOC_DIR, args[0] + FORMAT_HELP), 'r').read()
                    work_H = True
                except FileNotFoundError:
                    work_H = False
                if work_H:
                    print(txt_H)
                else:
                    print("Help of command not found.")
                
        elif name == "exit":
            stop(0)
        elif name == "restart":
            main()
            exitis = True
        elif name == "prompt":
            if args != None:
                if args[0] == DEFAULT:
                    prompt = DEFAULT_PROMPT
                else:
                    prompt = args[0]
            else:
                 NotArgumentsError()  
        elif name == "cmd":
            if args != None:
                os.system(args[0])
            else:
                 NotArgumentsError()
        elif name == "list":
            print("=== Scripts ===")
            for n in prg_list:
                nl = n.split('.')
                if nl[-1] == 'py':
                    print(nl[0])
            print("===============")
        elif name == "clear":
            os.system('cls')
        else:
            if (name + FORMAT_SCRIPT) in prg_list:
                filename = name+FORMAT_SCRIPT
                cmd = os.path.join(BIN_DIR, filename)
                try:
                    exec(open(cmd, 'r').read())
                except Exception as error:
                    print(f"Script error: {error}")
            else:
                print(f"Invaild command \"{name}\".")


if __name__ == '__main__':
    init()
    main()
