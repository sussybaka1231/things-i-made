import os


def admin_off():
    os.system("net user administrator /active:no")


def admin_on():
    os.system("net user administrator /active:yes")


while True:
    yes_or_no = int(input("0 = turn admin off\n1 = turn admin on\n"))
    if yes_or_no == 0:
        admin_off()
    elif yes_or_no == 1:
        admin_on()
    else:
        print("Invalid option")
