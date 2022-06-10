from multiprocessing.reduction import recv_handle
import tkinter as tk
from tkinter import Button, Canvas, filedialog, Text
import os

# A simple gui that loads a workspace
# Allows user to select apps and files to run from the gui.
# saves previous apps used and runs them

# set up root 
root = tk.Tk()
apps = []
# default apps to use if no apps are added- default set by user manually
# Google Chrome Browser and VSCODE 
apps_default = ["C:/Program Files/Google/Chrome/Application/chrome.exe", "D:/VSCode/Microsoft VS Code/Code.exe" ]

# getting saved last used apps and running them
if os.path.isfile('save.txt'):
    with open('save.txt', "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        
# Functionality for loading an app - used in openFile button
def addApp():
    # filter out repeat selection
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    # append selected files to apps array for later execution
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        # attactch it to the screen
        label.pack()
    
# Runs apps in apps array 
def runApps():
    
    for app in apps:
        os.startfile(app)

# pack canvas

canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()

# pack frame 
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons
# Open File
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()
# run 
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# startup grab last used apps
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Save last used apps to file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')