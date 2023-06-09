import glob
import operator
import re
import markdown
from jinja2 import Template

def command_build():
    #Return all the markdown files in the content folder
    all_html_files = glob.glob("content/*.md")
    pages = generate_pages(all_html_files)
    
    for page in pages:
        convert_md_html(page)
       
    #Reference: https://pythonhow.com/how/sort-a-list-of-dictionaries-by-a-value-of-the-dictionary/
    pages.sort(key=operator.itemgetter('order'))

    for new_page in pages:
        resulting_html = apply_template(new_page, pages) 
        open(new_page["output"], 'w+').write(resulting_html)    

#Function to add a new html page by user input
def command_new():
    new_filename = input('Title of new page?')
    sanitized_str = re.sub(r'\W+', '_', new_filename).lower()
    open("content/"+sanitized_str+".html","w+").write("<title>"+sanitized_str+"</title>")

#Return a list of dictionaries having the meta data of the html pages 
def generate_pages(files):
    pages = []
    #Loop through each file in the content folder
    for file in files:
        output = file.replace('content', 'docs').replace('md', 'html')
        href = './'+output.split('/')[1]
        link_title = file.split('/')[1].split('.')[0].capitalize()
        if link_title == "Index":
            link_title = "About"

        pages.append({
        "filename": file,
        "output": output,
        "href": href,
        "link_title": link_title,
        })  

    return pages

#Read the content of the markdown files and convert those to html
def convert_md_html(page):
   
    file_page = open(page["filename"]).read()
    #content_html = markdown.markdown(file_page)
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    content_html = md.convert(file_page)
    order = md.Meta["order"][0]
    title = md.Meta["title"][0]
    #Update the dictionary with metadata from the markdown files
    page['title'] = title
    page['html'] = content_html
    page['order'] = order
    
#Use jinja templating to replace placeholders in base.html with html content
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
