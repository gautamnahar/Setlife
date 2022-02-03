import smtplib
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox, ttk
import pymysql


class CtoN:
    def frontpage(self, mainframe, orgid):
        self.userid = orgid

        my_canvas = Canvas(mainframe)
        my_canvas.place(x=0, y=0, height=550, width=1020)

        scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=my_canvas.yview)
        scrollbar.place(x=1000, y=0, height=550, width=20)

        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        self.second_frame = Frame(my_canvas, bg="white")

        my_canvas.create_window((0, 0), height=750, width=1020, window=self.second_frame, anchor="nw")

        btn1 = Button(self.second_frame, text="Create Meeting", cursor='hand2', command=self.createmeeting,
                      font=('times new roman', 18, 'bold'), bg='black', fg='white', bd=0)
        btn1.place(x=550, y=50, width=200, height=45)

        btn2 = Button(self.second_frame, text="Create Exam", cursor='hand2', command=self.createexam,
                      font=('times new roman', 18, 'bold'), bg='black', fg='white', bd=0)
        btn2.place(x=250, y=50, width=150, height=45)

        self.nallaid = Entry(self.second_frame, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.nallaid.place(x=300, y=150, width=270, height=35)

        searchbtn = Button(self.second_frame, text="Search", cursor='hand2', command=self.searchnalla,
                           font=('times new roman', 18, 'bold'), bg='light green', fg='white', bd=0)
        searchbtn.place(x=600, y=150, width=85, height=35)

    def createmeeting(self):
        webbrowser.open("https://meet.google.com/wzf-dijc-fex")

    def createexam(self):
        webbrowser.open("https://docs.google.com/forms/u/0/")

    def searchnalla(self):
        con = pymysql.connect(host='localhost', user='root', password='Mysql@123', database="set_life")
        cur = con.cursor()
        cur.execute('select * from nallaprofile where userid=%s', (self.nallaid.get()))
        row = cur.fetchone()
        con.close()
        if row == None:
            messagebox.showerror('Error', 'Such Company name not found!', parent=self.second_frame)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()
                cur.execute("select * from nallaprofile where userid=%s", self.nallaid.get())
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
                labelname.place(x=200, y=220)

                labelskill = Label(self.second_frame, text="Skills:", font=('calibre', 14, 'bold'), fg="red",
                                   bg="white")
                labelskill.place(x=200, y=290)

                labeledu = Label(self.second_frame, text="Education:", font=('calibre', 14, 'bold'), fg="red",
                                 bg="white")
                labeledu.place(x=200, y=360)

                labelexp = Label(self.second_frame, text="Experience:", font=('calibre', 14, 'bold'), fg="red",
                                 bg="white")
                labelexp.place(x=200, y=430)

                labelpast = Label(self.second_frame, text="Past Performance:", font=('calibre', 14, 'bold'), fg="red",
                                  bg="white")
                labelpast.place(x=200, y=500)

                labelemail = Label(self.second_frame, text="Email_ID:", font=('calibre', 14, 'bold'), fg="red",
                                   bg="white")
                labelemail.place(x=200, y=570)

                labelphone = Label(self.second_frame, text="Contact:", font=('calibre', 14, 'bold'), fg="red",
                                   bg="white")
                labelphone.place(x=200, y=640)

                self.labelname = Label(self.second_frame, text=self.fname, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelname.place(x=400, y=220)

                self.labelskill = Label(self.second_frame, text=self.fskills, font=('calibre', 14, 'bold'), fg="black",
                                        bg="white")
                self.labelskill.place(x=400, y=290)

                self.labeledu = Label(self.second_frame, text=self.fedu, font=('calibre', 14, 'bold'), fg="black",
                                      bg="white")
                self.labeledu.place(x=400, y=360)

                self.labelexp = Label(self.second_frame, text=self.fexp, font=('calibre', 14, 'bold'), fg="black",
                                      bg="white")
                self.labelexp.place(x=400, y=430)

                self.labelpast = Label(self.second_frame, text=self.fpast, font=('calibre', 14, 'bold'), fg="black",
                                       bg="white")
                self.labelpast.place(x=400, y=500)

                self.labelemail = Label(self.second_frame, text=self.femail, font=('calibre', 14, 'bold'), fg="black",
                                        bg="white")
                self.labelemail.place(x=400, y=570)

                self.labelphone = Label(self.second_frame, text=self.fphone, font=('calibre', 14, 'bold'), fg="black",
                                        bg="white")
                self.labelphone.place(x=400, y=640)

                self.Givebtn = Button(self.second_frame, text="Hire", cursor='hand2', command=self.givejob,
                                      font=('times new roman', 18, 'bold'), bg='light green', fg='white', bd=0)
                self.Givebtn.place(x=370, y=710, width=75, height=40)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.second_frame)

    def givejob(self):
        try:
            email_user = 'setlife.customercare@gmail.com'
            email_password = 'Setlife@123'
            email_send = self.femail

            subject = 'Hiring Letter'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Congratulations, we have an interest in hiring you.'
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
            messagebox.showinfo("success", "Application sent successfully!", parent=self.second_frame)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.second_frame)
