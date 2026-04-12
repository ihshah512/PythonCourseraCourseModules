def main():
    #print_squre(10)
    #getNum()
    x = getNumElseBlock()
    print(f"x is :: {x}")
    getNumElseBlock()

def print_squre(size):
    for i in range(size):
       # for j in range(size):
       print("#"*size)
    #print()

def getNum():
    user_input = input("Insert number: ")
    try:
        x = int(user_input)
        print("number is: ", x)
    except ValueError:
        print(user_input, " is not an integer")

def getNumElseBlock():
    while True:
        try:
            return int(input("INSET THE NUMBER: "))

        except ValueError:
            print("x is not an integer")




main()
