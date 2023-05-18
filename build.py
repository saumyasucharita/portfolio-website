
top_side_panel = open('./templates/top.html').read()
file_index = open('./content/index.html').read()
bottom_side_panel = open('./templates/bottom.html').read()
full_index = top_side_panel + file_index + bottom_side_panel
open('./docs/index.html', 'w+').write(full_index)

#Building education.html

file_edu = open('./content/education.html').read()
full_edu = top_side_panel + file_edu + bottom_side_panel
open('./docs/education.html', 'w+').write(full_edu)

#Building experience.html
file_exp = open('./content/experience.html').read()
full_exp = top_side_panel + file_exp + bottom_side_panel
open('./docs/experience.html', 'w+').write(full_exp)

#Building projects.html
file_proj = open('./content/projects.html').read()
full_proj = top_side_panel + file_proj + bottom_side_panel
open('./docs/projects.html', 'w+').write(full_proj)


