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
# 10

try:
    num1 = int(input("Number 1: "))
    op = input("Operator: ")
    num2 = int(input("Number 2: "))

    if op == "+": 
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
        print("cannot divede by 0")
    else:
        print("invalid operator")
except ZeroDivisionError:
    print("cannot divede by 0")
except ValueError:
    print("enter a number!")
finally:
    print("Calculator closed")

# 10 extra
celsius = input("Celsius: ")
try:
    fahrenheit = int(celsius) * 9 / 5 + 32
except ValueError:
    print("Temperature must be a number")
print(fahrenheit)

# 2
word = input("Enter word: ")
try:
    print(word[0])
except IndexError:
    print("enter something")
# 3
scores = [90, 80, 100]
total = 0

for score in scores:
    #  total = score
    total += score

average = total / len(scores)
print(average)
# output = 33.3
# 90
# logical error

# 4
products = {
    "pen": 4,
    "notebook": 12}
try:
    product = input("Product: ")
    amount = int(input("Amount: "))
    print(products[product] * amount)
except ValueError:
    print("enter a number")
    exit()
except KeyError:
    print("product isn't valid")
    exit()

# 5
files = ["data.txt", "users.csv", "notes.txt"]
try:
    choice = int(input("Choose file number: "))
    print(files[choice])
except ValueError:
    print("enter a number")
except IndexError:
    print("invalid index")

# 6
numbers = [4, 10, 2, 8]
maximum = 0

for number in numbers:
    #if number < maximum:
    if number > maximum:
        maximum = number

print(maximum)
# worng output = 0
# expected =10
# logical error
'''
#7
user = {
    "name": "Dana",
    "age": 25}

try:
    field = input("Choose field: ")
    print(user[field].upper())
except KeyError:
    print("invalid field")