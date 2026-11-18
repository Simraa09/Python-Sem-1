# Count the number of each vowel in the sentence
sentence = input("Enter a sentence: ")
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for i in sentence:
    if i in "aA":
        count_a += 1
    elif i in "eE":
        count_e += 1
    elif i in "Ii":
        count_i += 1
    elif i in "Oo":
        count_o += 1
    elif i in "Uu":
        count_u += 1

print("No of A: ",count_a)
print("No of E: ",count_e)
print("No of I: ",count_i)
print("No of O: ",count_o)
print("No of U: ",count_u)