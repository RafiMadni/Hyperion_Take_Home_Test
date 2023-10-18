# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax error: added parentheses to print statement
print("\n") # Syntax error:(Compilation/indentation error) corrected indentation and added parentheses.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Logical error: == changed to = as age_Str is being compared to "24 yeas old". years old removed.  
age = int(age_Str)  
print("I'm " + str(age) + " years old.") # Runtime error: concatenated string correctly by adding spaces and casted age to a string.
# Compilation error: Corrected indentation of entire block.

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # Logical error: years_from_now is being compared to the word "3", quotation marks removed. (Alternatively, we could have casted to an integer on a new line.)
total_years = age + years_from_now 

print("The total number of years: " + str(total_years)) # Runtime: concatenated string correctly, added parentheses, incorrect variable called, answer_years should be total_years, casted variable to a string.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 # Syntax error: Incorrect variable called, chaned to total_years and correct calculation added.

print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Runtime error: concatenated string correctly, added parentheses, and casted total months to a string.

#HINT, 330 months is the correct answer