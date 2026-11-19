# Create a list of nos and strings and set the values from user
# Separate the list from the max no. 

lst = []
n = 6
for i in range(n//2):
    x = int(input("Enter a number: "))
    y = input("Enter a name: ")
    lst.append(x)
    lst.append(y)
print(lst)
for i in range(len(lst)+1):
    if i.isnum():
        print(i)
max_no = max(lst)
print(max_no)
max_index = lst.index(max_no)
print(max_index)