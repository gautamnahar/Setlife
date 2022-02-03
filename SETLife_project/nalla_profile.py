from tkinter import *
from tkinter import messagebox, ttk
import pymysql

from SETLife_project.nalla_resume import NallaResume


class NProfile:
    def userprofile(self, mainframe, userid):
        self.userid = userid

        my_canvas = Canvas(mainframe)
        my_canvas.place(x=0, y=0, height=550, width=1020)

        scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=my_canvas.yview)
        scrollbar.place(x=1000, y=0, height=550, width=20)

        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        self.second_frame = Frame(my_canvas, bg="white")

        my_canvas.create_window((0, 0), height=750, width=1020, window=self.second_frame, anchor="nw")

        label1 = Label(self.second_frame, text="Your Profile", font=('bell mt', 20, 'bold'), fg="blue", bg="white")
        label1.place(x=25, y=10)

        partition = Frame(self.second_frame, bg="blue")
        partition.place(x=25, y=50, height=2, width=950)

        con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
        cur = con.cursor()
        cur.execute("select * from nallaprofile where userid=%s", self.userid)
        results = cur.fetchall()
        self.fname = results[0][1]
        self.fphone = results[0][2]
        self.femail = results[0][3]
        self.fedu = results[0][4]
        self.fskills = results[0][5]
        self.fpast = results[0][6]
        self.fexp = results[0][7]
        con.close()

        if self.fedu is None:
            self.fedu = " "
        if self.fskills is None:
            self.fskills = " "
        if self.fpast is None:
            self.fpast = " "
        if self.fexp is None:
            self.fexp = " "

        labelname = Label(self.second_frame, text="Name:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelname.place(x=200, y=120)

        labelskill = Label(self.second_frame, text="Skills:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelskill.place(x=200, y=190)

        labeledu = Label(self.second_frame, text="Education:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labeledu.place(x=200, y=260)

        labelexp = Label(self.second_frame, text="Experience:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelexp.place(x=200, y=330)

        labelpast = Label(self.second_frame, text="Past Performance:", font=('calibre', 14, 'bold'), fg="red",
                          bg="white")
        labelpast.place(x=200, y=400)

        labelemail = Label(self.second_frame, text="Email_ID:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelemail.place(x=200, y=470)

        labelphone = Label(self.second_frame, text="Contact:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelphone.place(x=200, y=540)

        self.labelname = Label(self.second_frame, text=self.fname, font=('calibre', 14, 'bold'), fg="black", bg="white")
        self.labelname.place(x=400, y=120)

        self.labelskill = Label(self.second_frame, text=self.fskills, font=('calibre', 14, 'bold'), fg="black",
                                bg="white")
        self.labelskill.place(x=400, y=190)

        self.labeledu = Label(self.second_frame, text=self.fedu, font=('calibre', 14, 'bold'), fg="black", bg="white")
        self.labeledu.place(x=400, y=260)

        self.labelexp = Label(self.second_frame, text=self.fexp, font=('calibre', 14, 'bold'), fg="black", bg="white")
        self.labelexp.place(x=400, y=330)

        self.labelpast = Label(self.second_frame, text=self.fpast, font=('calibre', 14, 'bold'), fg="black", bg="white")
        self.labelpast.place(x=400, y=400)

        self.labelemail = Label(self.second_frame, text=self.femail, font=('calibre', 14, 'bold'), fg="black",
                                bg="white")
        self.labelemail.place(x=400, y=470)

        self.labelphone = Label(self.second_frame, text=self.fphone, font=('calibre', 14, 'bold'), fg="black",
                                bg="white")
        self.labelphone.place(x=400, y=540)

        self.resumebtn = Button(self.second_frame, text="Review your Resume", command=self.showresume, cursor='hand2',
                                font=('times new roman', 18, 'bold'), bg='white', fg='blue', bd=0)
        self.resumebtn.place(x=310, y=680, width=230, height=35)

        self.editbtn = Button(self.second_frame, text="Edit", cursor='hand2', command=self.update,
                              font=('times new roman', 18, 'bold'), bg='blue', fg='white', bd=0)
        self.editbtn.place(x=370, y=620, width=75, height=40)

    def showresume(self):
        NallaResume().resume(self.userid, self.second_frame)

    def update(self):
        self.labelname.destroy()
        self.labelskill.destroy()
        self.labeledu.destroy()
        self.labelexp.destroy()
        self.labelpast.destroy()
        self.editbtn.destroy()
        self.resumebtn.destroy()

        self.ename = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.ename.place(x=400, y=120, width=270, height=35)

        self.eskill = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.eskill.place(x=400, y=190, width=270, height=35)

        self.eedu = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.eedu.place(x=400, y=260, width=270, height=35)

        self.eexp = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.eexp.place(x=400, y=330, width=270, height=35)

        self.epast = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.epast.place(x=400, y=400, width=270, height=35)

        self.updatebtn = Button(self.second_frame, text="Update", cursor='hand2', command=self.submit,
                                font=('times new roman', 18, 'bold'), bg='green', fg='white', bd=0)
        self.updatebtn.place(x=300, y=620, width=90, height=40)

    def submit(self):
        if self.ename.get() == "":
            messagebox.showerror("Error", "Please Enter your name!", parent=self.second_frame)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()

                cur.execute('UPDATE nallaprofile SET name = %s,education = %s,skills = %s,past_performance = %s,'
                            'experience = %s WHERE userid = %s',
                            (self.ename.get(), self.eedu.get(), self.eskill.get(), self.epast.get(), self.eexp.get(),
                             self.userid))
                con.commit()
                con.close()
                messagebox.showinfo("success", parent=self.second_frame)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.second_frame)
