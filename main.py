import cli
from vars import *

def cprint(col, *args, **kwargs):
    print(col, end="")
    print(*args, **kwargs)
    print(RESET, end="")

def success_print(*args, **kwargs):
    cprint(GREEN, *args, **kwargs)

def err_print(*args, **kwargs):
    cprint(RED, *args, **kwargs)

def def_print(*args, **kwargs):
    cprint(RESET, *args, **kwargs)

def out_print(*args, **kwargs):
    cprint(WHITE, *args, **kwargs)

def cli_iter():
    def_print("Enter command: ", end="")
    cmd = input()
    output = cli.run_cmd(cmd)
    out_print(output, end="")

def cli_main():
    success_print("This is the workout uploader CLI.")
    while True:
        cli_iter()

if __name__ == "__main__":
    cli_main()