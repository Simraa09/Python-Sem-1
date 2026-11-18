sentence = input("Enter a sentence: ").upper()
vowels = 'aeiouAEIOU'
hm = {}
for i in sentence:
    if i in vowels:
        hm[i] = hm.get(i,0)+1
for i in hm:
    print(i,":",hm[i])