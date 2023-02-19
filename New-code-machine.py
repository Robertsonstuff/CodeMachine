
title = input("<!--what will be your new heading? ")
time = input("what will be the time that you posted it? format is 'hh:mm dd/mm/yyyy' ")
post = input("what is your new blog post? ")

print(f"""-->\n<div class="content">\n<button type="button" class="expand-button" style="fas-fa-chevron-down"><h1>{title}</h1><br> -Much love {time} - By me.</button>\n<div class="content-expand">\n<br>\n<cite>-Much love {time}-</cite>By me.\n<br>\n<br>\n<p>{post}\n""")

para = input("<!--start blogging: ")

lst = []


lst.append('\n<br>\n<br>\n' + para)

while para != 'endpost':
	lst.append('\n<br>\n<br>\n')
	para = input()
	if para == 'endpost':
		break
	else:
		lst.append(para)


print("-->")
print(''.join(lst))			
print(f"""</p>\n<br>\n<br>\n<a href="#top">
		Jump to the top</a>\n\t\t</div>\n</div>""")
