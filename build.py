
pages = [
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title": "About Me",
            "href": "./index.html",
            "link_title": "About",
        },
        {
            "filename": "content/education.html",
            "output": "docs/education.html",
            "title": "My education",
            "href": "./education.html",
            "link_title": "Education",
        },
        {
            "filename": "content/experience.html",
            "output": "docs/experience.html",
            "title": "My experience",
            "href": "./experience.html",
            "link_title": "Experience",
        },
        {
            "filename": "content/projects.html",
            "output": "docs/projects.html",
            "title": "My projects",
            "href": "./projects.html",
            "link_title": "Projects",
        },
    ]
#Phase 4: Function refactor
def generate_title(page):
    template = open('./templates/base.html').read()
    int_page = template.replace("{{title}}", page["title"])
    return int_page

#Phase 5: Advanced templating
def generate_nav_list():
    list_template = ''
    for page in pages:
        list_template += f'<li class="nav-item"><a class="nav-link js-scroll-trigger" href="{ page["href"] }">{ page["link_title"] }</a></li>'
    return list_template

def apply_template(page, int_page):
    file_page = open(page["filename"]).read()
    #Phase 3 - String replacement templating
    #String replace in base.html page
    finished_page = int_page.replace("{{content}}", file_page)
    new_nav = generate_nav_list()
    finished_page = finished_page.replace("{{nav}}", new_nav) 
        
    return finished_page

# Phase 1: Code is in "main" function
def main():

    # Phase 2: Using lists to store information of all content pages
    template = open('./templates/base.html').read()
    
    # for page in pages:
    #     file_page = open(page["filename"]).read()
    #     full_page = top_side_panel + file_page + bottom_side_panel
    #     open(page["output"], 'w+').write(full_page)

    
    # for page in pages:
    #     #Read content of content HTML page
    #     file_page = open(page["filename"]).read()

    #     #String replace in base.html page
    #     finished_page = template.replace("{{content}}", file_page)
    #     open(page["output"], 'w+').write(finished_page)

    for page in pages:
        int_html = generate_title(page) #Function call
        resulting_html = apply_template(page, int_html) 
        open(page["output"], 'w+').write(resulting_html)

main()