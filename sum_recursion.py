# define function
def sum_of_numbers(numbers, index_point):
    # base case: if the index_point is equal 0, return the value at the 0 index of the list.
    if index_point == 0:
        return numbers[0]
    else:
        # recursive case: add the value at the current index_point to the sum of the rest of the list.
        return numbers[index_point] + sum_of_numbers(numbers, index_point - 1)


# print and test result 1
result1 = sum_of_numbers([1, 4, 5, 3, 12, 16], 4)
print(result1)  # 25 (1 + 4 + 5 + 3 + 12)

# print and test result 2
result2 = sum_of_numbers([4, 3, 1, 5], 1)
print(result2)  # 7 (4 + 3)
