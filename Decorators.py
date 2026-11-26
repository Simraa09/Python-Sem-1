# Decorator simple example
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()
print()


# Demo of decorator part 1
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()
print()


#Demo of decorator part 2
def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")
        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")

# decorate the ordinary function
decorated_func = make_pretty(ordinary)
# call the decorated function
decorated_func()
print()


# Decoartor with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print("Hello", name)
greet("Students")
print()


# Instead of assigning the function call to a variable,
# Python provides a much more elegant way to achieve this functionality using
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary() 