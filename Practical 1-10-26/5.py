#Remove the duplicates from the list
lst = [1,2,3,4,5,1,2,3]
new_lst = []
for i in lst:
    if i in new_lst:
        continue
    new_lst.append(i)
print("With logical code: ",new_lst)

#optimum code
lst2 = [1,2,3,2,5,6,1]
new_lst2 = list(set(lst2))
print("With optimum code: ",new_lst)