import linecache
from  tkinter import * 
import tkinter.messagebox

deleted = False
enablecommands = False

def refresh():
    tempsession = open('saves.txt', 'w')
    tempsession.write('')
    tempsession.close()
    window.destroy()

def pickbackup():
    try:
        session = open('saves.txt')
    except:
        session = open('saves.txt', 'x')
        session.close()
        session = open('saves.txt', 'r')
        tkinter.messagebox.showwarning(title='stop messing with me', message='you deleted or modified a major file. why did you do that? nevermind, but dont do it again. i know where u live')
    total_lines = len(session.readlines())
    session.close()
    for q in range(total_lines):
        listbox_task.insert(END, (linecache.getline('saves.txt', q+1)))

def entertask():
    global deleted
    global enablecommands
    input_text=""
    def add():
        global deleted
        global enablecommands
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="woah",message="You can't leave that blank, buddy.")
        elif input_text.startswith('/enablecommands'):
            try:
                if input_text[16] == '1':
                    enablecommands = True
                    tkinter.messagebox.showinfo(title='nice work', message="commands are now enabled i guess")
                elif input_text[16] == '0':
                    enablecommands = False
                    tkinter.messagebox.showinfo(title="annnnd they're gone", message="you've just disabled commands, /enablecommands will still work, though.")
                else:
                    tkinter.messagebox.showerror(title='whoops', message='I see that you are trying to enable commands. True is 1 and False is 0.')
            except:
                    tkinter.messagebox.showerror(title='whoops', message='I see that you are trying to enable commands. True is 1 and False is 0.')
        elif input_text=="/info" and enablecommands==True:
            tkinter.messagebox.showinfo(title='info', message='This program was made by Jane Mat Dreaigs on the 4th of september, 2022. Version 1.0')
            root1.destroy()
        elif input_text=="/info" and enablecommands==False:
            tkinter.messagebox.showwarning(title="commands aren't enabled", message="thats actually a command, but commands aren't enabled.")
        elif input_text=="/janematdreaigs" and enablecommands==True:
            tkinter.messagebox.showinfo(title='jane mat dreaigs', message="If you unscramble 'Jane Mat Dreaigs', you get 'i aM sateJ ganDre. stop asking questions.")
            root1.destroy()
        elif input_text=="/janematdreaigs" and enablecommands==False:
            tkinter.messagebox.showwarning(title="commands aren't enabled", message="thats actually a command, but commands aren't enabled.")
        elif input_text.startswith('/'):
            tkinter.messagebox.showerror(title='bruh', message='are you making commands up or are you just misspelling them?')
        else:
            listbox_task.insert(END,input_text)
            saves = open('saves.txt', 'a')
            if deleted==False:
                saves.write(f'{input_text}\n')
            elif deleted==True:
                saves.write(f'\n{input_text}\n')
                deleted = False
            saves.close()
            root1.destroy()

    root1=Tk()
    root1.config(bg='black')
    root1.title("new task")
    entry_task=Text(root1,width=40,height=4,bg='black',fg='limegreen',font='Terminal')
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add, bd=-1, bg='black', fg='limegreen', font='Terminal')
    button_temp.pack()
    root1.mainloop()

def deletetask():
    global deleted
    try:
        selected=listbox_task.curselection()
        deleteword = listbox_task.get(selected)
        listbox_task.delete(selected[0])
        saves = open('saves.txt', 'r')
        savedtext = saves.read()
        savedtext = savedtext.replace(deleteword, '')
        deleted = True
        savedtext = savedtext.strip()
        saves.close()
        saves = open('saves.txt', 'w')
        saves.write(savedtext)
        saves.close()
    except:
        tkinter.messagebox.showerror(title='well thats weird', message="you wanted to delete something but you didn't select anything. but if you delete nothing, then wouldn't that mean that you keep everything? alright, just select something next time okay?")

def markcompleted():
    try:
        marked=listbox_task.curselection()
        temp=marked[0]
        temp_marked=listbox_task.get(marked)
        temp_marked=temp_marked.strip('\n')
        temp_marked=temp_marked+" [FINISHED!]"
        listbox_task.delete(temp)
        with open('saves.txt', 'r') as file:
            data = file.readlines()

        data[temp] = f'{temp_marked}\n'

        with open('saves.txt', 'w') as file:
            file.writelines(data)
        listbox_task.insert(temp,temp_marked)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title='well thats weird', message="well thats an error. try re-installing pytasks or contact me at jmd.pyaresquare@gmail.com if you still need help.")

window=Tk()
window.title("pytasks 1.0")
try:
    window.iconbitmap('pencil.ico')
except:
    pass
window.config(bg='black')
frame_task=Frame(window)
frame_task.pack()

listbox_task=Listbox(frame_task,bg="black",fg="limegreen",height=15,width=40,font = "Terminal", bd=0)  
listbox_task.pack(side=tkinter.LEFT)
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button=Button(window,text="new task",width=40,command=entertask, bg='black',fg="limegreen",font = "Terminal", bd=-1)
entry_button.pack(pady=3)

mark_button=Button(window,text="mark selected task as finished",width=40,command=markcompleted, bg='black',fg="limegreen",font = "Terminal", bd=-1)
mark_button.pack(pady=3)

delete_button=Button(window,text="remove selected task",width=40,command=deletetask, bg='black',fg="limegreen",font = "Terminal", bd=-1)
delete_button.pack(pady=3)

deletee_button=Button(window,text="delete all tasks",width=40,command=refresh, bg='black',fg="limegreen",font = "Terminal", bd=-1)
deletee_button.pack(pady=3)

pickbackup()

window.mainloop()