# define function
def largest_number(numbers):
    # base case: if the list has only one number return it
    if len(numbers) == 1:
        return numbers[0]
    else:
        # recursive case: get first number in the list 
        first_number = numbers[0]
        list_of_numbers = numbers[1:]  # create a new list with the rest of the numbers
        largest_in_list = largest_number(list_of_numbers)  # recursive call to fine the largest numbers in the new list

        # compare first numbers witht the largest in list 
        if first_number > largest_in_list:
            return first_number   # return the first number if its the largest
        else:
            return largest_in_list  # return the largest number in the new list

# print result 1 and test
result1 = largest_number([1,4,5,3])
print(result1)

# print result 2 and test    
result2 = largest_number([3,1,6,8,2,4,5])
print(result2)
