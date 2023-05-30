# Waypoint 4: Test whether at least one Condition is True
# Write a function is_a_condition_true that takes an argument conditions (a list of booleans) and returns True if at least one boolean of this list is True, otherwise the function returns False.
# If the argument conditions is an empty list, the function is_a_condition_true returns None.
# For examples:
# >>> is_a_condition_true([True, True, False, True, False, False, True])
# True
# >>> is_a_condition_true([True, True, True])
# True
# >>> is_a_condition_true([False, False])
# False
# >>> print(is_a_condition_true([]))
# None

# **************************************************************************************************************
#B1. Tạo hàm are_all_conditions_true chứa arguments conditions là 1 list. Nếu argument là list rỗng thì trả
# về None. Sử dụng vòng lặp for kiểm tra các giá trị trông list của conditions, trả về true nếu là true, false nếu là false

def is_a_condition_true(conditions):
    if not conditions:
        return None
    for condition in conditions:
        if condition:
            return True
    return False

# B2: tạo hàm nhập giá trị boolean. Nếu giá trị nhập vào là true thì trả về true, false thì trả về false, nếu ngoài 2 giá trị này thì error
def get_boolean_input():
    while True:
        boolean_input = input("Enter a boolean value (True or False): ")
        if boolean_input.lower() == 'true':
            return True
        elif boolean_input.lower() == 'false':
            return False
        else:
            print("Invalid input! Please enter either 'True' or 'False'")

# B3. tạo hàm inpurt_condition yêu cầu nhập giá trị và append nó vào list tên là conditions.
# gán biến bool_value bằng hàm get_boolean_input. sử dụng vòng lặp để nhập dữ liệu liên tục cho tới khi thoát với n.
def input_conditions():
    conditions = []
    while True:
        bool_value = get_boolean_input()
        conditions.append(bool_value)
        while True:
            more_input = input("\tDo you want to input more boolean values? (y/n) ")
            if more_input.lower() == 'y':
                break
            elif more_input.lower() == 'n':
                return conditions
            else:
                print("Invalid input! Please enter either 'y' or 'n'")

# Gọi hàm input_conditions() function và lưu trong 1 biến
conditions_list = input_conditions()

# Gọi hàm is_a_condition_true() , sử dụng biến conditions_list như là argument đầu vào
print("Your input list: "+ str(conditions_list))
print("is_a_condition_true: " + str(is_a_condition_true(conditions_list)))



# *********************************************************************************************
# def is_a_condition_true(conditions):
#     if not conditions:
#         return None
#     for condition in conditions:
#         if condition:
#             return True
#     return False

# def input_conditions():
#     conditions = []
#     while True:
#         boolean_input = input("Enter a boolean value (True or False): ")
#         if boolean_input.lower() == 'true':
#             conditions.append(True)
#         elif boolean_input.lower() == 'false':
#             conditions.append(False)
#         else:
#             print("Invalid input! Please enter either 'True' or 'False'")
#             continue
#         more_input = input("Do you want to input more boolean values? (y/n)")
#         if more_input.lower() == 'y':
#             continue
#         elif more_input.lower() == 'n':
#             break
#         else:
#             print("Invalid input! Please enter either 'y' or 'n'")
#             break
#     return conditions


# print("is_a_condition_true: "+ str(is_a_condition_true(input_conditions())));


