# Waypoint 2: Pythagorean Theorem
# Write a function calculate_hypotenuse that takes two arguments a and b (integers or floats) representing the length of the two sides of a right triangle, and that returns the length of the hypotenuse. You will use the Pythagorean theorem.
# For examples:

import math
# B1.Tạo hàm : truyền vào tham số a, b tính canh huyền c của tam giác vuông, sử dụng công thức toán căn bậc 2
def hypotenuse(a,b): # gọi tên hàm là action
    a_squared = pow(a,2)
    b_squared = pow(b,2)
    c_squared = a_squared + b_squared
    c = math.sqrt(c_squared)
    return c

# B2.Tạo hàm nhập giá trị các cạnh a,b. Gán giá trị c = function hypotenuse(a,b), làm tròn c
# Tạo đk ràng buộc nếu giá trị nhập vào là chuỗi. Sử dụng vòng lặp cho tới khi nhập đúng giá trị a,b
def result():
    a,b = None, None;
    while True:
        try:
            a = int(input("Enter the length of side A: "))
            b = int(input("Enter the length of side B: "))
            c = hypotenuse(a,b)
            print("The length of the hypotenuse is: ", round(c))
            action = input("Do you want to continue: (Y/N)");
            if action == 'N' or action == 'n': # chuyển thành action.upper()
                break;
        except ValueError:
            print("Invalid input. Please enter integers only.")

# Gọi hàm result để nhập giá trị và tính toán.
result();


