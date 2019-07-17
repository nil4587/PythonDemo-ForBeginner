#*************************************************************************************************#
# CMD + SHIFT + M : Move to problems under VSCode terminal 
# SHIFT + CMD + P : Command Palette

# PYTHON for beginners (Video tutorials):
# 1. https://www.youtube.com/watch?v=f79MRyMsjrQ
# 2. https://www.youtube.com/watch?v=_uQrJ0TkZlc
# 3. https://www.youtube.com/watch?v=yE9v9rt6ziw

# Python Fundamentals
# Data Structures
# Object-oriented Programming (OOP)
# Writing Reusable Code
# Error Handling
# Automation
# Web Scraping
# Consuming APIs
# Automated Testing with Selenium
# Consuming 3rd-party Packages
# Publishing Python Packages
# Working with Files and Directories
# Working with CSV and JSON Files
# Working with Excel Spreadsheets
# Working with PDFs
# Working with ZIP Files
# Sending Emails and Text Messages
# Introduction to Building Web Apps

#*************************************************************************************************#
# Tools :
# 1. Editor(VSCode, Atom, Sublime),

# 2. IDE(Integrated Development Environment :
#   a. Features : Autocompletion, Debugging, Unit Testing, Linting, Code Formatting, Code Snippets)
#   b. PYCHARM as IDE

# 3. PYTHON Extensions :
#   a. PYLINT : Linting which anlyse the code and finding the errors (MYPY Linter)
#   b. AUTO PEP8 : Install through command (python3 -m pip install -U autopep8)

# 4. Code Formatting :
#   a. PEPs : PYTHON ENHANCEMENT PROPOSALS (PEP8 : Style Guide for Python Code)
#   b. Throgh Command Palette, search for Format Document
#   and install it through command (python3 -m pip install -U autopep8)

# 5. Running Python Code :
#   a. Move to left panel with Extensions and search for "Code Runner : Jun Han as Editor"
#   b. Now click and release "CTRL + ALT + n" keys together

# 6. Python Implementation :
#   a. It's program which understands the rules of PYTHON language and executes the code written in PYTHON itself.
#   b. Default implementation of Python in C and that's y it's called as "CPython"
#   c. There are other implementations of Python too. (
#       1. Jython : Written in Java
#       2. IronPython : Written in C#
#       3. PyPy : Written in Subset of Python
#       4. Reasons of having various version of PYTHON implmentations (Multiple OS, Browsers, Languages)

# 7. Execution of Python Code with CPython :
#   Java Language -> Java Compiler -> Java ByteCode -> Java Virtual Machine -> Appropriate Machine Code
#   Python Program -> CPython Compiler -> Python ByteCode -> Python Virtual Machine -> Appropriate Machine Code

#            Cpython ==> Python ByteCode ==> Python Virtual Machine
#          /                                                        \
#         /                                                          \
# "Python"                                                          "Machine Code"
#         \                                                         /  
#          \                                                      /
#            Jython ==> Jython ByteCode ==> Java Virtual Machine


#*************************************************************************************************#
# TYPING :
# 1. STATIC : C++, C#, JAVA (It's required to mention variable type at the time of declaring it)
# 2. DYNAMIC : Javascript, Ruby, Python (It automatically type casts the variable)
#*************************************************************************************************#

import random
from ecommerce import shipping
from ecommerce.shipping import calculate_shipping_cost
import math

# print("Hello World :)")
# print("&" * 10)
# x = 1
# student_count = 11  # Integer
# fees = 12.34  # Float
# is_holiday = False  # Boolean
# technology_name = "Python Programming"  # String
# print(student_count)
# print(fees)
# print(is_holiday)

# x = 90
# print(id(x)) # it will print the memory location of an x where the exact value is stored.
# Immutable type : Becuase integers are immutable each time, the new value of integers will have new memory address.
# Mutable type : the memory address won't be changed after updating the value of mutable types.
#*************************************************************************************************#
# MULTILINE COMMENT :
#*************************************************************************************************#

# email_message = """
# Hello everyone,
# Tomorrow, i'm going to work on PYTHON programming and leave the rest of React Native as it's.

# Thanks
# Nilesh
# """

# print(email_message)
# print(len(email_message))

#*************************************************************************************************#
# STRING OPERATIONS :
#*************************************************************************************************#

# first = "Nilesh"
# last = "Prajapati"
# fullname = first + " " + last
# print(fullname)

# # fullname = f"{first} {last}"
# # print(fullname)

# # fullname = f"{len(first)} {last}"
# # print(fullname)

# # fullname = f"{len(first)} {2 + 2}"
# # print(fullname)

# print(fullname.upper())

#------------------------------------------------------------------------------------------------#

# technology_name = "  python programming   "
# print(technology_name.title())
# # Capitalized manner after trimming whole string from left & right side
# print(technology_name.strip().title())
# print(technology_name.rstrip().title())  # Trim from right side only
# print(technology_name.lstrip().title())  # Trim from left side only

#------------------------------------------------------------------------------------------------#

# print(technology_name.find("gra"))
# print(technology_name.find("gRa"))  # Find
# print(technology_name.replace("ra", "ca"))  # Replace
# print("ca" in technology_name)  # Contains
# print("ca" not in technology_name)  # Not Contains

#------------------------------------------------------------------------------------------------#

# print(25 + 5)  # Addition
# print(25 - 5)  # Substraction
# print(25 * 5)  # Multiplication
# print(25 / 5)  # Division with Float value
# print(25 // 5)  # Division with Int value
# print(25 % 5)  # Modulo to get remainder from Division operation
# print(25 ** 5)  # Exponent value == (25)*(25)*(25)*(25)*(25)

#*************************************************************************************************#
# OPERATOR PRECEDENCE: (Order of execution for mathematical operations)
#*************************************************************************************************#

# Parenthesis,
# **(exponentiation),
# /(Division) or *(Multiplication),
# +(Addition) or -(Substraction)

#*************************************************************************************************#
# AUGMENTED ASSIGNMENT OPERATOR :
#*************************************************************************************************#

# x = 15
# x += 4  # (like x=x + 4)

#*************************************************************************************************#
# FUNCTION USAGE WITH NUMBERS :
#*************************************************************************************************#

# print(round(2.4))  # Rounding the numerice value to lower level
# print(round(2.6))  # Rounding the numerice value to upper level
# print(abs(-2.6))  # Absolute value like -ve to +ve value conversion

# print(math.ceil(2.4))  # Always return higher / upper value
# print(math.floor(2.4))  # Always return smaller / lower value

#*************************************************************************************************#
# TYPE CONVERSION :
#*************************************************************************************************#

# x = input("X: ")
# # To print the type of input parameter entered by user
# print(f"typeof(x) : {type(x)}")
# y = int(x) + 3
# print(f"x: {x} y: {y}")
# # To print the type of calculated value after type casting...
# print(f"typeof(y) : {type(y)}")

#*************************************************************************************************#
# COMPARISION OPERATORS :
#*************************************************************************************************#

#------------------------------------------------------------------------------------------------#
# Numberic :
#------------------------------------------------------------------------------------------------#

# 10 > 3  # TRUE
# 10 >= 3  # TRUE
# 10 < 20  # TRUE
# 10 <= 20  # TRUE
# 10 == 10  # TRUE
# 10 == "10"  # FALSE because both the values are of different types
# 10 != "10"  # TRUE because both the values are of different types

#------------------------------------------------------------------------------------------------#
# String :
#------------------------------------------------------------------------------------------------#

# # TRUE because at the time of sorting "bag" comes after "apple"
# print("bag" > "apple")
# print("bag" == "BAG")  # FALSE : because it's case sensitive language

# print(ord("b"))  # Numberic representation of character
# print(ord("B"))  # Numberic representation of character

#*************************************************************************************************#
# CONDITIONAL STATEMENTS :
#*************************************************************************************************#

#------------------------------------------------------------------------------------------------#
# # 1. IF Statement :
#------------------------------------------------------------------------------------------------#

# temprature = 35
# if temprature > 50:  # colon is required whenever you want to implement IF statement
#     # indentation is required after IF condition
#     print("It's too hot outside.")
#     # you can place multiple statements after IF condition alongwith indentation
#     print("Take water with you whenever you want to go for shopping")
# elif temprature > 40:
#     print("It's nearer to hot condition outside.")
#     print("Prepare your self for next higher level.")
# else:
#     print("It's warm weather outside and if you want to minimize this count then please plant trees outside your home.")
# # Once you remove the indentation compiler considers the IF statement condition gets over.
# print("Condition placement done.")

#------------------------------------------------------------------------------------------------#
# # 2. Ternary Operators :
#------------------------------------------------------------------------------------------------#

# age = 25
# # It's a plain ENGLISH statement
# message = "Eligible for Master Degree." if age >= 25 else "Not eligible for Master Degree."
# print(message)

#------------------------------------------------------------------------------------------------#
# # 3. Logical Operators (and, or, not) : Used to model more complex conditions
#------------------------------------------------------------------------------------------------#

# # Example of Loan Processing :

# higher_income = True
# good_credit = False
# no_debt = True
# student = False

# # Here, no need to compare a boolean with its value like higher_income == True
# if higher_income or good_credit and no_debt:
#     print("User will be eligible for Bank Loan")
# else:
#     print("User won't be eligible for Bank Loan")

# # Check for not operator like not student
# if not student:
#     print("User will be eligible for Bank Loan because it's not a student")
# else:
#     print("User won't be eligible for Bank Loan because it's a student")

# # More complex operations like below
# if (higher_income or good_credit or no_debt) and not student:
#     print("User will be eligible for Bank Loan because it's not a student")
# else:
#     print("User won't be eligible for Bank Loan because it's a student")

#------------------------------------------------------------------------------------------------#
# Short Circuit Evaluation : (In python, logical operators called as short circuit like electrical circuit board)
#------------------------------------------------------------------------------------------------#

# higher_income = False
# good_credit = True
# no_debt = True
# student = True

# # Python Compiler checks condition by picking the parameters validation one by one
# # It stops the execution if any of them found False and it won't check the whatever the values the next parameters have
# # It will execute the statement under the else condition
# if higher_income and good_credit and no_debt and not student:
#     print("User will be eligible for Bank Loan because it's not a student")
# else:
#     print("User won't be eligible for Bank Loan because it's a student")

# # Python Compiler checks condition by picking the parameters validation one by one
# # It stops the execution if any of them found True and it won't check the whatever the values the next parameters have
# # It will execute the statement under the if condition
# if higher_income or good_credit or no_debt or not student:
#     print("User will be eligible for Bank Loan because it's not a student")
# else:
#     print("User won't be eligible for Bank Loan because it's a student")


#------------------------------------------------------------------------------------------------#
# # 4. Chaining of Comparision Operators :
#------------------------------------------------------------------------------------------------#

# # age should be between 18 and 65

# age = 25
# if 18 <= age < 65:  # equivalent to age >= 18 and age < 65:
#     print("Age in between 18 - 65")
# else:
#     print("Age is not in between 18-65")

#------------------------------------------------------------------------------------------------#
# # 5. For Loops :
#------------------------------------------------------------------------------------------------#

# # For loop to print a statemented repeatadely 5 times
# # For each iteration index parameter will contain new value
# for index in range(5):
#     print("Index", index)

# # Loop will be executed from 1 to 5 and 6 will be excluded
# for index in range(1, 6):
#     print("Index", index)

# # Loop will be executed from 1 to 9 and it will exclude number divisionable by 2
# for index in range(1, 10, 2):
#     print("Index", index, index * "*")

# # A For..Loop to print right angle Piramid
# for index in range(5):
#     print("* " * (index + 1))

#------------------------------------------------------------------------------------------------#
# # 6. For..Else :
#------------------------------------------------------------------------------------------------#

# successful = False  # A flag to check successful to break the for loop in between
# for index in range(5):
#     print("Index", index)
#     if successful:  # A condition to check succesful flag value to True, break the loop if successful
#         print("Successfully Indexed")
#         break
# else:  # Execute if successful == True never gets success in the above loop
#     print("Unsucessful indexed")


#------------------------------------------------------------------------------------------------#
# # 7. Nested Loops :
#------------------------------------------------------------------------------------------------#

# # Outer loop gets executed first
# for x in range(4):
#     # Inner loop gets executed in parallel to outer loop
#     for y in range(2):
#         print(f"({x}, {y})")

#------------------------------------------------------------------------------------------------#
# # 8. Iterables :
#------------------------------------------------------------------------------------------------#

# # range() function is one of the examples of Iterable primitive types available in Python
# # Using range(), we can iterate value multiple times like in below example.
# for number in range(4):
#     # So, now i can execute print function to display value multiple times.
#     print("Iterate")

# # Just like range(), string is also an iterable
# for string in "PYTHON":
#     # below line will print each character from the "PYTHON" string separately
#     # In each iteration, string parameter will contain different parameter
#     print(string)

# # Just like range(), LIST is also an iterable
# for number in [1, 2, 4, 5, 6]:
#     # below line will print each numeric value from the LIST separately
#     # In each iteration, number parameter will contain different parameter
#     print(number)

#------------------------------------------------------------------------------------------------#
# # 9. While Loops :
#------------------------------------------------------------------------------------------------#

# number = 100
# # A while loop statement to repeate the statements until the specified condition executes
# while number > 0:
#     print(number)  # print number until number > 0
#     number //= 2  # divide the number with integer value

# command = ""
# # A while loop condition to check command == quit
# # Loop will be executed until user types "quit" on shell
# # Have placed two conditions because upper & lower case characters have different numeric values
# while command != "quit" and command != "QUIT":
#     # Gets user input from shell and store it into command variable
#     command = input(">")
#     print("ECHO", command)

# # Insted of writing multiple conditions, just convert string to lowercase and compare it with user input
# # So, whatever the input format from user: like Quit, QUIT, quit, QUit, QuIt, etc..
# while command.lower() != "quit":
#     # Gets user input from shell and store it into command variable
#     command = input(">")
#     print("ECHO", command)

#------------------------------------------------------------------------------------------------#
# # 10. Infinite Loops :
#------------------------------------------------------------------------------------------------#

# # An infinite loop and we don't have to initialize the value of command variable just becuase
# # command variable will be fetch from user input and then it will be compared with the given conditional parameter
# # Note : So, the main difference between while loops and infinite loops is the one statement i.e. break
# while True:
#     # Gets user input from shell and store it into command variable
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":  # A condition has been placed to check & compare user input with "quit"
#         print("Quits loop")
#         # For infinite loops there must be a break statement whereas the condition gets satisfied
#         # otherwise it will jump to infinite mode and will have the memory related issues.
#         # Due to which application may get crash
#         break


# # Exercise :
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")


#*************************************************************************************************#
# FUNCTIONS :
#*************************************************************************************************#

# # A way to define a function along with the statements to perform various operations
# def print_welcome_message():
#     print("Hi There")
#     print("Welcome to function")


# print_welcome_message()  # A way to call a function inside a project

#------------------------------------------------------------------------------------------------#
# # 1. Arguments :
#------------------------------------------------------------------------------------------------#

# # A way to define a function along with the arguments
# # Here, first_name & last_name called as PARAMETERS
# # When user will pass the values to this function, they will be called as ARGUMENTS
# # It's also a generalised & reusable function to print message for multiple users
# # Both the given parameters are required from user whenever it will be called
# def print_welcome_message(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome to function")


# # A way to call a function inside a project by passing arguments to it.
# # It's also a generalised & reusable function to print message for multiple users
# print_welcome_message("Nilesh", "Prajapati")
# print_welcome_message("Dhvanit", "Prajapati")

#------------------------------------------------------------------------------------------------#
# # 2. Types of Function :
#------------------------------------------------------------------------------------------------#

# Two types of functions :
# a. A function which executes/performs the given task
# b. A function which performs/executes the given task and also return a value at the end.

# # A function with the input parameter which returns the value after/without performing several operations
# # In Python, all functions returns "None" value by default
# def return_greeting_meesage(fullname):
#     return f"Hi {fullname} \n Welcome to Abroad"


# # A way to call a function with arguments which returns a value to store it in a variable for later use in project.
# message = return_greeting_meesage("Nilesh Prajapati")
# file = open("content.txt", "w")  # A statement to open a file in writing mode
# # A statement to write a message, return from a function, to a file.
# file.write(message)

#------------------------------------------------------------------------------------------------#
# # 3. Keyword Arguments : (a. POSITIONAL (value without the name of argument), b. KEYWORD (value with the of argument)
#------------------------------------------------------------------------------------------------#

# # A function gets an arguments, performs an addition on those parameters and then returns a result.
# def increment(number, by):
#     return number + by


# # A pameter which contains the result given by the function.
# result = increment(5, 4)
# # A line to print the result given by the increment function.
# print(result)
# # A newer way to pass arguments directly to print function without storing it to a temporary varilable
# # For this, first increment function will be called to get the result and then PYTHON will store that result to a temporary
# # variable which won't be visible and then that variable will be passed to print statement to display it at terminal.
# print(increment(5, 4))
# # To make a function more readable to user, here, we have used "by" keyword prior "4"
# # So, now, user can read it just like plain ENGLISH (i.e increment 5 by 4)
# print(increment(5, by=4))

#------------------------------------------------------------------------------------------------#
# # 4. Default Arguments :
#------------------------------------------------------------------------------------------------#

# # A function gets an arguments, performs an addition on those parameters and then returns a result.
# # Here, user can put by with default value.
# # So, in case, if user don't pass any value the default value will be used to calculate the result.
# # "by" known as "OPTIONAL PARAMETER" for this case of function
# # "OPTIONAL PARAMETER" should come after all the required parameters have been defined.
# def increment(number, by=1):
#     return number + by


# # For the below format, increment function will use by=1 as default argument and result will be "4"
# print(increment(3))
# # For the below format, increment function will use user input i.e by=5 and result will be "8"
# print(increment(3, 5))

#------------------------------------------------------------------------------------------------#
# # 5. *args, wait, what? :
#------------------------------------------------------------------------------------------------#

# # A function which accepts list of arguments in a single parameter by declaring prefix "*"
# # to that parameter without declaring multiple parameters
# def multiply(*numbers):
#     # it will display whole list of arguments contained by numbers parameter
#     print(numbers)


# # (2, 3, 4, 5, 6) called as tuples, can't modify tuple by adding or removing objects to or from it
# # [2, 3, 4, 5, 6] called as list, can modify collection / list by adding or removing objects to or from it
# # A way to pass mulitple arguments at once
# multiply(2, 3, 4, 5, 6)

# # A function which accepts list of arguments in a single parameter by declaring prefix "*"
# # to that parameter without declaring multiple parameters
# def multiply(*numbers):
#     total = 0
#     # Tuples(numbers) are iterable just like other iterables like LIST, STRING and so, can use it in loops
#     for number in numbers:
#         total += number  # Addition to get total sum of all available numbers as argument
#         print(number)
#     print(total)  # A statement to print the total of all numbers


# # (1, 2, 3, 4, 5) called as tuples, can't modify tuple by adding or removing objects to or from it
# # [1, 2, 3, 4, 5] called as list, can modify collection / list by adding or removing objects to or from it
# # A way to pass mulitple arguments at once
# multiply(1, 2, 3, 4, 5)

#------------------------------------------------------------------------------------------------#
# # 6. **args or called it as DICTIONARY :
#------------------------------------------------------------------------------------------------#

# # A function to allow to pass multiple keyword arguments
# # PYTHON will convert later on it to a dictionary packaged with keys & values
# # So, here in this case, user is known as dictionary.
# def save_user(**user):
#     # So, print statement will display all the contained keys & values to user through terminal.
#     print(user)
#     # So, print statement will display the contained value for the specified key in dictionary.
#     print(user["name"])


# # A way to pass multiple keyword arguments in form of DICTIONARY
# save_user(id=1, name="Nilesh Prajapati", age=23)

#------------------------------------------------------------------------------------------------#
# # 6. Scope :
#------------------------------------------------------------------------------------------------#

# # A) Local Variables :
# # 1. Have short life when it's passed to a function.
# # 2. Python will assign temporary memory location to that variable until the operation gets completed by function.
# # 3. After that, the garbase collector will release that memory location (Python interpreter performs this operation)

# # Example :
# def greeting(name):
#     message = "New arrival"
#     print(message)


# def greeting_welcom(name):
#     message = "New arrival"
#     print(message)


# # A function with arguments
# greeting("iOS")
# # A function with arguments
# greeting_welcom("iOS")

# # NOTE : In above both the functions, name & message variables are there but they are local to those functions only


# # B) Global Variables :
# # 1. It stays long it memory and won't release by garbase collector until user release it manually.
# # 2. So, it's good practice to create functions and use of local variables in the functions.

# # Example :

# # A globally declared variable
# message = "A"


# def greeting(name):
#     # message was declared inside the function and so, it was called local variable
#     # but now it's became global as i have redeclared it globally with "global" keyword.
#     # so, it will change the outside declared message value to "B"
#     global message
#     message = "B"
#     # It will print the "B" as per it's local value
#     print(message)


# greeting("C")
# # this will print "A" instead "B" because message doesn't change inside greeting function
# # becuase the variable declared inside it is totally different from the global variable declared outside the function.
# # but after change in declaration of message variable inside greeting function, it will print modified value i.e "B"
# print(message)

#*************************************************************************************************#
# DEBUGGING :
#*************************************************************************************************#

# F5 : To start the DEBUGGING
# F9 : To place break point in front of the line
# F10 : To move to the next line of code at the time of debugging
# F11 : To step inside the function to check the mutiple steps instead of jumping out of it to the next line of code.
# SHIFT + F5 : To end the DEBUGGING
# SHIFT + F11 : To jump outside the function at the time of DEBUGGING

# # A function to implement FizzBuzz algorithm
# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input


# print(fizz_buzz(15))

#*************************************************************************************************#
# EXCERCISES :
#*************************************************************************************************#

# #------------------------------------------------------------------------------------------------#
# # 1. A Program to convert weight from (L)bs to (K)g and vice a versa.
# #------------------------------------------------------------------------------------------------#

# calculated_weight = 0
# weight = float(input("Weight : "))
# lbs_kg = input("(L)bs or (K)g : ")

# while lbs_kg.lower() != "k" or lbs_kg.lower() != "l":
#     if lbs_kg.lower() == "l":
#         calculated_weight = weight * 0.45
#         print(f"Your weight : {round(calculated_weight)} (K)g")
#         break
#     elif lbs_kg.lower() == "k":
#         calculated_weight = weight / 0.45
#         print(f"Your weight : {calculated_weight} (L)bs")
#         break
#     else:
#         print("Invalid input.. Please enter l/L unit for (L)bs or k/K unit for (K)g")
#         lbs_kg = input("(L)bs or (K)g : ")

#------------------------------------------------------------------------------------------------#
# 2. A Program to guess a secret number between 1 - 10
#------------------------------------------------------------------------------------------------#

# # Default secret number in the game for which user has to enter correct value
# secret_number = 8
# user_input = int(input("Guess a number (1-10) : "))
# attempt = 0
# # Checks whether user input and secret numbers are same or not.
# while user_input != secret_number:
#     attempt += 1
#     # check until user attempts == 3
#     if attempt == 3:
#         print("You failed to guess the number")
#         break
#     # Ask for user input until the user input matchs with secret number
#     user_input = int(input("Guess a number (1-10) : "))
# else:
#     # While Loop has default else condition and according to it,
#     # it numbers are matched with each other then user will be notified as Winner of the game.
#     print("You win!!")

#------------------------------------------------------------------------------------------------#
# 3. A Program to Car Game which understands the commands like Start, Stop, Quit & Help
#------------------------------------------------------------------------------------------------#

# user_input = ""
# car_started = False
# while True:  # Comparision of user input with "quit" and it will continue to execute statements come under while loops until user provides "quit"
#     # A statement to get user input and after that convert input to lower case prior comparision
#     user_input = input("> ").lower()
#     if user_input == "help":  # A statement to compare user inpur with "help" command
#         print("Start - to start the car")
#         print("Stop - to stop the car")
#         print("Quit - to exit")
#     elif user_input == "start":  # A statement to compare user inpur with "start" command
#         if car_started:
#             print("Car is alreay started")
#         else:
#             car_started = True
#             print("Car Started... Ready to go !!")
#     elif user_input == "stop":  # A statement to compare user inpur with "stop" command
#         if not car_started:
#             print("Car is already stopped..")
#         else:
#             car_started = False
#             print("Car stopped.")
#     elif user_input == "quit":  # A statement to quit from the program by breaking the loop
#         break
#     else:  # If user input doesn't qualify for above conditions then user will be notified for entering unknow command.
#         print("Sorry, i can't understand the command.")

#------------------------------------------------------------------------------------------------#
# 4. A Program to print the total cost of items in shopping cart using For..Loops
#------------------------------------------------------------------------------------------------#

# item_prices = [10, 20, 30, 40]
# total_cost = 0
# for item_price in item_prices:
#     total_cost += item_price
# print(f"Total Shopping Cost: {total_cost}")

#------------------------------------------------------------------------------------------------#
# 5. A Program to Draw "F" & "L" shape using list or collection of intergers
#------------------------------------------------------------------------------------------------#

# # numbers = [5, 2, 5, 2, 2] # TO print "F"
# numbers = [2, 2, 2, 2, 7]

# # for number in numbers:
# #     print("x" * number)

# for number in numbers:
#     iteration = ""
#     for i in range(number):
#         iteration += "x"
#     print(iteration)

#------------------------------------------------------------------------------------------------#
# 6. A Program to find out the maximum number from a list
#------------------------------------------------------------------------------------------------#

# numbers_list = [0, 12, 89, 66, 596, 44]
# max_number = 0
# for number in numbers_list:
#     if number > max_number:
#         max_number = number
# print(f"Max number : {max_number}")


#*************************************************************************************************#
# 2Dimensional LIST :
#*************************************************************************************************#


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # print(matrix[0])  # it will print [1, 2, 3] list
# # print(matrix[1])  # it will print [4, 5, 6] list
# # print(matrix[2])  # it will print [7, 8, 9] list

# print(matrix[0][2])  # it will print "3" in first list, item from index == "2"

# for raw in matrix:
#     for item in raw:
#         print(item)

#------------------------------------------------------------------------------------------------#
# 1. List methods/functions :
#------------------------------------------------------------------------------------------------#

# numbers = [5, 7, 6, 7, 8, 4]

# # To append/add a new item to an existing list at the end of the list
# numbers.append(11)
# # To add/insert a new item to an existing list at anywhere in the list
# numbers.insert(1, 24)
# print(numbers)

# numbers.remove(24)  # To remove a sepecific item from list with the same value
# print(numbers)

# # numbers.clear()  # To clear/remove whole list
# # print(numbers)

# numbers.pop()  # To remove the last item from a list.
# print(numbers)

# # Prints the index of first occurrence of "7" from the list
# print(numbers.index(7))

# # Print the occurrence of an item in the list
# print(numbers.count(7))

# # print the list after performing a sort operation over the list, always sort in ASCENDING order
# numbers.sort()
# print(numbers)

# # print the list after performing reverse operation which will display list in DESCENDING order
# numbers.reverse()
# print(numbers)

# # It copies the items of numbers to cpynumber variable
# cpynumber = numbers.copy()
# print(cpynumber)

#------------------------------------------------------------------------------------------------#
# 2. A Program to remove duplicate entries from the list
#------------------------------------------------------------------------------------------------#

# numbers = [5, 7, 6, 7, 8, 4]

# newlist = []
# for number in numbers:
#     if number not in newlist:
#         newlist.append(number)
# print(newlist)

#*************************************************************************************************#
# TUPLES :
#*************************************************************************************************#

# # A tuple can't be modified to perform add/remove operations
# # It's called immutable type parameter
# numbers = (5, 7, 6, 7, 8, 4)
# print(numbers.index(4))  # To get the index of an existing item in tuple

#*************************************************************************************************#
# UNPACKING : It works same for LISTs & TUPLEs
#*************************************************************************************************#

# # FOR TUPLES :
# coordinates = (1, 2, 3)
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
# x, y, z = coordinates  # instead of writing above old fashion syntax, PYTHON allows to create & assign values to variables in the following manner
# print(x, y, z)

# # FOR LISTS :
# coordinates = [4, 5, 6]
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
# x, y, z = coordinates  # instead of writing above old fashion syntax, PYTHON allows to create & assign values to variables in the following manner
# print(x, y, z)

#*************************************************************************************************#
# DICTIONARIES :
#*************************************************************************************************#

# # Dictionary can have any kind of value containing but dictionary must have unique keys.
# customer = {
#     "name": "John",
#     "email": "john@gmail.com",
#     "phone": "+910020010210",
#     "is_married": True,
#     "age": 25
# }

# # Print a name fetched from dictionary, user can write in the following manner to get the value of specific key
# print(customer["name"])

# # It won't give an error if the key doesn't exist in the dictionary. Instead of giving an error, it will return None as object.
# # Because it PYTHON, None is considered as an object with no value
# print(customer.get("birthday"))

# # We can set default value for the key if the key doesn't exist in the given dictionary.
# # it will simple print the given default value instead of printing None
# print(customer.get("birthday", "Jan 20, 1987"))

#------------------------------------------------------------------------------------------------#
# Example : A Program to print the user given phone number in WORD format
#------------------------------------------------------------------------------------------------#

# phone = input("Phone : ")
# dict_number = {
#     "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
#     "6": "six", "7": "seven", "8": "eight", "9": "nine"
# }
# strnumber = ""
# for p in phone:
#     #strnumber += f"{dict_number[p]} "
#     # To avoid an error if the keyword doesn't exist in dictionary
#     strnumber += f"{dict_number.get(p)} "
# print(strnumber.upper())

#------------------------------------------------------------------------------------------------#
# Emoji Converter : Without reusable function
#------------------------------------------------------------------------------------------------#

# message = input("> ")
# words_list = message.split(" ")

# # To get emoji list, press CONTROL, COMMAND & SPACE on MAC
# dict_emoji = {
#     ":)": "😊",
#     ":(": "😌",
# }

# output = ""
# for word in words_list:
#     output += f"{dict_emoji.get(word, word)} "
# print(output)

#------------------------------------------------------------------------------------------------#
# Emoji Converter : With reusable function
#------------------------------------------------------------------------------------------------#

# def emoji_converter(message):
#     words_list = message.split(" ")
#     # To get emoji list, press CONTROL, COMMAND & SPACE on MAC
#     dict_emoji = {
#         ":)": "😊",
#         ":(": "😌",
#     }
#     output = ""
#     for word in words_list:
#         output += f"{dict_emoji.get(word, word)} "
#     return output


# message = input("> ")
# print(emoji_converter(message))

#*************************************************************************************************#
# EXCEPTIONS :
#*************************************************************************************************#

# EXIT 0 means a program has been executed successfully

# # A TRY: EXCEPT: statement to handle the exception in PYTHON language
# try:
#     age = int(input("Age: "))
#     income = int(input("Income: "))
#     risk = income / age
#     print(age)
#     print(f"Risk : {risk}")
# except ValueError: # An exception hanlder if invalid type of value entered by the user
#     print("Invalid value has been entered")
# except ZeroDivisionError: # A hanlder to get any arithmetic exception
#     print("Age can't be zero")


#*************************************************************************************************#
# CLASSES :
#*************************************************************************************************#

# # Classes are used to model the real world concept
# # In PYTHON, classes name should be in Capitalised manner like "EmailClient"
# # Class simply creates a blue print of Objects to be created

# class Point:
#     def draw(self):
#         print("Draw")

#     def move(self):
#         print("Move")


# point1 = Point()
# # these variables are only valid for point1 class instance, it won't be allowed to access by other class instance until it's declared inside the class
# point1.x = 29
# point1.y = 34
# point1.draw()
# print(f"Point: ({point1.x}, {point1.y})")

# point2 = Point()

#------------------------------------------------------------------------------------------------#
# Constructor inside class :
#------------------------------------------------------------------------------------------------#

# class Point:
#     # A constructor method to create/construct an object with passed parameters at the time of initialization
#     # As both the parameters/attributed are defined in constructor, they are accessible multiple instances of the same class
#     # But all instances will have different values based on given at the time of creation
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print("Draw")

#     def move(self):
#         print("Move")


# point1 = Point(10, 20)
# point1.x = 23  # We can change the value of attribute later on with the help of class instance variable
# print(f"Point: ({point1.x}, {point1.y})")

# point2 = Point(23, 30)

#------------------------------------------------------------------------------------------------#
# Excercise : Create A Person class with name as attribute and talk() as method
#------------------------------------------------------------------------------------------------#

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):  # Here, self is used to access the class attributes
#         print(f"Hi, I'm {self.name}")


# person1 = Person("Nilesh")
# name = input("Name : ")
# person1.name = name
# # print(person1.name)
# person1.talk()

#------------------------------------------------------------------------------------------------#
# Inheritance :
#------------------------------------------------------------------------------------------------#

# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     # To make PYTHON happy by ignoring error, because in PYTHON class must have values or a pass statement
#     # pass
#     def bark(self):
#         print("Bark")


# class Cat(Mammal):
#     pass


# dog = Dog()
# dog.walk()
# dog.bark()

# cat = Cat()
# cat.walk()

#*************************************************************************************************#
# PACKAGES :
#*************************************************************************************************#

# import ecommerce.shipping  # importing a module in PYTHON
# # calling a method from a file of a imported module
# ecommerce.shipping.calculate_shipping_cost()

# # second approach of importing a function from a module of a package.
# calculate_shipping_cost()

# # user can also import only module from a package and then module will be used to access the methods inside the module.
# shipping.calculate_shipping_cost()

#*************************************************************************************************#
# MODULES :
#*************************************************************************************************#

# To check the list of in-built modules in PYTHON, search for "python 3 module index" in google
# https://docs.python.org/3/py-modindex.html
# modules may differ based on PYTHON version

#------------------------------------------------------------------------------------------------#
# By importting whole module :
#------------------------------------------------------------------------------------------------#

# # Files called as modules to organize code in well mannered and place in mulitple sections
# # Imported file/module called "converters" to utilised the weight converting reusable functions
# import converters

# try:
#     weight = float(input("Weight in (K)g : "))
#     print(f"Your weight in (L)bs : {converters.kgs_to_lbs(weight)}")
#     weight = float(input("Weight in (L)bs : "))
#     print(f"Your weight in (K)g : {converters.lbs_to_kgs(weight)}")
# except ValueError:
#     print("Please enter valid weight")

#------------------------------------------------------------------------------------------------#
# By importting specific functions from the module :
#------------------------------------------------------------------------------------------------#

# # instead of importing whole module, user can import a specific function from that module
# # after writing "from module_name import" press CONTROL + SPACE to see the list of functions available in module
# from converters import kgs_to_lbs
# from converters import lbs_to_kgs

# try:
#     weight = float(input("Weight in (K)g : "))
#     print(f"Your weight in (L)bs : {kgs_to_lbs(weight)}")
#     weight = float(input("Weight in (L)bs : "))
#     print(f"Your weight in (K)g : {lbs_to_kgs(weight)}")
# except ValueError:
#     print("Please enter valid weight")

#------------------------------------------------------------------------------------------------#
# A program to find max number from the given list with the help of importing a specific function
# from the module to perform the operation
#------------------------------------------------------------------------------------------------#

# from utils import find_max_from_list

# numbers = [12, 15, 58, 96, 56, 12, 2]
# print(f"Max number from the given list : {find_max_from_list(numbers)}")

#------------------------------------------------------------------------------------------------#
# By importting in-build module called RANDOM :
#------------------------------------------------------------------------------------------------#

# import random

# for i in range(3):
#     print(random.random()) # To generate any random value

# for i in range(3):
#     print(random.randint(11, 20)) # To generate random value between 11-20

#------------------------------------------------------------------------------------------------#
# A program to fetch any random team member from the list and to make him/her as team lead
#------------------------------------------------------------------------------------------------#

# members_list = ["John", "Peter", "Roy", "Jack", "Brad"]
# leader = random.choice(members_list)
# print(leader)

#------------------------------------------------------------------------------------------------#
# A program to fetch random values through tuple
#------------------------------------------------------------------------------------------------#

# import random

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         # In python, it user wants to return a tuple from a function then 
#         # there's no need of paranthesis around the parameters 
#         # like 'return first, second' instead return (first, second)
#         return (first, second) 


# dice = Dice()
# print(dice.roll())

#*************************************************************************************************#
# FILES & DIRECTORIES :
#*************************************************************************************************#

# # pathlib : Object Oriented FileSystem Path

# # here, pathlib is a library and 'Path' is a class
# from pathlib import Path 

# # Absolute path : 
# # Root of a harddisk (c:\Program Files\Microsoft) - For Windows machines
# # Root of a harddisk (/usr/local/bin) - For MAC machines
# # Relative path : A path starting from a current directory

# # Path() # This will reference a current directory if we don't pass any arguments to this 
# # path = Path("ecommerce") # it will refer a file / directory
# # print(path.exists()) # To check whether the path exists or not

# # # if you want to create a new directory in project then need to execute the below commands :
# # path = Path("emails") 
# # print(path.mkdir())
# # # if you want to delete the directory from a project then need to execute the below commands : 
# # print(path.rmdir()) 

# # To fetch and iterate each file & directory from a current directory
# path = Path()
# print(path.glob("*")) # here, "*" means all kind of files & directory
# # here, "*" means obl kind of files with any kind of the extension or 
# # instead "*", you can also pass a sepecific type of a file to get only those kind of files
# print(path.glob("*.*")) 
# print(path.glob("*.py")) 

# # To fetch the list of file along with the name of files
# for file in path.glob("*.py"):
#     print(file)

# # To fetch the list of file & directories and their names
# for file in path.glob("*"):
#     print(file)

#-------------------------------------------------------------------------------------------------#
# Import and call a function to write data along with charts in files
#-------------------------------------------------------------------------------------------------#

# from utils import process_workbook
# # Call function with argument to override the changes into an existing file
# process_workbook("transactions.xlsx") 
