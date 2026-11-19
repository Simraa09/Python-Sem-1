# Create a list of 10 nos...
lst = [1,2,3,4,5,6,7,8,9,10]

# Print the sum of last 4 elements of the list...
sum = 0
for i in range(len(lst)-4, len(lst)):
    sum += lst[i]
print("Sum of Last 4 elements: ", sum)

# Find the difference between the maximum and minimum element of the list...
max = max(lst)
min = min(lst)
print("Difference between max and min number: ", max-min)

# Insert a no. in a list at 6th position. This no. must be 1/3rd of the no. stored at 4th position...
element = lst[4]//3
print("Before: ",lst)
lst.insert(6, element)
print("After: ", lst)


