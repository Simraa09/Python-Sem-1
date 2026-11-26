# Default Parameter
def my_function(name = "friend"):
    print("Hello", name)
my_function("Trisha")
my_function()


# Keyword argumnet
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function( name = "Lucky", animal = "Cat")


# Position Only Parameter
def my_function(name, /):
    print("Hello", name)
my_function("Jayashree")
#my_function(name = "Viraj")


# Keyword only parameter
def my_function(*, name):   
    print("Hello", name)
my_function(name = "Vihan")
#my_function("Ajay")


# Local variable available inside that function only
def myfunc():
    i = 300
    print(i)
myfunc()