# Generators are functions that can pause and resume their execution.
# • When a generator function is called, it returns a generator object, which is an iterator.
# • The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
# • Generators allow you to iterate over data without storing the entire dataset in memory.
# • Instead of using return, generators use the yield keyword

# The yield keyword is what makes a function a generator.
# • When yield is encountered, the function's state is saved, and the value is returned.
# • The next time the generator is called, it continues from where it left off.
# • You can manually iterate through a generator using the next() function
# • When there are no more values to yield, the generator raises a StopIteration exception

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for i in count_up_to(5):
    print(i)
print()


# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)
print()


# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)
# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
print()


# Fibonacci
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Get first 10 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
    print(next(gen))
print()

