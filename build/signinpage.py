from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


# functionality part
def forget_pass():
    def change_password():
        if user_entry.get=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and confirm password are not matching', parent=window)
        else:
            con = pymysql.connect(user='root', password='tiger', host='localhost', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username',parent=window)
            else:
                query='Update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('change password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label=Label(window, text='RESET PASSWORD', font=('arial','18','bold'),bg='white',fg='Dimgrey')
    heading_label.place(x=480, y=60)

    userlabel = Label(window, text='username', font=('arial', '12', 'bold'), bg='white', fg='Dimgrey')
    userlabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, fg='Dimgrey', font=('arial' , 11, 'bold'), bd=0)
    user_entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='Dimgrey').place(x=470, y=180)

    passwordlabel = Label(window, text='New password', font=('arial', '12', 'bold'), bg='white', fg='Dimgrey')
    passwordlabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='Dimgrey', font=('arial', 11, 'bold'), bd=0)
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250,height=2,bg='Dimgrey').place(x=470, y=260)

    confirmpasslabel = Label(window, text='Confirm password', font=('arial', '12', 'bold'), bg='white', fg='Dimgrey')
    confirmpasslabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='Dimgrey', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='Dimgrey').place(x=470, y=340)



    submitButton = Button(window, text='submit',bd=0,bg='Dimgrey',fg='white',font=('Open Sans','16', 'bold'), width=19, cursor='hand2', activebackground='Dimgrey',activeforeground='white',command=change_password)
    submitButton.place(x=470, y=390)
    window.mainloop()
def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')

    else:
        try:
            con=pymysql.connect(user='root', password='tiger', host='localhost', database='userdata')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()

        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            login_window.destroy()
            import Homepage



def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


# GUI part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('Login page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                fg='DimGrey')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='DimGrey')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

Frame(login_window, width=250, height=2, bg='DimGrey').place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='DimGrey')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

Frame(login_window, width=250, height=2, bg='DimGrey').place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=800, y=253)

forgetButton = Button(login_window, text='Forgot password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yahei UI Light', 9, 'bold'), fg='DimGrey', activeforeground='DimGrey',command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='DimGrey', activeforeground='white', activebackground='DimGrey', cursor='hand2', bd=0, width=19,command=login_user)

loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='---------------OR---------------', font=('Open Sans', 16), fg='DimGrey',
                bg='white')
orLabel.place(x=583, y=400)

facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9), fg='DimGrey', bg='white')
signupLabel.place(x=590, y=500)

newaccountButton = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'), fg='blue',
                          bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                          command=signup_page)
newaccountButton.place(x=727, y=500)

login_window.mainloop()
