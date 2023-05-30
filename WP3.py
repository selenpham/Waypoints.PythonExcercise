# Waypoint 3: Test whether all Conditions are True
# Write a function are_all_conditions_true that takes an argument conditions (a list of booleans) and returns 
# True if all the booleans of this list are True, otherwise the function returns False.
# If the argument conditions is an empty list, the function are_all_conditions_true returns None.
# For examples:
# >>> are_all_conditions_true([True, True, False, True, False, False, True])
# False
# >>> are_all_conditions_true([True, True, True])
# True
# >>> print(are_all_conditions_true([]))
# None

# **************************************************************************************************************
#B1. Tạo hàm are_all_conditions_true chứa arguments conditions là 1 list. Nếu argument là list rỗng thì trả
# về None, nếu không thì trả về list boolean đã nhập

def are_all_conditions_true(conditions):
    if not conditions:
        return None
    return all(conditions)
# B2: tạo hàm nhập giá trị boolean. Nếu giá trị nhập vào là true thì trả về true, false thì trả về false, nếu ngoài 2 giá trị này thì error

def get_boolean_input():   
    while True:
        boolean_input = input("Enter a boolean value (True or False): ")
        if boolean_input.lower() == 'true':
            return True
        elif boolean_input.lower() == 'false':
            return False
        
        print("Invalid input! Please enter either 'True' or 'False'")
# B3. tạo hàm input_condition yêu cầu nhập giá trị và append nó vào list tên là conditions.
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
            
            print("Invalid input! Please enter either 'y' or 'n'")
# B4. In ra giá trị của hàm are_all_conditions_true chứa argument là function input_conditions
conditions_list = input_conditions()
print("Your input list: "+ str(conditions_list));
print("are_all_conditions_true: " + str(are_all_conditions_true(conditions_list)))



