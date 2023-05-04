from tkinter import *
import os

root = Tk()
root.title("Git Client")
if os.path.exists("C:/Program Files/Git"):
    def clone_repo():
        os.system()
    button = Button(text="Clone Repo", font=("consolas", 30))
    button.pack()
else:
    git_warning = Label(
        text="Git is not installed, Installing Git...", font=("consolas", 30))
    git_warning.pack()
    root.after(1000, os.system("winget install git"))
root.mainloop()
