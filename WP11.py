# In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n:
# n! = n × (n - 1) × (n - 2) × ... × 3 × 2 × 1
# For example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# The value of 0! is 1, according to the convention for an empty product.
# Write a function factorial that takes an argument n (an integer) and that returns the factorial of n.
# The function raises the exception TypeError if the argument n is not an integer.
# The function raises the exception ValueError if the argument n is not a positive integer.
# For examples:
# >>> [(n, factorial(n)) for n in range(6)]
# [(0, 1),
#  (1, 1),
#  (2, 2),
#  (3, 6),
#  (4, 24),
#  (5, 120)]
# >>> factorial('3')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 33, in factorial
# TypeError: Not an integer
# >>> factorial(-2)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 36, in factorial
# ValueError: Not a positive integer

# hàm đệ quy tìm giai thừa của 1 số nguyên
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
    
# num =3;
# print("The factorial of", num, "is" , factorial(num));
# ***********************************************************
# B1. Tạo hàm giai thừa
def factorial(x):
    if x==1:
        return 1
    if x <= 0:
        raise ValueError("Argument must be a positive integer")
    return(x*factorial(x-1))
# B2. Tạo hàm input giá trị x
def input_x():
    while True:
        try:
            x = int(input("Please enter a positive integer for computing its factorial: "))
            if x <= 0:
                raise ValueError("The value must be a positive integer")
            break
        except ValueError as error:
            print(error)
    return x

# B3.  Gán x= giá trị hàm inpur_X, in ra kq
x = input_x()
print(f"The factorial of {x} is {factorial(x)}")

