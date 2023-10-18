# Create a variable list to store and append id nos to.
ID_List = []

# create a variable and promt user the to enter the number of students writing
num_of_students = int(input("How many students are writing the exam?\n"))

# Create a for loop that iterates, and prompts for the student ID numbers
for i in range(num_of_students):
    id = input("Please enter the student ID No:\n")
    # append the ids entered to the ID_list created  
    ID_List.append(id)

# open file to write and create the desired file
file = open("reg_form.txt", "w")

# Create a loop  that writes each id on a new line and adds a dotted line on a new line
for id in ID_List:
    file.write(id + "\n")
    file.write("." * 25 + "\n")

# close the file
file.close()    









    