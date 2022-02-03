import random
import smtplib
from tkinter import *
from tkinter import messagebox
import pymysql
from twilio.rest import Client
from ttkthemes import themed_tk as tk


class Nalla:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.loginform()

    def loginform(self):
        self.root.geometry("350x400+450+100")
        self.root.resizable(False, False)

        Frame_login = Frame(self.root, bg="orange")
        Frame_login.place(x=0, y=0, height=700, width=1366)

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=10, y=10, height=380, width=330)

        label2 = Label(frame_input, text="Username or Email", font=('Goody old style', 18, 'bold'), fg="orange",
                       bg="white")
        label2.place(x=30, y=45)
        self.username_txt = Entry(frame_input, font=("times new roman", 16, "bold"), bg='white', bd=2)
        self.username_txt.place(x=30, y=95, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=('Goody old style', 18, 'bold'), fg="orange", bg="white")
        label3.place(x=30, y=145)
        self.password = Entry(frame_input, show="*", font=("Goody old style", 16, "bold"), bg='white', bd=2)
        self.password.place(x=30, y=195, width=270, height=35)

        btn1 = Button(frame_input, text="forgot password?", cursor='hand2', font=('calibre', 10), bg='white',
                      fg='black', bd=0)
        btn1.place(x=125, y=255)

        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2", font=('times new roman', 15),
                      bg='orange', fg='white', bd=0, width=15, height=1)
        btn2.place(x=90, y=290)

        btn3 = Button(frame_input, text="Not Registered? register", command=self.Register, cursor='hand2',
                      font=('calibre', 10), bg='white', fg='black', bd=0)
        btn3.place(x=110, y=340)

        btn4 = Button(self.root, text="Back", command=root.destroy, cursor='hand2', font=('calibre', 12),
                      bg='orange', fg='white', bd=0)
        btn4.place(x=300, y=0, height='30', width='50')

    def login(self):
        if self.username_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                self.userid = self.username_txt.get()
                con = pymysql.connect(host='localhost', user='root', password='Mysql@123', database="set_life")
                cur = con.cursor()
                cur.execute('select * from nalla where (user_id=%s or email=%s) and password=%s',
                            (self.username_txt.get(), self.username_txt.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Username or Password!', parent=self.root)
                else:
                    messagebox.showinfo('Success', 'Login Successful', parent=self.root)
                    self.Nalla_dashboard()
                    con.close()
            except Exception as es:
                messagebox.showerror('Error', f'Error Due to :{str(es)}', parent=self.root)

    def Nalla_dashboard(self):
        print("hello")

    def Register(self):
        self.root.geometry("650x550+300+100")
        self.root.resizable(True, True)

        Frame_login1 = Frame(self.root, bg="light green")
        Frame_login1.place(x=0, y=0, height=550, width=650)

        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=10, y=10, height=530, width=630)

        label2 = Label(frame_input2, text="Username", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label2.place(x=30, y=25)
        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry.place(x=30, y=85, width=270, height=35)

        label3 = Label(frame_input2, text="Password", font=("Goody old style", 20, "bold"), fg='light green',
                       bg="white")
        label3.place(x=30, y=145)
        self.entry2 = Entry(frame_input2, show="*", font=("Goody old style", 20, "bold"), bg='white', bd=2)
        self.entry2.place(x=30, y=195, width=270, height=35)

        label4 = Label(frame_input2, text="Full Name", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label4.place(x=330, y=25)
        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry3.place(x=330, y=85, width=270, height=35)

        label5 = Label(frame_input2, text="Confirm Password", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label5.place(x=330, y=145)
        self.entry4 = Entry(frame_input2, show="*", font=("Goody old style", 20, "bold"), bg='white', bd=2)
        self.entry4.place(x=330, y=195, width=270, height=35)

        label5 = Label(frame_input2, text="Contact Number", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label5.place(x=30, y=245)
        self.entry5 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry5.place(x=30, y=295, width=270, height=35)

        label6 = Label(frame_input2, text="Email", font=("Goody old style", 20, "bold"), fg='light green',
                       bg='white')
        label6.place(x=330, y=245)
        self.entry6 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='white', bd=2)
        self.entry6.place(x=330, y=295, width=270, height=35)

        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        btn2.place(x=330, y=440)

        btn4 = Button(frame_input2, command=self.verification, text="Verify", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="light green", bd=0, width=15, height=1)
        btn4.place(x=130, y=440)

        btn3 = Button(frame_input2, command=self.loginform, text="already register ? login", cursor="hand2",
                      font=("calibre", 10), fg="black", bg="white", bd=0)
        btn3.place(x=260, y=490)

        label7 = Label(frame_input2, text="Note: PLEASE DON'T REGISTER BEFORE VERIFICATION", font=("Arial", 14, "bold"),
                       fg='red', bg='white')
        label7.place(x=60, y=510)

    def verification(self):
        if len(self.entry5.get()) != 10:
            messagebox.showerror("Error", "Enter Valid Contact number", parent=self.root)
        elif self.entry6.get() == "":
            messagebox.showerror("Error", "Please Enter a Email-ID", parent=self.root)
        else:
            o = smtplib.SMTP("smtp.gmail.com", 587)
            o.starttls()
            o.login("setlife.customercare@gmail.com", "Setlife@123")
            self.OTPE = random.randint(1000, 9999)
            message = "Your otp for registration is " + str(self.OTPE)
            listOfAddress = [self.entry6.get()]
            o.sendmail("setlife.customercare@gmail.com", listOfAddress, message)
            o.quit()

            account_sid = 'ACf0c7a7d9bf207419dd15159acebaba47'
            auth_token = '010f2e2eec71e1263160ad11adc898ad'
            client = Client(account_sid, auth_token)
            self.OTPS = str(random.randint(1000, 9999))
            client.messages.create(body=self.OTPS, from_='+18044099875', to="+918169885344", )

            label8 = Label(root, text="Enter sms OTP", font=("Calibre", 12, "bold"),
                           fg='light green', bg='white')
            label8.place(x=40, y=355)
            self.otps = Entry(root, font=("times new roman", 15, "bold"), bg='white', bd=2)
            self.otps.place(x=40, y=405, width=150, height=35)

            label9 = Label(root, text="Enter mailed OTP", font=("Calibre", 12, "bold"),
                           fg='light green', bg='white')
            label9.place(x=330, y=355)
            self.otpe = Entry(root, font=("times new roman", 15, "bold"), bg='white', bd=2)
            self.otpe.place(x=340, y=405, width=150, height=35)

    def register(self):
        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "" \
                or self.entry5.get() == "" or self.entry6.get() == "":
            messagebox.showerror("Error", "All Field Are Required", parent=self.root)

        elif self.entry2.get() != self.entry4.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.root)

        elif self.otpe.get() != self.OTPE and self.otps.get() != self.OTPS:
            messagebox.showerror("Error", "Enter Valid OTP", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="set_life")
                cur = con.cursor()
                cur.execute("select * from nalla where email=%s", self.entry6.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error user already exist ,please try with another Email", parent=self.root)
                else:
                    cur.execute("INSERT INTO nalla VALUES (%s,%s,%s)",
                                (self.entry.get(), self.entry6.get(), self.entry2.get()))
                    cur.execute("INSERT INTO nallaprofile (userid,name,phone,emailid) VALUES (%s,%s,%s,%s)",
                                (self.entry.get(), self.entry3.get(), self.entry5.get(), self.entry6.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("success", "Register Successful  Username:" + self.entry.get() +
                                        "Password" + self.entry2.get(), parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)


root = tk.ThemedTk()
root.get_themes()
root.set_theme("black")

ob = Nalla(root)
root.mainloop()
