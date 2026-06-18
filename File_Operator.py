import os
from sys import exit
from datetime import datetime

ENTRY_DATA = "PR-6-_File_Operator/data.txt"


class Entry:
    def init(self):
        pass

    def adding_entry():
        print("-------------------------")
        print("Enter your diary entry below")
        d_entry = input().strip
        date = datetime.now()
        data.append([date, d_entry])
        try:
            with open(ENTRY_DATA, "a") as f:
                f.write(date + "\n")
                f.write(d_entry + "\n")
            print("The Entry is Successfully Added")
        except FileNotFoundError or PermissionError:
            f = open(ENTRY_DATA, "w")
            print("The Data is not perfectly added please try again later!!")

    def view_entry():
        print("------------------------")
        if data:
            try:
                for index, items in enumerate(data, start=1):
                    print(f"{index}.\n  {items[0]}\n  {items[1]}")
            except IndexError:
                print("Please delete all entry and rewrite it!")
        else:
            print("There is not a single entry!")

    def check_entry():
        print("----------------------")
        flag = False
        if data:
            try:
                print("Enter the diary entry to check below : ")
                check = input()
                for index, item in enumerate(data, start=1):
                    if check in item[1]:
                        print(f"{index}.\n  {item[0]}\n  {item[1]}")
                        flag = True
                if not flag:
                    print("There is no such thing!!")
            except IndexError:
                print("Retry this or delete all the entry!")

    def del_entry():
        print("----------------------")
        try:
            if data:
                data = []
                with open(ENTRY_DATA, "w") as f:
                    pass
                print("The data completely removed!")
            else:
                print("there no such data in this")
        except:
            print("Try again later")


def load_data():
    global data
    data = []
    temps = []
    if os.path.exists(ENTRY_DATA):
        try:
            with open(ENTRY_DATA, "r") as f:
                for line_num, line in enumerate(f, start=1):
                    if line_num % 2 == 1 and line:
                        temps.append(line)
                    elif line and line_num % 2 == 1:
                        temps.append(line)
                        data.append(temps)
                        temps = []
        except PermissionError or FileNotFoundError:
            f = open(ENTRY_DATA, "w")
    else:
        try:
            f = open(ENTRY_DATA, "x")
        except PermissionError or FileExistsError:
            f = open(ENTRY_DATA, "w")


def show():
    print("-----------------------------------")
    print("| Welcome to Personal Diary Entry |")
    print("-----------------------------------\n")

    print("-------Entry Menu-------")
    print("1. Add the new Entry")
    print("2. View all Entry")
    print("3. Search for an Entry")
    print("4. Delete all the Entries")
    print("5. Exit")

    choice = input("Enter the choice : ")

    return choice


def main():
    load_data()
    ch = show()
    dataentry = Entry()

    match ch:

        case "1":
            dataentry.adding_entry()

        case "2":
            dataentry.view_entry()

        case "3":
            dataentry.check_entry()

        case "4":
            dataentry.del_entry()

        case "5":
            print("Thank you for this!")
            exit()
