# use of *args
def my_fun(*args):
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
    print("\n Argument Type is :", type(args))
my_fun(12,23,"jay")
print()


# Find Maximum Value
def get_max(*num):
    if len(num) == 0:
        return None
    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n
    return max_num
print(get_max(3, 12, 32, 9, 21))
print(get_max('arush','Payal','zarina','Yogesh'))
print()


# using **kwrgs
def new_fun(**myvar):
    print("Argument Type is :", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
new_fun(name = "Tejas", age = 21, city = "Pune")
print()


# combining regular arguments with args and kwargs
def my_function(title, *args, **kwargs):
 print(title)
 print("CR is ",args[0], "\nLR is ",args[1])
 print("Positional arguments:", args)
 print("Keyword arguments:", kwargs)
# my_function("Div B Info", "Vaibhav", "Sonal", age = 25, city = "Pune")
my_function("Div A Info","Chintamani","Bhavya", age = 24, city = "Pune")
print()



# demo of LEGB rule
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", x)
print()


# Using Global
x = "global"
def change_global():
    global x
    x = "modified by global"
change_global()
print(x) 
print()


# Using Non local
def outer():
    x = "enclosing"
    #y = 3
    def inner():
        nonlocal x
        x = "modified by nonlocal"
    inner()
    print("Outer:", x)
outer()
print()


#without global or nonlocal
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", x)
print()


# Nested Function
def outer():
    message = "Hello from outer"
    def inner():
        print(message)
    inner()
outer()
print()


def operation_factory(op):
    def add(a, b): return a + b
    def mul(a, b): return a * b
    if op == "add":
        return add
    else:
        return mul
f = operation_factory("mul")
print(f(3, 4)) 
print()


# pass function as argument
def add(x, y):
    return x + y
def mul(x,y):
    return "Mulipliaction is ", x*y
def calculate(func, x, y):
    return func(x, y)
result = calculate(add, 8, 20)
res = calculate(mul,4,5)
print("Addition is ",result)
print(res)
