# Create variables to hold total and count of inputs
total = 0
count = 0

# Create a variable and promt user to enter numbers, press -1 to exit
user_input = int(input("Please enter the numbers you would like to find the mean of, (Press -1 to exit):\n"))

# Create a while loop that increments user inputs and stores , do the same for the count
while user_input != -1:
    total += user_input
    count += 1

    # if condition is not met, keep promting user for input
    user_input = int(input("Please enter the next number (Press -1 to exit):\n"))

    # create and if statement, if condition is met, calculate the user input.
    if user_input == -1:
        average = count/total # Logical error will happen here - The right way would be, total/count
        print(average)
        break
        
   
