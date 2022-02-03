import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox, ttk
import pymysql


class NtoC:
    def frontpage(self, mainframe, userid):
        self.userid = userid

        self.Frame1 = Frame(mainframe, bg="white")
        self.Frame1.place(x=0, y=0, height=550, width=1020)

        self.comname = Entry(self.Frame1, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.comname.place(x=300, y=50, width=270, height=35)

        searchbtn = Button(self.Frame1, text="Search", cursor='hand2', command=self.searchcom,
                           font=('times new roman', 18, 'bold'), bg='light green', fg='white', bd=0)
        searchbtn.place(x=600, y=50, width=85, height=35)

    def searchcom(self):
        con = pymysql.connect(host='localhost', user='root', password='Mysql@123', database="set_life")
        cur = con.cursor()
        cur.execute('select * from company where name=%s', (self.comname.get()))
        row = cur.fetchone()
        con.close()
        if row == None:
            messagebox.showerror('Error', 'Such Company name not found!', parent=self.Frame1)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()
                cur.execute("select * from company where name=%s", self.comname.get())
                results = cur.fetchall()
                self.name = results[0][1]
                self.femail = results[0][2]
                self.fphone = results[0][3]
                self.frevenue = results[0][4]
                self.fdep = results[0][5]
                con.close()

                labelname = Label(self.Frame1, text="Name:", font=('calibre', 14, 'bold'), fg="red", bg="white")
                labelname.place(x=200, y=120)

                labelrev = Label(self.Frame1, text="Revenue:", font=('calibre', 14, 'bold'), fg="red", bg="white")
                labelrev.place(x=200, y=170)

                labeldep = Label(self.Frame1, text="Department:", font=('calibre', 14, 'bold'), fg="red", bg="white")
                labeldep.place(x=200, y=220)

                labelphone = Label(self.Frame1, text="Phone:", font=('calibre', 14, 'bold'), fg="red", bg="white")
                labelphone.place(x=200, y=270)

                labelmail = Label(self.Frame1, text="Email:", font=('calibre', 14, 'bold'), fg="red", bg="white")
                labelmail.place(x=200, y=320)

                self.labelname = Label(self.Frame1, text=self.name, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelname.place(x=400, y=120)

                self.labelname = Label(self.Frame1, text=self.frevenue, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelname.place(x=400, y=170)

                self.labelname = Label(self.Frame1, text=self.fdep, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelname.place(x=400, y=220)

                self.labelname = Label(self.Frame1, text=self.fphone, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelname.place(x=400, y=270)

                self.labelname = Label(self.Frame1, text=self.femail, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelname.place(x=400, y=320)

                self.applybtn = Button(self.Frame1, text="Apply", cursor='hand2', command=self.applyjob,
                                      font=('times new roman', 18, 'bold'), bg='light green', fg='white', bd=0)
                self.applybtn.place(x=370, y=370, width=75, height=40)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.Frame1)

    def applyjob(self):
        try:
            email_user = 'setlife.customercare@gmail.com'
            email_password = 'Setlife@123'
            email_send = self.femail

            subject = 'Resume'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi, here is an applicant resume, interested in applying in your company.'
            msg.attach(MIMEText(body, 'plain'))

            filename = 'myResume.pdf'
            attachment = open(filename, 'rb')

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)

            server.sendmail(email_user, email_send, text)
            server.quit()
            messagebox.showinfo("success", "Application sent successfully!", parent=self.Frame1)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.Frame1)
