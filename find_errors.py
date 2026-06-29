'''
# 1 
age = input("Enter your age: ")
try:
    next_year = int(age) + 1
except ValueError:
    print("Age must be a number")
    exit()
print("Next year you will be", next_year)
'''
# 2
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("enter a number!")