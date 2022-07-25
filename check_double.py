"""
Problem Statement

Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

    The number and its double should have exactly the same number of digits.

    Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
"""
# code



def check_double(number):
    num_list = list(str(number))
    num_list.sort()
    num2_list = list(str(2*number))
    num2_list.sort()
    if int("".join(num_list)) == int("".join(num2_list)):
        return True
    return False

#Provide different values for number and test your program
print(check_double(125874))
