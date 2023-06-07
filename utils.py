import glob
import operator
import re
from jinja2 import Template

def command_build():
    all_html_files = glob.glob("content/*.html")
    pages = generate_pages(all_html_files)

    for page in pages:
        resulting_html = apply_template(page, pages) 
        open(page["output"], 'w+').write(resulting_html)
        
def command_new():
    new_filename = input('Title of new page?')
    sanitized_str = re.sub(r'\W+', '_', new_filename).lower()
    open("content/"+sanitized_str+".html","w+").write("<title>"+sanitized_str+"</title>")

def generate_pages(files):
    pages = []
    for file in files:
        output = file.replace('content', 'docs')
        href = './'+output.split('/')[1]
        title = file.split('/')[1].split('.')[0].capitalize()
        if title == "Index":
            title = "About"

        pages.append({
        "filename": file,
        "title": title,
        "output": output,
        "href": href,
        })  

    #Reference: https://pythonhow.com/how/sort-a-list-of-dictionaries-by-a-value-of-the-dictionary/
    pages = sorted(pages, key=operator.itemgetter('title'))
    return pages

def apply_template(page, pages):
   
    file_page = open(page["filename"]).read()
    template_html = open('./templates/base.html').read()
    template = Template(template_html)
    finished_page = template.render(
        pages = pages,
        title = page["title"],
        content = file_page,
        selected_page = page["href"],
    )      
    return finished_page
