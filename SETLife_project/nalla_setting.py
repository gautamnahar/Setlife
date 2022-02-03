import random
import smtplib
from tkinter import *
from tkinter import messagebox
import pymysql
from twilio.rest import Client


class Nalla_Setting:
    def setting(self, mainframe, user_id):
        self.userid = user_id

        con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
        cur = con.cursor()
        cur.execute("select * from nalla where user_id=%s", self.userid)
        results = cur.fetchall()
        self.fpass = results[0][2]
        con.close()

        self.Frame1 = Frame(mainframe, bg="white")
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
                cur.execute('UPDATE nalla SET password = %s WHERE user_id = %s',
                            (self.lnpass.get(), self.userid))
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
                cur.execute('UPDATE nalla SET email = %s WHERE user_id = %s',
                            (self.nemail.get(), self.userid))
                cur.execute('UPDATE nallaprofile SET emailid = %s WHERE userid = %s',
                            (self.nemail.get(), self.userid))
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
                cur.execute('UPDATE nallaprofile SET phone = %s WHERE userid = %s',
                            (self.nphone.get(), self.userid))
                con.commit()
                con.close()
                messagebox.showinfo("success", "Your Contact Number is Updated", parent=self.Frame1)
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.Frame1)
