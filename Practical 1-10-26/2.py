#Print square of first N numbers staring from S
S = int(input("Enter a number: "))
N = int(input("Enter the limit: "))

for i in range (S,S+N):
    print(i,": ", i**2)