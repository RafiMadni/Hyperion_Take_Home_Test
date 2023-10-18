# Define function and prompt user to make a choice
def user_choice():
    print("Hi There and welcome to the calculator app!")
    print("Press 1 for calculations")
    print("Press 2 for calculations history")
    choice = input("Enter your choice now\n")
    return choice

# Define function, make neccesary calculations for input, add defensive programming - error handling for division by zero
def calculation():
    num1 = float(input("Please enter the first number\n "))
    operator = input("Enter the operator (+,-,*,/)\n ")
    num2 = float(input("Enter the second number\n"))

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":               
            result = num1 / num2  
        else:
            print("You have entered an invalid operator, please try again")
            return
        
        print(f"{num1}{operator}{num2} = {result}")

        with open("history.txt", "a") as file:  # create and append to history.txt
            file.write(f"{num1} {operator} {num2} = {result}\n")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Define function, read file and add defensive programming - FileNotFound
def history():
    try:
        with open("history.txt", "r") as file:
            history = file.read()
            if history.strip():  # check if file is empty
                print("Calculations History:")
                print(history)
            else:
                print("No previous calculations found")
    except FileNotFoundError:
        print("No previous calculations found")


# Create a loop to keep runnning the start of program - main, make it a try except block and use value error to handle incorrect values added for num1 and numb 2
while True:
    try:

        choice = user_choice()

        if choice == "1":
            calculation()
        elif choice == "2":
            history()
        else:
            print("You have entered an invalid option, please try again ")
   
    except ValueError:
        print("Incorrect value added, please add a number")