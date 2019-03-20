def collatz(number):
    try:
        while number != 1:
            if number % 2 == 0:
                print(number // 2)
                number = number // 2
            elif number % 2 == 1:
                print(number * 3 + 1)
                number = number * 3 + 1
    except ValueError:
        print("Error: That's not an integer.")
        return
def repeat():
    while True:
        try:
            chosenInteger = int(input("\nEnter an integer:  "))
            collatz(chosenInteger)
            keepGoing = input("\nDo you want to try another integer? (y/n):  ")
            if keepGoing == "y" or keepGoing == "Y":
                continue
            elif keepGoing == "n" or keepGoing == "N":
                print("Peace...")
                break
            else:
                print("I assume that means no. Peace...")
                break
        except ValueError:
            print("Error: That's not an integer.")
            return
print("Hello! Today we will explore the Collatz sequence...\n")
try:
    chosenInteger = int(input("Enter an integer:  "))
    collatz(chosenInteger)
    keepGoing = input("\nDo you want to try another integer? (y/n):  ")
    if keepGoing == "y" or keepGoing == "Y":
        repeat()
    elif keepGoing == "n" or keepGoing == "N":
        print("Peace...")
    else:
        print("I assume that means no. Peace...")
except ValueError:
    print("Error: That's not an integer.")
