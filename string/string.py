# 1. Create and Access
# Create a string containing your full name. Print:
# The complete string
# First character
# Last character
# First 5 characters
# Last 5 characters

name = "Divyanshi Sagal"

print("Complete name:",name)
print("First character:",name[0])
print("Last character:",name[-1])
print("First 5 character:",name[:5])
print("Last 5 character:",name[-5:])

# 2. String Length
# Take a string from the user and find its length using len().

string_1 = input("Enter a string: ")

print("Length of string:",len(string_1))

# OR

length = 0

for char in string_1:
    length += 1 

print("Length of string:",length)

# 3. String Indexing
# Given:
# text = "Python Programming"
# Print the characters at index:
# 0
# 3
# 7
# -1
# -5

text = "Python Programming"

print(text[0])
print(text[3])
print(text[7])
print(text[-1])
print(text[-5])

# 4. String Slicing
# Given:
# text = "Python Programming"
# Use slicing to print:
# "Python"
# "Programming"
# The string in reverse
# Every second character
# Every third character

text = "Python Programming"

print(text[0:6])
print(text[7:18])
print(text[::-1])
print(text[::2])
print(text[::3])

# 5. Case Conversion
# Take a string from the user and display it in:
# Uppercase
# Lowercase
# Title Case
# Capitalized form
# Swapcase
# Use appropriate string methods. 

string_2= input("Enter a string: ")

print("Uppercase:",string_2.upper())
print("Lowercase:",string_2.lower())
print("Title Case:",string_2.title())
print("Capitalized form:",string_2.capitalize())
print("Swapcase:",string_2.swapcase())

# 6. Remove Extra Spaces
# Given:
# text = "   Python Programming   "
# Remove the extra spaces from both sides and print the cleaned string.
# Also demonstrate the difference between:
# strip()
# lstrip()
# rstrip()

text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

# 7. Search Inside a String
# Given:
# text = "Python is easy and Python is powerful"
# Find:
# The position of the first occurrence of "Python"
# The position of the first occurrence of "easy"
# How many times "Python" appears
# Use appropriate string methods.

text = "Python is easy and Python is powerful"

print(text.find("Python"))
print(text.find("easy"))
print(text.count("Python"))

# 8. Replace Characters/Words
# Given:
# text = "I love Java. Java is easy."
# Replace every occurrence of "Java" with "Python".
# Then print the updated string.

text = "I love Java. Java is easy."

print("Updated string:",text.replace("Java", "Python"))

# 9. Split and Join
# Given:
# text = "Python is a powerful programming language"
# Convert the string into a list of words using split().
# Join the words using -.
# Join them again using a space.

text = "Python is a powerful programming language"

word_1 = text.split()
print("List:",word_1)

word_2 = text.split()
print("Using -:","-".join(word_2))

word_2 = text.split()
print("Using space:"," ".join(word_2))

# 10. Check String Content
# Take a string from the user and check whether it contains:
# Only alphabets
# Only digits
# Alphanumeric characters
# Only spaces
# Uppercase characters
# Lowercase characters
# Use appropriate is...() string methods.

string_3 = input("Enter a string: ")

w1 = string_3.isalpha()
print("Only alphabets:",w1)

w2 = string_3.isdigit()
print("Only digits:",w2)

w3 = string_3.isalnum()
print("Alphanumeric characters:",w3)

w4 = string_3.isspace()
print("Only spaces:",w4)

w5 = string_3.isupper()
print("Uppercase characters:",w5)

w6 = string_3.islower()
print("Lowercase characters:",w6)

# 11. Count Vowels and Consonants
# Take a string from the user and count:
# Number of vowels
# Number of consonants
# Number of digits
# Number of spaces
# Ignore special characters.

string_4 = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in string_4:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
  
print("Number of vowels",vowels)
print("Number of consonants",consonants)
print("Number of digits",digits)
print("Number of spaces",spaces)

# 12. Reverse a String
# Take a string from the user and reverse it without using any built-in reverse function.
# Example:
# Input: Python
# Output: nohtyP

string_5 = input("Enter a string: ")

print("Reverse string:",string_5[::-1])

# 13. Palindrome String
# Write a program to check whether a string is a palindrome.

# Example:

# Input: madam
# Output: Palindrome

# Input: python
# Output: Not Palindrome

# Try solving it using string slicing.

string_6 = input("Enter a string: ")

original_string = string_6
reverse_string = string_6[::-1]

if original_string == reverse_string:
    print("Palindrome")
else:
    print("Not Palindrome")    

# 14. Count Character Frequency
# Given:
# text = "programming"
# Count how many times each character occurs.
# Expected output should be similar to:

# p : 1
# r : 2
# o : 1
# g : 2
# a : 1
# m : 2
# i : 1
# n : 1

# Hint: You can use a dictionary.

text = "programming"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for key, value in frequency.items():
    print(key,":",value)           

# MINI PROJECT - Username & Password Validator ⭐
# Create a program that takes a username and password from the user.

# Validate that:

# Username contains only letters and numbers.
# Username has at least 5 characters.
# Password has at least 8 characters.
# Password contains at least one uppercase letter.
# Password contains at least one lowercase letter.
# Password contains at least one digit.

# Print "Valid credentials" if all conditions are satisfied; otherwise print the appropriate error message.

username = input("Enter the username: ")
password = input("Enter the password: ")

if not username.isalnum():
    print("Username only contains letters and numbers.")
elif len(username) < 5:
    print("Username must have at least 5 characters.")
elif len(password) < 8:
    print("Password must have at least 8 characters.")
elif not any(char.isupper() for char in password):
    print("Password must contains at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password must contains at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
else:
    print("Valid credentials")




















































