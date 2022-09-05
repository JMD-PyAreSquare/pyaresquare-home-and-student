from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageTk,  Image, ImageDraw
from PIL import *

widthh = 1000
height = 600
try:
    configfile = open('config.txt')
    content = configfile.read()
    widthh = int(content.split('\n', 1)[0])
    height = int(content.split('\n', 1)[1])
except:
    pass

def open():
    global myimage
    global canvas
    myfile = filedialog.askopenfilename(defaultextension='png', filetypes=(('PNG File', '.PNG'), ('PNG File')))
    filepath = myfile.title()
    selectedimg = ImageTk.PhotoImage(file=myfile)
    canvas.create_image(0, 0, image=selectedimg)
    myimage = Image.open(filepath)

def save():
    myfile = filedialog.asksaveasfilename(initialfile='portrait.png', defaultextension='png', filetypes=(('PNG File', '.PNG'), ('PNG File')))
    filepath = myfile.title()
    myimage.save(filepath)

def pickcolor():
    try:
        mycolor = colorchooser.askcolor()
        colorHex = str(mycolor[1])
        customoptions.add_command(label=colorHex, background=colorHex, command=lambda: color(colorHex))
    except:
        pass

def showimage():
    myimage.show()

def clear():
    canvas.delete('all')
    draw.rectangle([0, 0, widthh, height], fill='white')

def color(x):
    global kolor 
    kolor = x

def brush(z):
    global paintbrush
    paintbrush = z

def width(y):
    global weedth
    weedth = y

def paint(event):
    global kolor
    global weedth
    global paintbrush

    x1,y1=(event.x-1), (event.y-1)
    x2,y2=(event.x+1), (event.y+1)
    if paintbrush == 'rect':
        canvas.create_rectangle(x1, y1, x2, y2, fill=kolor, outline=kolor, width=weedth)
        draw.rectangle([x1, y1, x2+weedth, y2+weedth], fill=kolor, outline=kolor , width=weedth)
    if paintbrush == 'cal':
        canvas.create_polygon(x1, y1, x2, y2, fill=kolor, outline=kolor, width=weedth)
        draw.line([x1, y1, x2+weedth, y2+weedth], fill=kolor)
    if paintbrush == 'circle':
        canvas.create_oval(x1, y1, x2, y2, fill=kolor, outline=kolor, width=weedth)
        draw.ellipse([x1, y1, x2+weedth, y2+weedth], fill=kolor, width=weedth)
    
root = Tk()
paintbrush = 'circle'
root.title('pydraw')
try:
    root.iconbitmap('blackboard.ico')
except:
    pass
kolor = 'black'
weedth = 3
menubar = Menu(root, background='#80aaff', foreground='black')  
file = Menu(menubar, tearoff=0, background='#80aaff', foreground='black')  
file.add_command(label="clear", command=clear)   

coloroptions = Menu(file, tearoff=0)
sizeoptions = Menu(file, tearoff=0)
brushoptions = Menu(file, tearoff=0)
customoptions = Menu(file, tearoff=0)

file.add_command(label='save as', command=save)
file.add_command(label='open', command=open)
file.add_command(label='color picker', command=pickcolor)
file.add_command(label='show image', command=showimage)
file.add_separator()
coloroptions.add_command(label='red', background='red', command=lambda: color("red"))
coloroptions.add_command(label='blue', background='blue',command=lambda: color("blue"))
coloroptions.add_command(label='green', background='green',command=lambda: color("green"))
coloroptions.add_command(label='yellow', background='yellow',command=lambda: color("yellow"))
coloroptions.add_command(label='white', background='white',command=lambda: color("white"))
coloroptions.add_command(label='pink', background='pink',command=lambda: color("pink"))
coloroptions.add_command(label='black', background='black', foreground='white', command=lambda: color("black"))

sizeoptions.add_command(label='microscopic', command=lambda: width(0.25))
sizeoptions.add_command(label='very small', command=lambda: width(1))
sizeoptions.add_command(label='small', command=lambda: width(3))
sizeoptions.add_command(label='medium', command=lambda: width(5))
sizeoptions.add_command(label='semi-large', command=lambda: width(7))
sizeoptions.add_command(label='large', command=lambda: width(10))
sizeoptions.add_command(label='big chungus', command=lambda: width(20))

brushoptions.add_command(label='square pixel', command=lambda: brush('rect'))
brushoptions.add_command(label='calligraphy', command=lambda: brush('cal'))
brushoptions.add_command(label='rounded', command=lambda: brush('circle'))

file.add_cascade(label='brush', menu=brushoptions)
file.add_cascade(label='color', menu=coloroptions)
file.add_cascade(label='size', menu=sizeoptions)
file.add_cascade(label='custom colors', menu=customoptions)

root.config(menu=menubar)
menubar.add_cascade(label="options", menu=file) 
canvas = Canvas(root, width=widthh, height=height, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.bind('<B1-Motion>', paint)

myimage = Image.new('RGB', (widthh, height), (255,255,255))
draw = ImageDraw.Draw(myimage)

root.mainloop()