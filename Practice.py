#f-strings 
name = input("Enter your name:")   # Greeting message 
print(f"Hello {name}! Welcome to Python!")

current_age = int(input("Enter your current age:"))  #Age in 10 years 
future_age = current_age + 10
print(f'You will be {future_age} in 10 years age.')

length = int(input("Enter the length of the rectangle:"))  # Area of rectangle 
breadth = int(input("Enter the breadth of the rectangle:"))
area = length * breadth
print(f"The area of the rectangle with the given inputs is {area}.")

c_temp = int(input("Enter a temprature in Celcius:"))  #Temperature converter
f_temp = (c_temp *9/5) + 32
print(f"The temprature in Fahrenheit is {f_temp}")


# For loops
for i in range(1,21):    # Every number from 1-20
    print(i)

fruits = ['b','a','n','a','n','a']   # Every letter in the word "banana"
for i in fruits:
    print(i)

for i in range(2, 51, 2):   # Every even number from 1-50
    print(i)

for i in range(1, 11):   #Square of each number from 1-10
    print(i*i)

total = 0      #Sum of numbers from 1 to 100
for i in range(1, 101):   
    total += i
print(total)


#def functions 
def greet(name):    # Greet someone
    return "Hello " + name + "!"
print(greet("Krishna"))

def square(num):    # Enter a number and square it
    return num*num
num = int(input("Enter a number:"))
print(square(num))

def is_even(num):   # Even or odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number:"))
print(is_even(num))

def area_of_rectangle(l, b):    # Area of rectangle
    return l * b
print(area_of_rectangle(5, 6))

def fahrenheit_to_celsius(n):   # Fahrenheit to Celcius
    return (n-32)*5/9
n = float(input("Enter a temperatue in Fahrenheit:"))
print(fahrenheit_to_celsius(n))
