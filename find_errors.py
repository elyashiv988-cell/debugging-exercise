'''
# 1 
age = input("Enter your age: ")
try:
    next_year = int(age) + 1
except ValueError:
    print("Age must be a number")
    exit()
print("Next year you will be", next_year)

# 2
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("enter a number!")
# 3
try:
    numbers = [10, 20, 30]
    index = int(input("Choose index: "))
    print(numbers[index])
except IndexError:
    print("Index not found")
except ValueError:
    print("enter a number!")
# 4
prices = {
    "apple": 3,
    "banana": 5}
item = input("Enter item: ")
try:
    print(prices[item])
except KeyError:
    print("item doesn't found")
# 5
numbers = [100, 200, 300]
try:
    index = int(input("Choose index: "))
    divider = int(input("Choose divider: "))
    result = numbers[index] / divider
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("enter only a number!")
except IndentationError:
    print("index not found")
# 6
try:
    score = int(input("Enter score: "))
    print("Your score is", score)
except ValueError:
    print("Invalid score")
finally:
    print("check finished")
# 7
name = input("Enter your name: ")
if name == "admin":
    print("Welcome admin")
else:
    print("Welcome user")
# it was an error at the constuction of the code who should fixed. but try/except are for prevent unwanted but predictable situations
    '''
# 8
price = 100
discount = 20
#final_price = price - discount / 100
final_price=price-(price/100*discount)
print(final_price)
# output = 99.8
# expeceed price = 80
# it's a logic error

# 9
password = "abc123"
guess = input("Enter password: ")

#if guess != password:
if guess==password:
    print("Login successful")
else:
    print("Wrong password")



