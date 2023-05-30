# Waypoint 5: Filter List of Integers
# Write a function filter_integers_greater_than that takes two arguments l (a list of integers) and n (an integer), 
# and returns a list of integers, taken from the initial list l, greater than n.
# >>> l = [0, 3, 5, -2, 9, 8]
# >>> filter_integers_greater_than(l, 4)
# [5, 9, 8]
# >>> filter_integers_greater_than(l, 6)
# [9, 8]

# B1. Tạo hàm nhập giá trị integer vào list l.
# Tạo vòng lặp input giá trị, nếu ấn E thì thoát.
# Tạo đk ràng buộc nếu giá trị nhập vào không phải integer
def input_integers():
    integers = []
    while True:
        try:
            value = input("Enter an integer (or 'E' to exit): ")
            if value.upper() == 'E':
                break
            integer = int(value)
            integers.append(integer)
        except ValueError:
            print("Invalid input, enter an integer again.")
            continue
    return integers
l = input_integers()
print(l)

# B2 Tạo hàm nhập giá trị integer n. tạo đk ràng buộc nếu nhập n ko là integer
def input_n():
    while True:
        try:
            n = input("Enter an integer n (or 'E' to exit): ")
            if n.upper() == 'E':
                break
            n = int(n)
        except ValueError:
            print("Invalid input, enter an integer again.")
        else:
            return n
    return None
n = input_n()
print(n)

# B3. Tạo hàm filter_integers_greater_than có 2 arguments l,n.
# hàm kiểm tra các giá trị trong list l, nếu >n thì append vào result 1 list các giá trị > n 
def filter_integers_greater_than(l, n):
    return [i for i in l if i > n]
result = filter_integers_greater_than(l, n)

# B4. In hàm
print(f"filter_integers_greater_than {l, n} is: " + str(result))













# *********************************************************************
# def input_decorator(func):
#     def input_integers():
#         l = []
# # tạo vòng lặp nhập giá trị integer và thêm vào list l, ấn E để thoát
#         while True:
#             try:
#                 value = input("Enter an integer (or 'E' to exit): ")
#                 if value.upper() == 'E':
#                     break
#                 integer = int(value)
#                 l.append(integer)
#             except ValueError:
#                 print("Invalid input, enter an integer again.")
#                 continue
#         return func(l)
#     l = input_integers(func())
# l = input_integers()

# def input_n():
#     while True:
#         try:
#             n = input("Enter an integer  n (or 'E' to exit): ")
#             if n.upper() == 'E':
#                 break
#             n = int(n)
#         except ValueError:
#             print("Invalid input, enter an integer again.")
#         return n

# @input_decorator
# def filter_integers_greater_than(l, n):
#     return [i for i in l if i > n]


# result = filter_integers_greater_than(l, n)
# print(f"filter_integers_greater_than {l, n} is: " + str(result))

#Sử dụng hàm decorator
# def input_decorator(func):
#     def inner():
#         name = input("Enter your name: ")
#         return func(name)
#     return inner

# @input_decorator
# def say_hello(name):
#     return f"Hello {name} !"

# print(say_hello())