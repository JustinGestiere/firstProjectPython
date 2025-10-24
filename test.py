
# code
password = input("Enter password: ")
password_length = len(password)
# verifier si le password < 8 caracteres
if password_length <= 8:
    print("Password is too short")
elif 8 < password_length < 16:
    print("good password")
else:
    print("too long")