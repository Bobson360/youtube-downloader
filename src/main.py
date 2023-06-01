import sys
from .cli import cli_main
from .gui import gui_main

def main():
    # If there are command line arguments, assume CLI
    if len(sys.argv) > 1:
        cli_main()
    # Otherwise, start the GUI
    else:
        gui_main()

if __name__ == '__main__':
    main()
