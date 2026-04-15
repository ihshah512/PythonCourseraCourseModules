import csv


def main():
    writeToFile()

def writeToFile():

    name = input("Whats your name: ")
    home = input("where is your home? ")

    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"]) #dictWriter and reader help us to tie down specific coloumns
        writer.writerow({"name":name, "home":home})


main()
