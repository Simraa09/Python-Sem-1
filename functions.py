def func(a, b):
    div = a // b
    rem = a % b
    return div, rem

a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
div, rem = func(a,b)
print(a, " divided by ", b , " = ", div, " and remainder is ", rem)


