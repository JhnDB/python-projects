print("Welcome to Jemflix!\n")
name = input("Enter your name:")
age = input("Enter your age:")

try:
    age = int(age)
except:
    age = -1

if age < 0:
    print("Enter a valid age!")
elif age < 13:
    print("Sorry " + name + ", 13+ only!")
    req_age = 13 - age
    print("Wait " + str(req_age) + " year(s) before signing up")
else:
    print("Welcome, " + name + "!")