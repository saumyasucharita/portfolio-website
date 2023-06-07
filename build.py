
# pages = [
#         {
#             "filename": "content/index.html",
#             "output": "docs/index.html",
#             "title": "About Me",
#             "href": "./index.html",
#             "link_title": "About",
#         },
#         {
#             "filename": "content/education.html",
#             "output": "docs/education.html",
#             "title": "My education",
#             "href": "./education.html",
#             "link_title": "Education",
#         },
#         {
#             "filename": "content/experience.html",
#             "output": "docs/experience.html",
#             "title": "My experience",
#             "href": "./experience.html",
#             "link_title": "Experience",
#         },
#         {
#             "filename": "content/projects.html",
#             "output": "docs/projects.html",
#             "title": "My projects",
#             "href": "./projects.html",
#             "link_title": "Projects",
#         },
#     ]
# pipenv --python 3
# pipenv shell
# pipenv install jinja2 

import glob
import operator
from jinja2 import Template


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


def main():

    all_html_files = glob.glob("content/*.html")
    pages = generate_pages(all_html_files)

    for page in pages:
        resulting_html = apply_template(page, pages) 
        open(page["output"], 'w+').write(resulting_html)

main()