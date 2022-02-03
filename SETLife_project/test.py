from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("500x600")


def upload_file():
    f = open("resume.txt", "w")
    text = str(entry.get(1.0, END))
    f.write(text)
    f.close()


def clear():
    entry.delete(1.0, END)


def load_file():
    file = filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)


b1 = Button(root, text="Upload", command=upload_file, cursor='hand2', font=('calibri', 10), bg='white',
            fg='green', bd=0)
b1.place(x=180, y=10)

b2 = Button(root, text="clear", command=clear)
b2.place(x=70, y=10)

b3 = Button(root, text="load", command=load_file)
b3.place(x=10, y=10)

entry = Text(root, height=33, width=58, wrap=WORD)
entry.place(x=10, y=50)

root.mainloop()