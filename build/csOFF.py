

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def backbuttontoavgui():
    window.destroy()
    import antivirusgui

def alldir():
    window.destroy()
    import alldirScan

def dirscan():
    window.destroy()
    import dirScan

def cson():
    window.destroy()
    import csON
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Path to frame 2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=dirscan,
    relief="flat"
)
button_1.place(
    x=364.0,
    y=229.0,
    width=261.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=alldir,
    relief="flat"
)
button_2.place(
    x=364.0,
    y=299.0,
    width=261.0,
    height=29.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=cson,
    relief="flat"
)
button_3.place(
    x=364.0,
    y=369.0,
    width=261.0,
    height=29.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=backbuttontoavgui,
    relief="flat"
)
button_4.place(
    x=105.0,
    y=67.0,
    width=39.0,
    height=35.0
)
window.resizable(False, False)
window.mainloop()
