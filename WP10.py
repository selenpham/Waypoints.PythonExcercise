# Write a function uppercase_lowercase_words that takes an argument s (a string) and that returns a copy of this string with the words converted to uppercase or lowercase depending on their position in the string (starting with 0):
# Words at even position are converted to uppercase;
# Words at odd position are converted to lowercase.

# def uppercase_lowercase_words(s):
#     words = s.split()
#     result = ""
#     for i in range(len(words)):
#         if i % 2 == 0:
#             result += words[i].upper()
#         else:
#             result += words[i].lower()
#         result += " "
#     return result[:-1]

# def input_value():
#     s = input("Enter a string: ")
#     return s
    
# s = input_value()
# result = uppercase_lowercase_words(s)
# print(result)

#Tạo hàm biến các chữ cái ở vị trí chẵn thành Upper,lẻ thành lower
def uppercase_lowercase_words(s):
    words = s.split()
    result = ""
    for i in range(len(words)):
        if i % 2 == 0:
            result += words[i].upper()
        else:
            result += words[i].lower()
        result += " "
    return result[:-1]

#Tạo hàm input giá trị, tạo ràng buộc nếu nhập số không hoặc để trống ko input
def input_value():
    s = ""
    while s.lower() != "e":
        s = input("Nhap 1 chuoi (hoac nhap 'E'de thoat): ")
        if s.lower() == "e":
            break
        elif s.strip() == "":
            print("Vui long khong de trong.Xin moi nhap lai.")
        elif any(char.isdigit() for char in s):
            print("Vui long nhap lai chuoi")
        else:
            return s
# Tạo vòng lặp neu   
while True:
    s = input_value()
    if s.lower() == "e":
        break
    result = uppercase_lowercase_words(s)
    print(result)