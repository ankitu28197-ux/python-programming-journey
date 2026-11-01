# Create a string with your name and display its length and datatype
a = "Ankit"
print(len(a))
b = type(a)
print(b)

# print the first and last character of the string "Data science"

a = "Data science"
print(a[0:12:11])
print(a[0:len(a):11])

# using negative indexing print the third character from the end of the string "Pymaster"

A = "Pymaster"
print(A[-3])

# Slice 'PROGRAMMING' to extract only "gram" 

a = "programming"
print(a[3:7:1])


# Reverse the string "INDIA" using slicing:-

a = "INDIA" 
print(a[::-1])


# Intermediate level questions :-

# Check eheather python is present in "I love python programming"

a = "I love python programming"
b = "python" in a
print(b)


# concatenate "hello" and "world" with a space beetween them

a = "hello" 
b = "world"
c = a + " " + b
print(c)

# Repeat '*' 20  times to create a seperator line:-

a = "*" * 20
print(a)

# extract every alternate character from "ABCDEFGHIJ"

a = "ABCDEFGHIJ"
print(a[0:11:2])

# From "Pymaster india" etract 'india' using slicing:-

a = "Pymaster india"
print(a[9:14:1])