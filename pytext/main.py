import os
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
import datetime

filepath = "pytext - Unnamed.txt"
count = 0
root = Tk()
root.title(filepath)

try:
    root.iconbitmap('pytext.ico')

except:
    pass

root.geometry('400x400')
root.maxsize(height=400, width=400)

def save():
    global count
    global filepath

    count += 1

    if count <= 1:
        filepath = asksaveasfile(
            initialfile = 'Unnamed.txt',
            defaultextension=".txt",
            filetypes=[
                ("All Files","*.*"),
                ("Text Documents","*.txt")
            ]
        )

    elif not os.path.exists(filepath.name):
        filepath = asksaveasfile(
            initialfile = 'Unnamed.txt',
            defaultextension=".txt",
            filetypes=[
                ("All Files","*.*"),
                ("Text Documents","*.txt")
            ]
        )

    try:
        root.title('PyText - '+filepath.name)
        editit = open(filepath.name, "w")
        savetext = text_box.get(1.0, 'end')
        editit.write(savetext)
        editit.close()
        filepath.close()
    except:
        pass


def saveas():
    global filepath

    filepath = asksaveasfile(
    initialfile = 'Unnamed.txt',
    defaultextension=".txt",
    filetypes=[
            ("All Files","*.*"),
            ("Text Documents","*.txt")
            ]
        )

    try:
        root.title('PyText - '+filepath.name)
        editit = open(filepath.name, "w")
        savetext = text_box.get(1.0, 'end')
        editit.write(savetext)
        editit.close()
        filepath.close()

    except:
        pass

def openfile():
    global filepath
    filepath = askopenfile(
        defaultextension=".txt",
        filetypes=[
            ("All Files","*.*"),
            ("Text Documents","*.txt")
            ]
        )

    try:
        root.title('PyText - '+filepath.name)
        editit = filepath.read()
        text_box.delete(1.0, 'end')
        text_box.insert(1.0, editit)
        filepath.close()

    except:
        pass

def stamp():
    current_time = datetime.datetime.now()
    text_box.insert('end',
'''
'''
)
    
    text_box.insert('end', str(current_time))

def clear():
    text_box.delete(1.0, 'end')

def font(ftype):
    text_box.configure(font=ftype)

def wrap(typeofwrap):
    text_box.configure(wrap=typeofwrap)

def newfile():
    global count
    text_box.delete(1.0, 'end')
    count = 0
    root.title('pytext - Unnamed.txt')
    text_box.insert(1.0,
'''
 PyText 1.0 - A text editor made in python!
  This program was made by Jane Mat Dreaigs
'''
)


menubar = Menu(root)
root.config(menu=menubar)
arial = ("Arial", 11)
system = ("System", 11)
comicsans = ("Comic Sans MS", 10)
consolas = ("Consolas", 11)
courier = ("Courier", 10)
impact = ("Impact", 11)
gothic = ("Century Gothic", 11)
lucida = ("Lucida Handwriting", 9)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="Save As", command=saveas)
file.add_command(label="Save", command=save)
file.add_command(label="Open", command=openfile)
file.add_command(label="New File", command=newfile)

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Timestamp", command=stamp)
edit.add_command(label="Clear", command=clear)
wwrap = Menu(edit, tearoff=0)
wwrap.add_command(label="Character", command=lambda: wrap('char'))
wwrap.add_command(label="Word", command=lambda: wrap('word'))
wwrap.add_command(label="None", command=lambda: wrap('none'))
edit.add_cascade(label = 'Wrap', menu=wwrap)

options = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Font", menu=options)
options.add_command(label="Arial", command=lambda: font(arial))
options.add_command(label="Century Gothic", command=lambda: font(gothic))
options.add_command(label="Comic Sans MS", command=lambda: font(comicsans))
options.add_command(label="Consolas", command=lambda: font(consolas))
options.add_command(label="Courier", command=lambda: font(courier))
options.add_command(label="Impact", command=lambda: font(impact))
options.add_command(label="Lucida Handwriting", command=lambda: font(lucida))
options.add_command(label="System", command=lambda: font(system))

text_box = Text(root, height=23, width=46)

text_box.pack(side=LEFT, expand=True)
text_box.insert(1.0,
'''
 PyText 1.0 - A text editor made in python!
  This program was made by Jane Mat Dreaigs
'''
)
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=BOTH)

text_box.config(yscrollcommand=scroll.set)
text_box.tag_configure("center", justify='center')
text_box.tag_add("center", 1.0, "end")
scroll.config(command=text_box.yview)

root.mainloop()