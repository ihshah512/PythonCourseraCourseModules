def main():
    fileToList()


#THIS FUNCTION WILL READ READ THE FILE AND APPEND THE CONTENTS OF FILE INTO A LIST

def fileToList():
    students = []

    with open("students.csv") as file:
        for line in file:
            name, city = line.rstrip().split(",")
            student = {"name": name, "city": city} #consice way of doing it
            #student["name"] = name #one way of doing
            #student["city"] = city #one way of doing
            students.append(student)
    #for student in sorted(students, key=lambda s: s["name"]):
    #    print(f"{student['name']} is in {student['city']}")

    print("SORTING BY USING LAMBDA FUNCTION AND USING IT AS KEY")
    def get_name(student):
        return student["name"]
    print("SORTED BY NAME \n")
    for student in sorted(students, key = get_name, reverse=False):
        print(f"{student['name']} is in {student['city']}")
    print("SORTED BY CITY \n")
    def get_city(student):
        return student["city"]
    for student in sorted(students, key=get_city, reverse=False):
        print(f"{student['name']} is living in {student['city']} ")

    print("SORTING BY USING LAMBDA FUNCTION AND USING IT AS KEY")

    print("SORTED BY NAME \n")
    for student in sorted(students, key=lambda student:student["name"]):
        print(f"{student['name']} is in {student['city']}")
    print()
    print("SORTED BY CITY \n")

    for student in sorted(students, key=lambda student:student["city"]):
        print(f"{student['name']} is living in {student['city']} ")


main()
