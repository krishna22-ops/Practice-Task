## Def functions 

def avg_num(a, b):    # Function that takes two numbers and returns their average
    return (a + b)/2
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
print(avg_num(a, b))


def greet(name, age):   # Function that takes a name and age and returns a greeting.
    return "Hello " + name + ", You are "  + age + " years old"
name = str(input("Enter your name:"))
age = str(input("Enter your age:"))
print(greet(name, age))

def is_even(x):      #Check if even or not 
    if x % 2 == 0:
       return True
    else:
      return False
x = int(input("Enter a number:"))
print(is_even(x))

def l_list(a):  # Find the largest one 
    return f"The largest one is {a}."
a = [33,54,66,44,53,23,13,45,67,89,99]
print(l_list(max(a)))

def count_vowels(word):   #Count vowels
    vowels = "aeiouAEIOU"
    count = 0
    for letters in word:
        if letters in vowels:
            count += 1
    return count
print(count_vowels("orange"))


## f-strings 
price = "$25" # Simple message
discount = "15%"
print(f"The price of the item is {price} and the discount is {discount}.")

# BMI calculator 
weight = int(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))
bmi = weight / height**2
print(f"Your BMI is {bmi}")

# Format a date
day = input("Enter todays day:")
date = input("Enter todays date:")
year = int(input("Enter current year:"))
print(f"Today is {day}, {date}, {year}.")

# Score
name = input("Enter your name:")
score = float(input("Enter your score:"))
print(f"{name} scored {score}")

# Length of a users name
user_name = input("Enter your username in LinkedIn:")
count = 0
for letters in user_name:
    count += 1
print(f"The length of your user name is {count}") 


## If/else tasks
age = int(input("Enter your age:"))  # Older than 18 or not
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

number = int(input("Enter a number:"))   # Checks positive or negative
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

year = int(input("Enter a year:"))   # Check if year is leap year or not
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")


password = input("Enter password")   # Password input
if password == "secret123":
    print("Access Granted.")
else:
    print("Access denied.")


score = int(input("Enter your score:"))
if score >= 50:
    print("Pass")
else:
    print("Fail")















