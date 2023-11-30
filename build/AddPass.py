import base64
import pymysql

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

def backbuttontopassman():
    window.destroy()
    import passMan
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Path to frame 1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def encrypt_password(password, key):
    password = password.encode()
    cipher = Fernet(key)
    ct = cipher.encrypt(password)
    return base64.b64encode(ct).decode()

def add_password(service, username, password):
    if not service or not username:
        output_label.config(text="Service and username fields are required.")
    elif not password:
        output_label.config(text="Password field is required.")
    else:
        cnx = pymysql.connect(user='root', password='tiger', host='localhost', database='passman')
        cursor = cnx.cursor()
        get_password_query = ("SELECT COUNT(*) FROM passwords WHERE service=%s AND username=%s")
        get_password_data = (service, username)
        cursor.execute(get_password_query, get_password_data)
        count = cursor.fetchone()[0]
        if count > 0:
            output_label.config(text="Password already exists for this service and username.")
        else:
            key = Fernet.generate_key()
            hashed_password = encrypt_password(password, key)
            add_password_query = ("INSERT INTO passwords (service, username, password, `key`) VALUES (%s, %s, %s, %s)")
            add_password_data = (service, username, hashed_password, key)
            cursor.execute(add_password_query, add_password_data)
            cnx.commit()
            output_label.config(text="Password added successfully.")
        cursor.close()
        cnx.close()


def add_password_to_db():
    service = entry_1.get()
    username = entry_2.get()
    password = entry_3.get()
    add_password(service, username, password)

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
    304.5,
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
    y=290.0,
    width=241.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    621.5,
    358.5,
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
    y=344.0,
    width=241.0,
    height=27.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    621.5,
    412.5,
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
    y=398.0,
    width=241.0,
    height=27.0
)

canvas.create_text(
    342.0,
    295.0,
    anchor="nw",
    text="Service",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    342.0,
    352.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    342.0,
    409.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_password_to_db,
    relief="flat"
)
button_1.place(
    x=402.0,
    y=478.0,
    width=178.0,
    height=36.0
)


output_label = Label(
    text="",
    font=("Inter", 12),
    bg="#FFFFFF",
    fg="#000000"
)
output_label.place(
    x=350,
    y=550
)



canvas.create_text(
    426.0,
    234.0,
    anchor="nw",
    text="Add Password",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=backbuttontopassman,
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
