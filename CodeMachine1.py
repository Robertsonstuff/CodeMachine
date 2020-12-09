
from tkinter import *

def save_info():
    #print("hello Luke")
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    post_info = post.get()
    print(firstname_info, lastname_info, post_info)

    file = open("newpost.txt", "a+")
    file.write("<div class='con container2'>\n<h1>" + firstname_info + "</h1>\n<br>\n")
    file.write("<cite>-Much Love " + lastname_info + "-</cite>By me.\n<br>\n<br>\n<p>\n")
    file.write(post_info + "\n")
    print(" User ", firstname_info, "registered successfully")
    file.close

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    post_entry.delete(0, END)

def end_post():

    file = open("newpost.txt", "a+")
    file.write("</p>\n<br>\n<br>\n<a href='#top'>Jump to the top</a>\n</div>\n")
    print(" Posted, Signed, sealed and delivered")
    file.close



root = Tk()
root.geometry("500x350")
root.title("Luke's Blog Post Code Machine")
heading = Label(root,
text = "Python Form", bg = "white", fg = "black", width = "500", height = "3")
heading.pack()

firstname_text = Label(root,
text = "Title * ",)
lastname_text = Label(root,
text = "(Time and Date) Posted * ",)
post_text = Label(root,
text = "Post * ",)
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 140)
post_text.place(x = 15, y = 210)

firstname = StringVar()
lastname = StringVar()
post = StringVar()

firstname_entry = Entry(textvariable = firstname, width = "30")
lastname_entry = Entry(textvariable = lastname, width = "20")
post_entry = Entry(root, textvariable = post, width = "70")

firstname_entry.place(x = 15, y = 100)
lastname_entry.place(x = 15, y = 170)
post_entry.place(x = 15, y = 240)

register = Button(root,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
finish = Button(root,text = "End Post", width = "30", height = "2", command = end_post, bg = "grey")
register.place(x = 15, y = 290)
finish.place(x = 250, y = 290)

root.mainloop()