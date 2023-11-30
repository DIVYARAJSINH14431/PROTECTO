
import base64
import pymysql

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
def backbuttontopassman1():
    window.destroy()
    import passMan

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Path to frame 4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def delete_password(service, username):
    cnx = pymysql.connect(user='root', password='tiger', host='localhost', database='passman')
    cursor = cnx.cursor()
    delete_password_query = ("DELETE FROM passwords "
                          "WHERE service=%s AND username=%s")
    delete_password_data = (service, username)
    cursor.execute(delete_password_query, delete_password_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Password deleted successfully!")
    success_label = Label(window, text="Password deleted successfully!")
    success_label.place(x=400, y=540)

def del_pass():
    service= entry_1.get()
    username= entry_2.get()
    delete_password(service,username)
window = Tk()

window.geometry("990x660")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 660,
    width = 990,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    495.0,
    330.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    491.0,
    127.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    621.5,
    303.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=501.0,
    y=289.0,
    width=241.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    621.5,
    357.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=501.0,
    y=343.0,
    width=241.0,
    height=27.0
)

canvas.create_text(
    342.0,
    294.0,
    anchor="nw",
    text="Service",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    342.0,
    351.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inter", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=del_pass,
    relief="flat"
)
button_1.place(
    x=402.0,
    y=484.0,
    width=178.0,
    height=36.0
)

canvas.create_text(
    411.0,
    206.0,
    anchor="nw",
    text="Delete Password",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    621.5,
    409.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=501.0,
    y=395.0,
    width=241.0,
    height=27.0
)

canvas.create_text(
    342.0,
    406.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=backbuttontopassman1,
    relief="flat"
)
button_2.place(
    x=104.0,
    y=65.0,
    width=39.0,
    height=35.0
)
window.resizable(False, False)
window.mainloop()
