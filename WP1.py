# Waypoint 1: Say Greeting
# Write a function hello that takes one argument name (a string) and that returns a string composed of 'Hello ' 
# concatenated with the argument name and concatenated with the character '!'.

# B1. Tạo hàm get_name để input  tên. đặt điều kiện ràng buộc dữ liệu nhập vào dạng string.
# Tạo vòng lặp cho tới khi nhập đúng dạng string

def get_name():
    while True:
        name = input("Enter your name: ")
        name = name.strip().upper()
        try:
            int(name)
            print("Please enter a valid name (not a number)")
        except ValueError:
            return name
# B2. Tạo hàm say_hello, khi nhập name thì sẽ trả về câu Hello +name !
def say_hello(name):
    return f"Hello {name}!"
# B3. Gán giá trị của name bằng hàm get_name(). in ra hàm say_hello(name)
name = get_name()
print(say_hello(name))



# #Sử dụng hàm decorator
# def input_decorator(func):
#     def inner():
#         while True:
#             name = input("Enter your name: ")
#             name = name.strip().upper()
#             try:
#                 int(name)
#                 print("Please enter a valid name (not a number)")
#             except ValueError:
#                 return func(name)
#     return inner

# @input_decorator
# def say_hello(name):
#     return f"Hello {name} !"

# print(say_hello())