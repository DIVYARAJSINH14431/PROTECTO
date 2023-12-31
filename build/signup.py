from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameLabel.delete(0,END)
    passwordLabel.delete(0,END)
    passwordLabel.delete(0,END)
    confirmLabel.delete(0,END)
    check.set(0)



def connect_database():
    if emailEntry.get() == '' or usernameLabel.get() == '' or passwordLabel.get() == '' or confirmLabel.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordLabel.get() != confirmLabel.get():
        messagebox.showerror('Error', 'Password must match!')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(user='root', password='tiger', host='localhost', database='userdata')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issue, please try again')
            return

        try:
            query = 'create database userdata;'
            mycursor.execute(query)
            query = 'use userdata;'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20));'

            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')
            query='select * from data where username=%s'
            mycursor.execute(query,(usernameLabel.get()))

            row=mycursor.fetchone()
            if row !=None:
                messagebox.showerror('Error', 'Username already exists')

            else:
                query = 'Insert into data(email,username,password) values(%s,%s,%s);'
            mycursor.execute(query, (emailEntry.get(), usernameLabel.get(), passwordLabel.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Database', "Registration is Successfull!")
            clear()
            signup_window.destroy()
            import  signinpage




def login_page():
    signup_window.destroy()
    import signinpage


signup_window = Tk()
signup_window.title('Signup page')
signup_window.resizable(False, False)

background = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white',
                fg='DimGrey')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='DimGrey')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='DimGrey')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='DimGrey')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
usernameLabel = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='DimGrey')
usernameLabel.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='DimGrey')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
passwordLabel = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='DimGrey')
passwordLabel.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                     fg='DimGrey')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
confirmLabel = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='DimGrey')
confirmLabel.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions',
                                 font=('Microsoft Yahei UI Light', 9, 'bold'), fg='DimGrey', bg='white',
                                 activebackground='white', activeforeground='DimGrey', cursor='hand2',
                                 variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=15)

signupButton = Button(frame, text='Signup', font=('Open Sans', 16, 'bold'), bd=0, bg='DimGrey', fg='white',
                      activebackground='DimGrey', activeforeground='white', width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'), bg='white',
                       fg='DimGrey')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), bg='white', fg='blue', bd=0,
                     cursor='hand2', activebackground='white', activeforeground='blue', command=login_page)
loginButton.place(x=170, y=404)

signup_window.mainloop()
