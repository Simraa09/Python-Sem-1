s = 'Simraa'
x = ''
for i in s:
    if i in 'aeiou':
        x += i.replace(i,'z')
    else:
        x += i
print(x)

print("Sam, Sara, Ram, Rima, Ramis, Asma, Asra, Isra")