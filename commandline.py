# 1st project

name = input("Enter your name: ")

print("Command Line Calculator-- [Version 1.0] ")
print("Type 'help' to view commands\n\n")


while True:
    line = input(name + "@cmd: $ ")

    def add(num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print(">", "SYNTAX ERROR")
            quit()
        print(">", num1 + num2)
    
    def subtract(num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print(">", "SYNTAX ERROR")
            quit()
        print(">", num1 - num2)

    def multiply(num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print(">", "SYNTAX ERROR")
            quit()
        print(">", num1 * num2)

    def divide(num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print(">", "SYNTAX ERROR")
            quit()
        print(">", num1 / num2)

    if line == "quit":
        print(">", "Thank you for using CLC")
        quit()
    elif line == "help":
        print(">", "CLC Commands:")
        print(">", "\tquit - exits the command line")
        print(">", "\tadd x y - adds numbers")
        print(">", "\tsubtract x y - subtracts numbers")
        print(">", "\tmultiply x y - multiplies numbers")
        print(">", "\tdivide x y - divides numbers")
    elif "add" in line:
        mathlist = line.split()
        add(mathlist[-2], mathlist[-1])
    elif "subtract" in line:
        mathlist = line.split()
        subtract(mathlist[-2], mathlist[-1])
    elif "multiply" in line:
        mathlist = line.split()
        multiply(mathlist[-2], mathlist[-1])
    elif "divide" in line:
        mathlist = line.split()
        divide(mathlist[-2], mathlist[-1])
    else:
        print(">", "SYNTAX ERROR")