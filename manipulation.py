# Create required variable and promt user to enter a sentence
str_manip = input("Kindly enter a sentence for us to manipulate\n")
# use len() function to determine number of characters in string
str_length = len(str_manip)
print(str_length)

# Create variable and slice string to get the last letter
last_letter = str_manip[-1]
# create variable and use the  replace function to replace the last letter with desired character
occurence = str_manip.replace(last_letter, "@")
print(occurence)

# Create variable and slice the string to get desired chunk of letters to display
last_three_letters = str_manip[-3:]
print(last_three_letters)

# Create variable and slice to get required chunk
first_three_letters = str_manip[:3]
# Create variable and slice to get required chunk
last_two_letters = str_manip[-2:]
# Create final variable and use concatenation to join variables and print 
combined = first_three_letters + last_two_letters
print(combined)