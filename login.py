
username=input("Enter your username=")
password=input("Enter your password=")

while len(password)<8 or not password.isdigit():
    password=input("Enter youe password again =")

print("Account created.")

username1=input("Enter username for login=")
password1=input("Enter password for login=")

while username!=username1 or password!=password1:
    username1=input("Enter username again=")
    password1=input("Enter password again=")

print("Login successful..")