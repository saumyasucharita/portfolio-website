
import sys
from utils import command_build
from utils import command_new

def main():

    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified")
        command_build()
    
    elif command == "new":
        print("New page was specified")
        command_new()
        
    
    else:
        print("Please specify ’build’ or ’new’")

        sys.stderr.write("Usage: ")
        sys.stderr.write("Rebuild site:     python manage.py build")
        sys.stderr.write("Create new page:  python manage.py new")

main()