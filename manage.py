
import sys
from utils import command_build
from utils import command_new
import markdown

def main():

    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)

    # file_page = open('content/index.md').read()
    # content_html = markdown.markdown(file_page)
    # print(content_html)
    
#     md = markdown.Markdown(extensions=["markdown.extensions.meta"])
#     data = """title: My New Blog
# author: Jane Q Hacker
# order: 1
# Welcome to my ~~site~~ *blog*
#     """
#     html = md.convert(data)
#     title = md.Meta["title"][0]
#     author = md.Meta["author"][0]
#     order = md.Meta["order"][0]
#     print(title, "by", author, "in order", order)
#     print(html)

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