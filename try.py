import re 

# pattern = r"exit"
# s1 = "I love programming in Python" 
# match = re.search(pattern, s1)
# if match:
#     print("Pattern found")
# else:
#     print("Pattern not found")


# text = "My name is Neema, and my email is neema@gmail.com"
# match = re.search(r"\w+@\w+\.\w+", text)
# if match:
#     print("Found email:", match.group())
# text = "Contact us at support@site.com or sales@site.com"
# emails = re.findall(r"\w+@\w+\.\w+", text)
# print(emails)

# password = "MyPassword123!"
# # At least 8 characters, at least one digit, one uppercase, one special char
# pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$'
# if re.match(pattern, password):
#     print("Valid password!")
# else:
#     print("Weak password!")


# def is_valid_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return bool(re.match(pattern, email))
# def is_valid_phone(phone):
#     pattern = r'^07\d{8}$'  # Kenyan format: 07 followed by 8 digits
#     return bool(re.match(pattern, phone))
# print(is_valid_email("neema@gmail.com"))   # True
# print(is_valid_phone("0712345678"))        # True

my_string = "H e l l o"
my_string = my_string.replace("l", "L")
my_string.strip()
split_text = my_string.split(" ")
print(split_text)
