from fpdf import FPDF
from tkinter import messagebox
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkPDFViewer import tkPDFViewer as pdf


class NallaResume:
    def resume(self, userid, mainframe):
        self.mainframe = mainframe
        self.userid = userid

        my_pdf = FPDF()

        con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
        cur = con.cursor()
        cur.execute("select * from nallaprofile where userid=%s", self.userid)
        results = cur.fetchall()
        name = results[0][1]
        phone = results[0][2]
        self.email = results[0][3]
        edu = results[0][4]
        skill = results[0][5]
        past = results[0][6]
        exp = results[0][7]
        con.close()

        my_pdf.add_page()
        my_pdf.set_font("Arial", size=16)
        my_pdf.cell(200, 10, txt="My Resume", ln=1, align="C")

        text = (
                "Respected Sir/Madam,\n I am " + name)
        my_pdf.cell(200, 10, txt=text, ln=2, align="C")
        if skill != "":
            text = (". \nI have mastered " + skill)
            my_pdf.cell(200, 10, txt=text, ln=3, align="C")
        if edu != "":
            text = (" thoroughly .\ni have done my graduation in " + edu)
            my_pdf.cell(200, 10, txt=text, ln=4, align="C")
        if past != "":
            text = (". My Past Performance: " + past)
            my_pdf.cell(200, 10, txt=text, ln=5, align="C")

        text = ("\n . Yours Faithfully\n " + name)
        my_pdf.cell(200, 10, txt=text, ln=6, align="C")
        my_pdf.output("myResume.pdf")

        r1 = pdf.ShowPdf()
        r2 = r1.pdf_view(mainframe, pdf_location=r"myResume.pdf", width=80, height=50)
        r2.pack()

        res = messagebox.askquestion('Send Resume', 'Do you want your resume mailed?')
        if res == 'yes':
            self.sendresume()

    def sendresume(self):
        try:
            email_user = 'setlife.customercare@gmail.com'
            email_password = 'Setlife@123'
            email_send = self.email

            subject = 'Resume'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi, here is your resume'
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
            messagebox.showinfo("success", "Resume sent on registered email successfully!", parent=self.mainframe)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.mainframe)
