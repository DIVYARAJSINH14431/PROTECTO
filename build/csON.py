import tlsh 
from pathlib import Path
import os
from tkinter import Tk, Canvas, Button, PhotoImage
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Path to frame 3")
cnx = mysql.connector.connect(user='root', password='tiger', host='localhost', database='threats')
cursor = cnx.cursor()
def backbuttontoavgui2():
    window.destroy()
    import antivirusgui

def alldir():
    window.destroy()
    import alldirScan

def dirscan():
    window.destroy()
    import dirScan

def csoff():
    window.destroy()
    import csOFF


def match_tlsh_value(generated_tlsh):
    # Fetch the file name from the database where tlsh value matches
    query = 'SELECT file_name FROM data WHERE tlsh = %s'
    cursor.execute(query, (generated_tlsh,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def delete_file(file_path):
    os.remove(file_path)

def scan_all_directories():
    for root in ['/']:
        for dirpath, dirnames, filenames in os.walk(root):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                generated_tlsh = tlsh.hash(open(file_path, 'rb').read())
                matched_file_name = match_tlsh_value(generated_tlsh)
                if matched_file_name:
                    print(f'The file "{file_path}" has virus.')
                    button_3.config(command=lambda: delete_file(file_path))
                    button_4.config(command=lambda: print(f'The file "{file_path}" has not been deleted.'))
                else:
                    button_3.config(command=lambda: print('No virus found.'))
                    button_4.config(command=lambda: print('No virus found.'))

    # Close the database connection
    cursor.close()
    cnx.close()


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
    command=csoff,
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
    command=backbuttontoavgui2,
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
