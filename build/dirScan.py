from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, StringVar, filedialog, Listbox, END
import mysql.connector
import tlsh
import os 
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Path to frame 0")
def backbuttontoavgui3():
    window.destroy()
    import antivirusgui

def keep_file():
    malware_listbox.delete(0, END)

def select_path():
    global ASSETS_PATH
    output_path = filedialog.askdirectory()
    if output_path:
        
        ASSETS_PATH = Path(output_path)
        directory_path_var.set(str(ASSETS_PATH))
        directory_label.config(text=str(ASSETS_PATH))
        print("New directory path:", str(ASSETS_PATH))
        print("Directory path var:", directory_path_var.get())
        path_label = Label(window, text=str(ASSETS_PATH), bg="#FFFFFF", font=("Helvetica", 11), padx=2, pady=2, anchor="w")
        path_label.place(x=300, y=205)
    else:
        print("No directory selected")
        
cnx = mysql.connector.connect(user='root', password='tiger',
                              host='localhost',
                              database='threats')
cursor = cnx.cursor()
# Generate Tlsh value for a file
def generate_tlsh_value(file_path):
    with open(file_path, 'rb') as f:
        binary_data = f.read()
    return tlsh.hash(binary_data)

# Match the generated Tlsh value with the Tlsh value in the database
def match_tlsh_value(generated_tlsh):
    conn = mysql.connector.connect(user='root', password='tiger', host='localhost', database='threats')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hashes WHERE tlsh=?", (generated_tlsh,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return result[0]
    else:
        return None


mlist=[]
def scan_files():
    # Scanning files in the directory
        for file_path in ASSETS_PATH.glob("*"):
            # Check if file is not a directory
            if file_path.is_file():
                # Calculate the tlsh hash for the file
                with open(file_path, 'rb') as f:
                    data = f.read()
                    file_tlsh = tlsh.hash(data)
                
                # Check if the file's tlsh hash is in the malware list
                db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='threats')
                cursor = db.cursor()
                cursor.execute('SELECT * FROM hashes WHERE tlsh=%s', (file_tlsh,))
                malware_list = cursor.fetchall()
                
                if malware_list:
                    # The file is malware
                    mlist.append(file_path)
                    malware_listbox.insert(END, f"{file_path} is malware")
                    print(f"{file_path} is malware")
                else:
                    # The file is not malware
                    
                    #malware_listbox.insert(END, f"{file_path} is not malware")
                    print(f"{file_path} is not malware")
        
def delete_file():
    print("delete function called")
    for  i in range(len(mlist)):
        print(mlist[i])
        os.remove(mlist[i])
    malware_listbox.delete(0, END)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
directory_path_var = StringVar()
window.geometry("990x660")
window.configure(bg="#FFFFFF")

directory_label = Label(
    window,
    textvariable=directory_path_var,
    bg="#FFFFFF",
    font=("Helvetica", 11),
    padx=2,
    pady=2,
    anchor="w"
)
directory_label.place(x=300, y=200)


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=660,
    width=990,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

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
    command=backbuttontoavgui3,
    relief="flat"
)
button_1.place(
    x=105.0,
    y=67.0,
    width=39.0,
    height=35.0
)

malware_listbox = Listbox(canvas, bg="#FFFFFF", font=("Helvetica", 11), width=90, height=10)
malware_listbox.place(x=125, y=310)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
button_2.place(
    x=125.0,
    y=200.0,
    width=154.0,
    height=33.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=scan_files,
    relief="flat"
)
button_3.place(
    x=414.0,
    y=243.0,
    width=154.0,
    height=33.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=delete_file,
    relief="flat"
)
button_4.place(
    x=255.0,
    y=539.0,
    width=154.0,
    height=33.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=keep_file,
    relief="flat"
)
button_5.place(
    x=575.0,
    y=539.0,
    width=154.0,
    height=33.0
)
window.resizable(False, False)
window.mainloop()
