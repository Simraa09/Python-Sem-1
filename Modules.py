# • To create a module just save the code in a file with the file extension .py
# • Use import statement to use the module
# • To use function from module syntax is module_name.function_name

import mymodule as m
m.greet_person('jay')
m.change_case('We are Testing Change CASE ')
print()


# import a specific components
from mymodule import greet_person
greet_person('jayashree')
print()


# Math module
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
print()


#  math module additional functions
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
print("Factorial is " ,math.factorial(5))
print("Square root is ", math.sqrt(625))
print()


# RANDOM MODULE
# randint(a,b)  -> Random integer
# random()      -> Random float between 0 and 1
# choice(seq)   -> Random element
# shuffle(list) -> Shuffle list

# Random module
import random
x=random.randint(1,10)
subject = ("Python","ADBMS", "DSA")
mychoice=random.choice(subject)
print(mychoice)
print(x)
print()

# DATETIME MODULE
# date.today()   -> Current date
# datetime.now() -> Current date and time
# timedelta()    -> Date arithmetic

#Date time module
import datetime as d
print(d.date.today())
print(d.datetime.now())
print(d.timedelta())
print()


from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta(days=10) # 10 days in the future
past_date = now - timedelta(hours=5) # 5 hours in the past
print("After 10 Days ",future_date)
print("5 hrs before", past_date)
date1 = datetime(2026, 11, 1)
date2 = datetime(2026, 12, 16)
interval = date2 - date1
print(interval) 
print()


# LAMDA FUNCTIONS
# map () -> Transform each element
#        -> Iterable of modified values
# filter () -> Select elements meeting a condition
#           -> Iterable of filtered values
# Reduce () -> Combine elements into one value
#           -> Single value

# Functional programming map()
# Double the number
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))
print(result)
print()

# change to upper case
names = ["amit", "raj", "neha"]
result = list(map(str.upper, names))
print(result)
print()


# Functional programming filter()
# Print even numbers
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
print()

# print number greater than 50
nums = [20, 55, 80, 15, 60,54,89]
result = list(filter(lambda x: x > 50, nums))
print(result)
print()


from functools import reduce
# sum of numbers
nums = [1, 2, 3, 4,-7]
result = reduce(lambda x, y: x + y, nums)
print(result)