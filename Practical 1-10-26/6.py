#Reverse the list
lst = [1,2,3,4,5,6,7]
reverse = []
for i in range(len(lst)-1,-1,-1):
    reverse.append(lst[i])
print(reverse)