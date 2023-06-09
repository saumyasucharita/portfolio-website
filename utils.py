import glob
import operator
import re
import markdown
from jinja2 import Template

def command_build():
    all_html_files = glob.glob("content/*.md")
    pages = generate_pages(all_html_files)
    
    new_pages = []
    for page in pages:
        new_page = convert_md_html(page)
        new_pages.append(new_page)
    #Reference: https://pythonhow.com/how/sort-a-list-of-dictionaries-by-a-value-of-the-dictionary/
    new_pages = sorted(new_pages, key=operator.itemgetter('order'))

    for new_page in new_pages:
        print("Building ", new_page['title'])
        resulting_html = apply_template(new_page, new_pages) 
        open(new_page["output"], 'w+').write(resulting_html)    

def command_new():
    new_filename = input('Title of new page?')
    sanitized_str = re.sub(r'\W+', '_', new_filename).lower()
    open("content/"+sanitized_str+".html","w+").write("<title>"+sanitized_str+"</title>")

def generate_pages(files):
    pages = []
    for file in files:
        output = file.replace('content', 'docs').replace('md', 'html')
        href = './'+output.split('/')[1]
        title = file.split('/')[1].split('.')[0].capitalize()
        if title == "Index":
            title = "About"

        pages.append({
        "filename": file,
        "title": title,
        "output": output,
        "href": href,
        "html": None,
        "order": None,
        })  

    return pages

def convert_md_html(page):
    
    file_page = open(page["filename"]).read()
    #content_html = markdown.markdown(file_page)
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    content_html = md.convert(file_page)
    order = md.Meta["order"][0]
    page['html'] = content_html
    page['order'] = order
    return page

def apply_template(page, pages):

    template_html = open('./templates/base.html').read()
    template = Template(template_html)
    finished_page = template.render(
        pages = pages,
        title = page["title"],
        content = page['html'],
        selected_page = page["href"],
    )      
    return finished_page
