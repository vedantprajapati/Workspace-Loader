#import tkinter lib for gui
import tkinter as tk
from tkinter import filedialog, Text
#let user use as application
import os

#holds the app structure
root = tk.Tk()
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]

def appAdd():

    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir ="/", title= "Select your file",
    filetypes = (("Executables","*.exe"),("All Files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame,text = app, fg= "blue", bg = "grey")
        label.pack()

def runApps():
    for app in apps:
            os.startfile(app)

#create a canvas
canvas = tk.Canvas(root,height=699, width = 700,bg = "#263D42")
canvas.pack()

#inner frame dimensions
frame = tk.Frame(root,bg="grey")
frame.place(relwidth =0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

#open specific files
openFile = tk.Button(root, text= "Open File", padx = 10,
                    pady = 5, fg = "white", bg = "grey" ,command=appAdd)
openFile.pack()

#run the apps
runApps = tk.Button(root, text="Run Apps!", padx=10,pady=5,fg="white",bg = "grey", command = runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

#draw mains screen
root.mainloop()

with open("save.txt", "w") as f:
        for app in apps:
            f.write(app + ",")