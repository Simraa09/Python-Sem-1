#Print the star pyramid pattern
n = int(input("Enter number: "))
for i in range (1,n+1):
    print(" " * (n-i), end="")
    for j in range (1,i+1):
        print("*", end=" ")
    print()

#Print the alternate star pyramid pattern
n = int(input("Enter number: "))
symbol = "*"
for i in range (1,n+1):
    if i%2 != 0:
        symbol = "*"
    else:
        symbol = "@"
    print(" " * (n-i), end="")
    for j in range (1,i+1):
        print(symbol, end=" ")
    print()
