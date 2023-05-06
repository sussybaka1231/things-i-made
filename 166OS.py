import os
import keyboard
import shutil


def usr_sel():
    print("""Welcome to the Boot Menu! Login as chad? (adminstrator)
            |-----------------------|
            | Yes (y)               |
            | No (n)                |
            |-----------------------|""")
    while True:
        if keyboard.is_pressed("y"):
            os.system("cls")
            print("Logged in as defaultusr!\n")
            print("Welcome to SmallOS, chad! type \"help\" for help on commands.\n")
            print("Changing directory to home...")
            os.chdir(f"{__file__}/../home")
            os.system("cls")
            print("Logged in as defaultusr!\n")
            print("Welcome to SmallOS, chad! type \"help\" for help on commands.\n")
            print("Changing directory to home... Done")

            def enter_cmd():
                usrcmd = input(
                    f"Working directory: {os.getcwd()}, enter command: ")
                if usrcmd.lower() == "help":
                    print("""---Help for all SmallOS commands---
mkdir - make a directory in the current working directory

dldir - delete a directory

read - read a file's contents

dwd - display current working directory

mkfile - make a file

dlfile - delete a file 

start - start an exe from your local machine

cd - change directory

---End of help for all SmallOS commands---
""")
                elif usrcmd.lower().startswith("mkdir"):
                    os.mkdir(usrcmd[5:])
                elif usrcmd.lower().startswith("mkfile"):
                    with open(usrcmd[6:], "w"):
                        pass
                elif usrcmd.lower() == "dwd":
                    print(os.getcwd())
                elif usrcmd.lower().startswith("read"):
                    with open(usrcmd[5:], "r+") as f:
                        print(f.read())
                elif usrcmd.lower().startswith("start"):
                    os.system(f"start {usrcmd[6:]}")
                elif usrcmd.lower().startswith("dldir"):
                    if not os.listdir(usrcmd[6:]):
                        if usrcmd[6:] == "home":
                            confirm_del_home = input("Hello, chad. It is dangerous to delete home/ directory. Do you wish to continue? (y/n): ")
                            if confirm_del_home.lower() == "y":
                                os.rmdir(usrcmd[6:])
                            elif confirm_del_home.lower() == "n":
                                print("Not deleting home directory.\n")
                            else:
                                print("Invalid option.\n")
                        else:
                            os.rmdir(usrcmd[6:])
                    else:
                        if usrcmd[6:] == "home":
                            confirm_del_home = input("Hello, chad. It is dangerous to delete home/ directory. Do you wish to continue? (y/n): ")
                            if confirm_del_home.lower() == "y":
                                os.rmdir(usrcmd[6:])
                                print("Operation successful!\n")
                            elif confirm_del_home.lower() == "n":
                                print("Not deleting home directory.\n")
                            else:
                                print("Invalid option.\n")
                        elif usrcmd.endswith(":/"):
                            print(
                                "Access denied.\n\nYou are trying to delete a tree.\n")
                        else:
                            shutil.rmtree(usrcmd[6:])
                elif usrcmd.lower().startswith("cd"):
                    os.chdir(usrcmd[3:])
                    print("Operation successful!\n")
                else:
                    print("Invalid command.\n")

                enter_cmd()
            enter_cmd()

        elif keyboard.is_pressed("n"):
            os.system("cls")
            print("Logged in as defaultusr!\n")
            print("Welcome to SmallOS, defaultusr! type \"help\" for help on commands.\n")
            print("Changing directory to home...")
            os.chdir(f"{__file__}/../home")
            os.system("cls")
            print("Logged in as defaultusr!\n")
            print("Welcome to SmallOS, defaultusr! type \"help\" for help on commands.\n")
            print("Changing directory to home... Done")

            def enter_cmd():
                usrcmd = input(
                    f"Working directory: {os.getcwd()}, enter command: ")
                if usrcmd.lower() == "help":
                    print("""---Help for all SmallOS commands---
mkdir - make a directory in the current working directory

dldir - delete a directory

read - read a file's contents

dwd - display current working directory

mkfile - make a file

dlfile - delete a file 

start - start an exe from your local machine

cd - change directory

---End of help for all SmallOS commands---
""")
                elif usrcmd.lower().startswith("mkdir"):
                    os.mkdir(usrcmd[5:])
                elif usrcmd.lower().startswith("mkfile"):
                    with open(usrcmd[6:], "w"):
                        pass
                elif usrcmd.lower() == "dwd":
                    print(os.getcwd())
                elif usrcmd.lower().startswith("read"):
                    with open(usrcmd[5:], "r+") as f:
                        print(f.read())
                elif usrcmd.lower().startswith("start"):
                    os.system(f"start {usrcmd[6:]}")
                elif usrcmd.lower().startswith("dldir"):
                    if not os.listdir(usrcmd[6:]):
                        if usrcmd[6:] == "home":
                            print(
                                "Access denied.\n\nYou are trying to delete home/ directory.\n")
                        else:
                            os.rmdir(usrcmd[6:])
                    else:
                        if usrcmd[6:] == "home":
                            print("Access denied.")
                        elif usrcmd.endswith(":/"):
                            print(
                                "Access denied.\n\nYou are trying to delete a tree.\n")
                        else:
                            shutil.rmtree(usrcmd[6:])
                elif usrcmd.lower().startswith("cd"):
                    os.chdir(usrcmd[3:])
                    print("Operation successful!\n")
                else:
                    print("Invalid command.\n")

                enter_cmd()
            enter_cmd()


usr_sel()
