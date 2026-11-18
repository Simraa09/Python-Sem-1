#Print sum if first 10 even numbers
sum = 0
for i in range(0,11):
    if i % 2 == 0:
        sum += i
print("Sum: ", sum)