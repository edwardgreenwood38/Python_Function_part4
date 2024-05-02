
# Write a Python function called max_num()to find the Max of three numbers.
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(123, 2454, 67))

print("========================================================")



# Write a Python function called mult_list()  to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0] * mult_list(lst[1:])

print(mult_list([1,2,3,4,5,6,7,8,9,10]))

print("========================================================")


# Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    if len(s) == 0:
        return s
    else:
        return rev_string(s[1:]) + s[0]

print(rev_string("hello"))

print("========================================================")



# Write a Python function called num_within() to check whether a number falls in a given range.

# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False

def num_within(x, start, end):
    if x >= start and x <= end:
        return True 
    else:
        return False
    
print(num_within(7,2,4))

print("========================================================")

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    row = [1]
    y = [0]

    for x in range(n):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

pascal(4)

print("========================================================")