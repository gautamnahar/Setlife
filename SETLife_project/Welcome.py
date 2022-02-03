from tkinter import *
from ttkthemes import themed_tk as tk


class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title('SetLife')
        self.root.iconbitmap('D:/Desktop ')
        self.root.geometry("1366x800+0+0")
        self.root.resizable(True, True)
        self.mainform()

    def mainform(self):
        self.bg = PhotoImage(file="D:/Downloads/background1.png")

        my_canvas = Canvas(self.root)
        my_canvas.pack(fill="both", expand=True)

        my_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        my_canvas.create_text(683, 50, text="Welcome TO Setlife!", font=("Helvetica", 50, 'bold'), fill="white")

        my_canvas.create_text(200, 200, text="Select your login type:", font=("Helvetica", 20, 'bold'), fill="white")

        btn1 = Button(self.root, text="Student", command=self.nalla, cursor='hand2',
                      font=('times new roman', 16, 'bold'), bg='white', fg='blue', bd=0)
        btn1.place(x=50, y=250, width=350, height=50)

        btn2 = Button(self.root, text="Industry", command=self.organizationform, cursor='hand2',
                      font=('times new roman', 16, 'bold'), bg='white', fg='blue', bd=0)
        btn2.place(x=50, y=350, width=350, height=50)

        btn3 = Button(self.root, text="Click here for voice over control", command=self.andha, cursor='hand2',
                      font=('times new roman', 16, 'bold'), bg='white', fg='blue', bd=0)
        btn3.place(x=500, y=150, width=500, height=50)

    def organizationform(self):
        import Company

    def nalla(self):
        import nalla

    def andha(self):
        import Andha


root = tk.ThemedTk()
root.get_themes()
root.set_theme("black")

ob = Welcome(root)
root.mainloop()
