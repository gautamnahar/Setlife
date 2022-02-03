from tkinter import *
from tkinter import messagebox, ttk
import pymysql


class CProfile:
    def userprofile(self, mainframe, orgid):
        self.orgid = orgid

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
        cur.execute("select * from company where org_id=%s", self.orgid)
        results = cur.fetchall()
        self.name = results[0][1]
        self.femail = results[0][2]
        self.fphone = results[0][3]
        self.frevenue = results[0][4]
        self.fdep = results[0][5]
        con.close()

        if self.frevenue is None:
            self.frevenue = " "
        if self.fdep is None:
            self.fdep = " "

        labelname = Label(self.second_frame, text="Name:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelname.place(x=200, y=120)

        labelrev = Label(self.second_frame, text="Revenue:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelrev.place(x=200, y=170)

        labeldep = Label(self.second_frame, text="Department:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labeldep.place(x=200, y=220)

        labelphone = Label(self.second_frame, text="Phone:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelphone.place(x=200, y=270)

        labelmail = Label(self.second_frame, text="Email:", font=('calibre', 14, 'bold'), fg="red", bg="white")
        labelmail.place(x=200, y=320)

        self.lname = Label(self.second_frame, text=self.name, font=('calibre', 14, 'bold'), fg="black",
                      bg="white")
        self.lname.place(x=400, y=120)

        self.labelrev = Label(self.second_frame, text=self.frevenue, font=('calibre', 14, 'bold'), fg="black",
                              bg="white")
        self.labelrev.place(x=400, y=170)

        self.labeldep = Label(self.second_frame, text=self.fdep, font=('calibre', 14, 'bold'), fg="black",
                              bg="white")
        self.labeldep.place(x=400, y=220)

        self.labelphone = Label(self.second_frame, text=self.fphone, font=('calibre', 14, 'bold'), fg="black",
                                bg="white")
        self.labelphone.place(x=400, y=270)

        self.labelmail = Label(self.second_frame, text=self.femail, font=('calibre', 14, 'bold'), fg="black",
                               bg="white")
        self.labelmail.place(x=400, y=320)

        self.editbtn = Button(self.second_frame, text="Edit", cursor='hand2', command=self.update,
                              font=('times new roman', 18, 'bold'), bg='blue', fg='white', bd=0)
        self.editbtn.place(x=370, y=380, width=75, height=40)

    def update(self):
        self.lname.destroy()
        self.labelrev.destroy()
        self.labeldep.destroy()
        self.editbtn.destroy()

        self.ename = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.ename.place(x=400, y=120, width=250, height=30)

        self.erev = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.erev.place(x=400, y=170, width=250, height=30)

        self.edep = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.edep.place(x=400, y=220, width=250, height=30)

        self.updatebtn = Button(self.second_frame, text="Update", cursor='hand2', command=self.submit,
                                font=('times new roman', 18, 'bold'), bg='green', fg='white', bd=0)
        self.updatebtn.place(x=300, y=380, width=90, height=40)

    def submit(self):
        if self.ename.get() == "":
            messagebox.showerror("Error", "Please Enter your name!", parent=self.second_frame)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()

                cur.execute('UPDATE company SET name = %s,revenue = %s,department = %s WHERE userid = %s',
                            (self.ename.get(), self.erev.get(), self.edep.get(), self.orgid))
                con.commit()
                con.close()
                messagebox.showinfo("success", parent=self.second_frame)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.second_frame)
