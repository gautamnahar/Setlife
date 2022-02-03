import smtplib
import random
from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
import pymysql

from SETLife_project.CompanytoNalla import CtoN
from SETLife_project.company_profile import CProfile


class CDashboard:
    def __init__(self, root):
        self.org_id = "gautam_001"
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
        self.search = PhotoImage(file="D:/Downloads/searchemployeebtn.png")
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

        btn3 = Button(frame_input, text=self.org_id, cursor='hand2', command=self.nallaprofile,
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
        CProfile().userprofile(self.mainframe, self.org_id)

    def searchjob(self):
        CtoN().frontpage(self.mainframe, self.org_id)

    def nallasetting(self):
        con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
        cur = con.cursor()
        cur.execute("select * from company where org_id=%s", self.org_id)
        results = cur.fetchall()
        self.fpass = results[0][2]
        con.close()

        self.Frame1 = Frame(self.mainframe, bg="white")
        self.Frame1.place(x=0, y=0, height=550, width=1020)

        btn1 = Button(self.Frame1, text="Update Password", cursor='hand2', command=self.upass,
                      font=('times new roman', 16, 'bold'), bg='grey', fg='white', bd=0)
        btn1.place(x=40, y=100, width=200, height=50)

        btn2 = Button(self.Frame1, text="Update Email_ID", cursor='hand2', command=self.uemail,
                      font=('times new roman', 16, 'bold'), bg='grey', fg='white', bd=0)
        btn2.place(x=40, y=200, width=200, height=50)

        btn3 = Button(self.Frame1, text="Update Contact_No.", cursor='hand2', command=self.uphone,
                      font=('times new roman', 16, 'bold'), bg='grey', fg='white', bd=0)
        btn3.place(x=40, y=300, width=200, height=50)

    def upass(self):
        frame2 = Frame(self.Frame1, bg="grey")
        frame2.place(x=300, y=50, height=450, width=700)

        lcpass = Label(frame2, text="Current Password:", font=('calibre', 14, 'bold'), fg="white", bg="grey")
        lcpass.place(x=50, y=50)
        self.lcpass = Entry(frame2, font=("times new roman", 14, "bold"), bg='white', bd=1)
        self.lcpass.place(x=270, y=50, width=250, height=35)

        lnpass = Label(frame2, text="New Password:", font=('calibre', 14, 'bold'), fg="white", bg="grey")
        lnpass.place(x=50, y=150)
        self.lnpass = Entry(frame2, show="*", font=("times new roman", 14, "bold"), bg='white', bd=1)
        self.lnpass.place(x=270, y=150, width=250, height=35)

        lcnpass = Label(frame2, text="Confirm Password:", font=('calibre', 14, 'bold'), fg="white", bg="grey")
        lcnpass.place(x=50, y=250)
        self.lcnpass = Entry(frame2, show="*", font=("times new roman", 14, "bold"), bg='white', bd=1)
        self.lcnpass.place(x=270, y=250, width=250, height=35)

        donebtn = Button(frame2, text="Done", cursor='hand2', command=self.updatepass,
                         font=('times new roman', 18, 'bold'), bg='white', fg='grey', bd=0)
        donebtn.place(x=300, y=350, width=75, height=40)

    def updatepass(self):
        if self.lcpass.get() != self.fpass:
            messagebox.showerror('Error', 'Invalid Current Password!', parent=self.Frame1)
        elif self.lnpass.get() != self.lcnpass.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.Frame1)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()
                cur.execute('UPDATE companylogin SET password = %s WHERE org_id = %s',
                            (self.lnpass.get(), self.org_id))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Your Password is now changed", parent=self.Frame1)

            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.Frame1)

    def uemail(self):
        self.frame2 = Frame(self.Frame1, bg="grey")
        self.frame2.place(x=300, y=50, height=450, width=700)

        nemail = Label(self.frame2, text="Enter your Email-ID:", font=('calibre', 14, 'bold'), fg="white", bg="grey")
        nemail.place(x=50, y=50)
        self.nemail = Entry(self.frame2, font=("times new roman", 14, "bold"), bg='white', bd=1)
        self.nemail.place(x=50, y=100, width=250, height=35)

        vemailbtn = Button(self.frame2, text="Verify", cursor='hand2', command=self.verifyemail,
                           font=('times new roman', 16, 'bold'), bg='white', fg='black', bd=0)
        vemailbtn.place(x=350, y=100, width=75, height=35)

    def verifyemail(self):
        if self.nemail.get() == "":
            messagebox.showerror("Error", "Please enter a email id!", parent=self.Frame1)
        else:
            o = smtplib.SMTP("smtp.gmail.com", 587)
            o.starttls()
            o.login("setlife.customercare@gmail.com", "Setlife@123")
            self.EOTP = random.randint(1000, 9999)
            message = "Your otp for new email-id registration is " + str(self.EOTP)
            RecieverAddress = [self.nemail.get()]
            o.sendmail("setlife.customercare@gmail.com", RecieverAddress, message)
            o.quit()

            lotp = Label(self.frame2, text="Enter OTP sent on new email-id:", font=('calibre', 14, 'bold'),
                         fg="white", bg="grey")
            lotp.place(x=50, y=150)
            self.eotp = Entry(self.frame2, show="*", font=("times new roman", 14, "bold"), bg='white', bd=1)
            self.eotp.place(x=50, y=200, width=250, height=35)

            uemailbtn = Button(self.frame2, text="Update", cursor='hand2', command=self.updateemail,
                               font=('times new roman', 16, 'bold'), bg='white', fg='black', bd=0)
            uemailbtn.place(x=200, y=300, width=75, height=35)

    def updateemail(self):
        if self.eotp.get() != self.EOTP:
            messagebox.showerror("Error", "Enter Valid OTP", parent=self.Frame1)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()
                cur.execute('UPDATE company SET email = %s WHERE org_id = %s',
                            (self.nemail.get(), self.org_id))
                cur.execute('UPDATE companylogin SET email = %s WHERE org_id = %s',
                            (self.nemail.get(), self.org_id))
                con.commit()
                con.close()
                messagebox.showinfo("success", "Your Email is Updated", parent=self.Frame1)
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.Frame1)

    def uphone(self):
        self.frame2 = Frame(self.Frame1, bg="grey")
        self.frame2.place(x=300, y=50, height=450, width=700)

        nphone = Label(self.frame2, text="Enter new Contact Number:", font=('calibre', 14, 'bold'), fg="white",
                       bg="grey")
        nphone.place(x=50, y=50)
        self.nphone = Entry(self.frame2, font=("times new roman", 14, "bold"), bg='white', bd=1)
        self.nphone.place(x=50, y=100, width=250, height=35)

        vphonebtn = Button(self.frame2, text="Verify", cursor='hand2', command=self.verifyphone,
                           font=('times new roman', 16, 'bold'), bg='white', fg='black', bd=0)
        vphonebtn.place(x=350, y=100, width=75, height=35)

    def verifyphone(self):
        if len(self.nphone.get()) != 10:
            messagebox.showerror("Error", "Enter Valid Contact number", parent=self.Frame1)
        else:
            account_sid = 'ACf0c7a7d9bf207419dd15159acebaba47'
            auth_token = '010f2e2eec71e1263160ad11adc898ad'
            client = Client(account_sid, auth_token)
            self.SOTP = str(random.randint(1000, 9999))
            client.messages.create(body=self.SOTP, from_='+18044099875', to="+918169885344", )

            lotp = Label(self.frame2, text="Enter SMS OTP:", font=('calibre', 14, 'bold'),
                         fg="white", bg="grey")
            lotp.place(x=50, y=150)
            self.sotp = Entry(self.frame2, show="*", font=("times new roman", 14, "bold"), bg='white', bd=1)
            self.sotp.place(x=50, y=200, width=250, height=35)

            uphonebtn = Button(self.frame2, text="Update", cursor='hand2', command=self.updatephone,
                               font=('times new roman', 16, 'bold'), bg='white', fg='black', bd=0)
            uphonebtn.place(x=200, y=300, width=75, height=35)

    def updatephone(self):
        if self.sotp.get() != self.SOTP:
            messagebox.showerror("Error", "Enter Valid OTP", parent=self.Frame1)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()
                cur.execute('UPDATE company SET contact = %s WHERE org_id = %s',
                            (self.nphone.get(), self.org_id))
                con.commit()
                con.close()
                messagebox.showinfo("success", "Your Contact Number is Updated", parent=self.Frame1)
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.Frame1)

    def signout(self):
        self.root.destroy()


root = Tk()
CDashboard(root)
root.mainloop()
