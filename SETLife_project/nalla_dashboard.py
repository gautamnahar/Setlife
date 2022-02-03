from tkinter import *

from SETLife_project import NtoC
from SETLife_project.nalla_setting import Nalla_Setting
from SETLife_project.nalla_profile import NProfile


class Dashboard:
    def __init__(self, root):
        self.user_id = "gautam_001"
        self.root = root
        self.root.title('SetLife')
        self.root.iconbitmap('D:/Downloads/icon1.ico')
        self.root.geometry("1366x800+0+0")
        self.root.resizable(True, True)
        self.mainform()

    def mainform(self):
        self.bg = PhotoImage(file="D:/Downloads/dashboardbg.png")
        self.profile1 = PhotoImage(file="D:/Downloads/profilebtns.png")
        self.profile = PhotoImage(file="D:/Downloads/profilebtn.png")
        self.search = PhotoImage(file="D:/Downloads/searchjobsbtn.png")
        self.setting = PhotoImage(file="D:/Downloads/settingsbtn.png")
        self.logout = PhotoImage(file="D:/Downloads/logoutbtn.png")

        my_canvas = Canvas(self.root)
        my_canvas.pack(fill="both", expand=True)

        my_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=25, y=25, height=100, width=1300)

        label1 = Label(frame_input, text="Dashboard", font=('Britannic Bold', 30, 'bold'), fg="blue", bg="white")
        label1.place(x=30, y=20)

        label2 = Label(frame_input, text="hello,", font=('Helvetica', 18, 'bold'), fg="blue", bg="white")
        label2.place(x=1000, y=25)

        labelimg = Label(frame_input, image=self.profile1, bd=0)
        labelimg.place(x=1080, y=30)

        btn3 = Button(frame_input, text=self.user_id, cursor='hand2', command=self.nallaprofile,
                      font=('times new roman', 16, 'bold'), bg='white', fg='indigo', bd=0)
        btn3.place(x=1105, y=25)

        btnframe = Frame(self.root, bg="white")
        btnframe.place(x=25, y=150, height=550, width=250)

        profilebtn = Button(btnframe, image=self.profile, command=self.nallaprofile, cursor='hand2', bd=0)
        profilebtn.place(x=20, y=50, width=216, height=72)

        searchbtn = Button(btnframe, image=self.search, command=self.searchjob, cursor='hand2', bd=0)
        searchbtn.place(x=20, y=175, width=216, height=72)

        settingsbtn = Button(btnframe, image=self.setting, command=self.nallasetting, cursor='hand2', bd=0)
        settingsbtn.place(x=20, y=300, width=216, height=72)

        logoutbtn = Button(btnframe, image=self.logout, command=self.signout, cursor='hand2', bd=0)
        logoutbtn.place(x=20, y=425, width=216, height=72)

        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=300, y=150, height=550, width=1020)
        self.searchjob()

    def nallaprofile(self):
        NProfile().userprofile(self.mainframe, self.user_id)

    def searchjob(self):
        NtoC().frontpage(self.mainframe, self.user_id)

    def nallasetting(self):
        Nalla_Setting().setting(self.mainframe, self.user_id)

    def signout(self):
        self.root.destroy()


root = Tk()
Dashboard(root)
root.mainloop()
