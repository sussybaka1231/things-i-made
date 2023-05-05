from tkinter import *
import os

root = Tk()
root.title("Git")
if os.path.exists("C:/Program Files/Git"):
    def main():
        def clone_repo():
            
            username_owner_label = Label(
                text="Enter username of the repo owner: ", font=("consolas", 30))
            username_owner_label.grid(
                row=1, column=0, padx=10, pady=10, sticky="w")
            username_owner_entry = Entry(root, font=("consolas", 30))
            username_owner_entry.grid(
                row=1, column=1, padx=10, pady=10, sticky="w")
            repo_name_label = Label(
                text="Enter name of the repo: ", font=("consolas", 30))
            repo_name_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            repo_name_entry = Entry(root, font=("consolas", 30))
            repo_name_entry.grid(row=3, column=1, padx=10, pady=10)
            username_user_label = Label(
                text="Enter GitHub username: ", font=("consolas", 30))
            username_user_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
            username_user_entry = Entry(root, font=("consolas", 30))
            username_user_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
            email_user_label = Label(
                text="Enter GitHub Email: ", font=("consolas", 30))
            email_user_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
            email_user_entry = Entry(root, font=("consolas", 30))
            email_user_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")
            clone_label = Label(text="Enter where to clone repo: ",
                                font=("consolas", 30))
            clone_label.grid(row=7, column=0, padx=10, pady=10)
            clone_entry = Entry(root, font=("consolas", 30))
            clone_entry.grid(row=7, column=1, padx=10, pady=10)

            def done():
                os.system("setx PATH \"%PATH%;C:\\Program Files\\Git\\bin\"")
                os.chdir(clone_entry.get())
                os.system(
                    f"git config --global user.name \"{username_user_entry.get()}\" && git config --global user.email \"{email_user_entry.get()}\" && git clone https://github.com/{username_owner_entry.get()}/{repo_name_entry.get()}.git")

            def cancel():
                clone_label.destroy()
                repo_name_label.destroy()
                email_user_label.destroy()
                username_user_label.destroy()
                username_owner_label.destroy()
                clone_entry.destroy()
                repo_name_entry.destroy()
                email_user_entry.destroy()
                username_user_entry.destroy()
                username_owner_entry.destroy()

        button = Button(text="Clone Repo", font=(
            "consolas", 30), command=clone_repo)
        button.grid(row=0, column=0, padx=10, pady=10)

else:
    git_warning = Label(
        text="Git is not installed, Installing Git...", font=("consolas", 30))
    git_warning.pack()
    root.after(1000, os.system("winget install git"))
root.mainloop()
