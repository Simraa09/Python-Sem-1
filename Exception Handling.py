# ZeroDivisionError -> Divide by zero
# ValueError        -> Wrong data type input
# NameError         -> Undefined variable
# IndexError        -> List index out of range
# FileNotFoundError -> Missing file
# TypeError         -> Invalid operation

# Try: The try block lets you test a block of code for errors.
# Except: The except block lets you handle the error.
# Else: The else block lets you execute code when there is no error.
# Finally: The finally block lets you execute code, regardless of the result of the try - and except blocks.

try:
    num = int(input("Enter Number: "))
    print(100/num)
except:
    print("Some error occurred")
print()


try:
    print(x)
except:
    print("An exception occurred")
print()


# Simple example
try:
    print(x)
    print(str)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print()


# divide by 0
try:
    a = 10
    b = 0
    c = a / b
except:
    print("Cannot divide by zero")
print()


# Multiple exceptions
try:
    num = int(input("Enter Number: "))
    print(100/num)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid Input")
print()


# use of finally
try:
    print("Processing Transaction")
    amount = int(input())
    if amount > 10000:
        print("Transaction Approved")
except:
    print("Transaction Failed")
finally:
    print("Thank You")
print()


balance = 10000
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise Exception("Insufficient Balance")
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
print()


# One Block for Multiple Exceptions
try:
    num = int(input("Enter number: "))
    result = 100 / num
    print(result)
except (ValueError, ZeroDivisionError):
    print("Invalid operation.")
print()


# Using Else Block
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
print()


#Using Finally Block
try:
    file = open("test.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program completed.")
print()


# Else and Finally Together
try:
    num = int(input("Enter a number: "))
    result = 50 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Enter interger only.")
else:
    print("Result:", result)
finally:
    print("Thank you for using the program.")
print()


# Exception Object
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print("Exception Message:", e)
print()

# Password Validation
try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")
    print("Valid Password")
except ValueError as e:
    print(e)
print()

# Nested Try-Except
try:
    num = int(input("Enter number: "))
    try:
        result = 100 / num
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
print()


# Raising exception
age = int(input("Enter Age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
print("Eligible")
print()


# Printing Report
roll = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
marks = float(input("Enter Marks: "))
try:
    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100")
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"
except ValueError as e:
    print("Error:", e)
else:
    print("\nStudent Report")
    print("Roll No :", roll)
    print("Name :", name)
    print("Marks :", marks)
    print("Grade :", grade)
finally:
    print("Record Processing Completed")
print()
