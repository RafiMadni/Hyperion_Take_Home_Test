# Import the regular expression module
import re

# Define a function called tokenize with the input expression as a parameter
def tokenize(expression):
    # Use the re.findall function to extract and serach for tokens with the regular expression pattern 
    # for operators, decimals, and integers
    tokens = re.findall(r'[-+*/()]|\d+\.\d+|\d+', expression)
    # Return the list of tokens
    return tokens

# Define a function to evaluate the expression
def evaluate_expression(tokens):
    # Base case: if there's only one token, return it
    # we use it to handle simple expressons where no evaluation is needed
    if len(tokens) == 1:
        return tokens[0]

    # now we start by handling the parenthesis
    # we checking for open parenthesis in the tokens 
    # we store its index using the .index function (open_index variable used)
    # then we initialise close_index to one position after the open_index  
    # we add a count to track our matching open parenthesis with a closed parenthsis,
    # if the count is greater than 0 we not balanced corretly  
    if '(' in tokens:
        open_idx = tokens.index('(')
        close_idx = open_idx + 1
        count = 1

        # Find the matching closing parenthesis
        while count > 0 and close_idx < len(tokens):
            # we check if there is a nested open parenthesis, if true our count +1
            if tokens[close_idx] == '(':
                count += 1
            # we check for a close parenthesis, if true our count decrements - a matching open parenthesis has been found    
            elif tokens[close_idx] == ')':
                count -= 1
            # after checking the current token we incremt our close index to move on to the next token in the list
            close_idx += 1
            #This loop essentially iterates through the tokens list, 
            # counting open and close parentheses to find the position of the matching closing parenthesis for a given open parenthesis.
            #  It ensures that nested parentheses are correctly matched

        # If the open parenthesis is unmatched, return an "Invalid Expression" message
        if count != 0:
            return "Invalid Expression"

        # Recursively evaluate the expression within the parentheses
        # slices the tokens list to get the subexpression between the open and close parentheses, 
        # excluding the parentheses themselves.
        result_in_parentheses = evaluate_expression(tokens[open_idx + 1:close_idx - 1]) # 1 and 3 - not 0 and 4()

        # Replace the expression in parentheses with the result
        # effectively 2 * (3 + 4) * 5 == 2 * 7 * 5
        tokens = tokens[:open_idx] + [result_in_parentheses] + tokens[close_idx:]

        # Continue evaluating the modified tokens list and return the result of the entire expression 
        return evaluate_expression(tokens) # eg is == 70

    # Initialize a counter variable and an index variable
    # we make sure to start at the 0 index
    i = 0

    # Loop to handle multiplication and division
    while i < len(tokens):
        # we specifically looking for either multiplication and division 
        # here we storing the value before the operator and after the operator and the operatoor
        if tokens[i] in ['*', '/']:
            left_operand = tokens[i - 1]
            right_operand = tokens[i + 1]
            # i is the operator
            operator = tokens[i]

            # Check if both operands are valid numbers (digits or decimals) 
            # here we replace the period with an empty string at the first occurence
            # we use the isdigit function to check if the remainig values after removing the decimals are valid numbers
            if not (left_operand.replace('.', '', 1).isdigit() and right_operand.replace('.', '', 1).isdigit()):
                return "Invalid Expression"

            # Perform the multiplication or division and store the result as a string
            if operator == '*':
                # here we multiply  L * R, convert to a float and convert back to a string
                result = str(float(left_operand) * float(right_operand))
            elif operator == '/':
                # here we handled a dvision by zero error
                if float(right_operand) == 0:
                    return "Division by zero"
                result = str(float(left_operand) / float(right_operand))

            # Update the tokens list with the result
            # here we take a slice from the list, everything from the left of the operator, i -1
            # and everthing from the right of the operator i + 2
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
        # here we handle tokens that are not operators,
        # we iterate through tokens to check for operators or numbers(operand)
        # if its not an operator it falls in this else block, it increments, meaning we move
        # on to the next token. this     
        else:
            i += 1

    # # Initialize a counter variable and an index variable
    # we make sure to start at the 0 index
    i = 0

    # Loop to handle addition and subtraction
    while i < len(tokens):
        if tokens[i] in ['+', '-']:
        # we specifically looking for either addition and subtraction 
        # here we storing the value before the operator and after the operator and the operatoor
            left_operand = tokens[i - 1]
            right_operand = tokens[i + 1]
            operator = tokens[i]

            # Check if both operands are valid numbers (digits or decimals) 
            # here we replace the period with an empty string at the first occurence
            # we use the isdigit function to check if the remainig values after removing the decimals are valid numbers
            if not (left_operand.replace('.', '', 1).isdigit() and right_operand.replace('.', '', 1).isdigit()):
                return "Invalid Expression"

            # Perform the addition or subtraction and store the result as a strin
            if operator == '+':
                # we calculate the result as a float and convert to a string
                result = str(float(left_operand) + float(right_operand))
            elif operator == '-':
                result = str(float(left_operand) - float(right_operand))

            # Update the tokens list with the result
            # here we take a slice from the list, everything from the left of the operator, i -1
            # and everthing from the right of the operator i + 2
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]

        # here we handle tokens that are not operators,
        # we iterate through tokens to check for operators or numbers(operand)
        # if its not an operator it falls in this else block, it increments, meaning we move
        # on to the next token
        else:
            i += 1

    # The final result should be the only remaining token
    # here we check again if there is more then one token in the list, we return an error invalid expression
    if len(tokens) == 1:
        return tokens[0]
    else:
        return "Invalid Expression"

# we create a function that takes an expression as its paramenter,
# then we tokenize the expresssion calling the tokenize function and passing the expression it in its parameter
# then we evalaute the tokens by passing the tokens list in the evaluate_expression function
# here it recursively process the list and () and operators
def evaluate_alg_expression(expression):
    # Tokenize the input expression
    tokens = tokenize(expression)
    # Return the result of evaluating the expression
    return evaluate_expression(tokens)

# Test cases
print(evaluate_alg_expression("7 + 5")) # example of a simple expression
print(evaluate_alg_expression("3 + 12 * 3 / 12"))  # Should print "6.0"
print(evaluate_alg_expression("(3 + 3) * 42 / (6 + 12)"))  # Should print "14.0"
print(evaluate_alg_expression("4 (12E)"))  # Should print "Invalid Expression"
print(evaluate_alg_expression("4 (41)"))  # Should print "Invalid Expression"
print(evaluate_alg_expression("42+43**271"))  # Should print "Invalid Expression"
