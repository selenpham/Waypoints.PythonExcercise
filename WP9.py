# WP9: Write a function capitalize_string which behavior is described by the following epydoc documentation:
# def capitalize_words(s):
"""Return a copy of the string with all the words capitalized.

    This function sets the first character in each word of the string `s`
    to uppercase and the rest to lowercase.

    The function removes any duplicate whitespace characters between
    words.

    If `None` is passed, the function returns `None`.

    @param s: a string that possibly contains words separated by whitespace
        characters.

    @return: a string where the first character in each word of the string
        `s`has been converted to uppercase and all remaining characters of
        this word have been converted to lowercase.

    @raise TypeError: if the argument `s` is not a string.
"""

# def capitalize_string(s):
#     if s is None:
#         return None

#     if not isinstance(s, str):
#         raise TypeError("Argument must be a string")

#     # split the string into words, then capitalize the first letter of each word and convert the rest to lowercase
#     words = [word.capitalize() for word in s.split()]

#     # join the words back into a string and remove any duplicate whitespace characters
#     return " ".join(words)


# s = "hello , im  a  world"
# result = capitalize_string(input())
# print(result)

#B1: Tạo hàm chuyển các chữ cái đầu trong chuỗi thành chữ hoa
def capitalize_string(s):
    if s is None:
        return None

    if not isinstance(s, str):
        raise TypeError("Argument must be a string")

#Tách các chữ trong chuỗi, in hoa chữ cái đầu của chữ, sau đó join lại thành string
    words = [word.capitalize() for word in s.split()]
    return " ".join(words)

#B2: Tạo hàm input chuỗi
def input_string():
    s = input("Enter a string: ")
    if not s.replace(" ", "").isalpha():
        raise ValueError("Input string must contain only letters and spaces")
    return s

try:
    s = input_string()
    result = capitalize_string(s)
    print(result)

except ValueError as e:
    print(f"Error: {e}")

except TypeError as e:
    print(f"Error: {e}")