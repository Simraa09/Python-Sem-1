s = 'Simraa'
print(max(s))
print(min(s))
print(sorted(s))

s = "Hello Simraa! Welcome to World."

# Converts to uppercase
print("Upper: ", s.upper())

# Converts to lowercase
print("Lower: ", s.lower())

# Capitalizes first letter only
print("Capitalize: ", s.capitalize())

# Capitalizes first letter of every word
print("Title: ", s.title())

# Swaps uppercase and lowercase
print("Swapcase: ", s.swapcase())

# Removes spaces from both ends
s2 = "     Hello Simraa! Welcome to World.     "
print("Strip: ", s2.strip())

# Removes specified characters from ends
print("Strip characters: ", s.strip("H"))

# Counts occurrences of a character
print("Count 'o': ", s.count("o"))

# Finds position of substring (-1 if absent)
print("Find 'Simraa': ", s.find("Simraa"))

# Replaces a word
print("Replace: ", s.replace("World", "Python"))

# Splits into list of words
print("Split words: ", s.split())

# Converts string into list of individual characters
print("List of letters: ", list(s))

# Converts to letters without spaces
print("Letters without spaces: ", list(s.replace(" ", "")))