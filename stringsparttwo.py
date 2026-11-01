# # # # STRIGS METHOS :-

# # # #Convert "pymaster india"  in to uppercase and title case then print both :-

# # # a = "pymaster india"
# # # b = a.upper()
# # # c = a.title()
# # # print(b,c)


# # Q2. Remove spaces from ' clean this ' using strip(). Verify with len().

# a = " clean this "
# b = a.strip()
# print(b)
# print(len(a))
# print(len(b))


# # Q3. Check if the string '12345' is all digits. Check if 'hello123' is all alph

# a = "12345"
# print(a.isdigit())
# print("heloo123".isalpha())


# # Q4. Replace 'bad' with 'good' in 'This is bad code with bad habits'.

# a = " This is bad code wiyh bad habits"
# print(a.replace("bad" , "good"))

# # Q5. Split 'one:two:three' on ':' and print the resulting list.

# a = "one:two:three"
# b = a.split(":")
# print(b)


# # Q6. Join ['Python', 'is', 'fun'] with a space separator.

# a = ["Python", "is", "fun"]
# print(" ".join(a))

# # Q7. Check if 'Python' starts with 'Py' and ends with 'on'.

# a = "Python"
# print(a.startswith("Py"))
# print(a.endswith("on"))

# # Q8. Print your name right-aligned in a field of width 30 using rjust().

# name = "Ankit"
# print(name.rjust(30))


# # Q9. Zero-pad the number string '7' to width 4.

# num ="7"
# print(num.zfill(4))


# # Q10. Use an f-string to display: 'My name is X and my score is Y.2f'

# name = "X"
# score = "Y.2f"
# print(f"My name is {name} and my score is {score}")


# Intermediate level questions :-

# Q11. Find the index of 'India' in 'PyMaster India'. Use both find() and index().

# a = "Pymaster India"
# b = a.find("India")
# print(b)
# c = a.index("India")
# print(c)


# Q12. Count how many times 'an' appears in 'banana'. Count 'a' too.

# a = "banana"
# b = a.count("an")
# c = a.count("a")
# print(b,c)



# Q13. Split the CSV string 'Rajeev,25,Varanasi,Python' into a list and print each value on a new line.

# a = "Rajeev,25,Varanasi,python"
# b = a.split(",")
# print(b)
# for b in b:
#   print(b)


# Q14. Use .format() to display a formatted invoice: Item, Quantity, Price in columns.

# print("{:<15} {:<10} {:<10}".format("Item", "Quantity", "Price"))
# print("{:<15} {:<10} {:<10}".format("Pen", 2, 20))
# print("{:<15} {:<10} {:<10}".format("Notebook", 3, 150))
# print("{:<15} {:<10} {:<10}".format("Pencil", 5, 25))


# Q15. Strip all '*' characters from '***hello world***' using strip().

# a = "***hello world***"
# print(a.strip("*"))
# # Q16. Check if user input (simulate with a variable) is a valid integer using isdigit().

# user_input = "1234"

# if user_input.isdigit():
#   print("Valid number")
# else:
#   print("invalid numer")



# Q17. Use swapcase() on 'PyMaster India' and explain what happened.

# a = "pyMaster India"
# print(a.swapcase()) # all the small letters are swapped into capital and capital letters words are swapped into small letters , this happens.


# Q18. Using only find() (no 'in'), write a function that returns True if substring exists.

a = "i love ankit"
b = a.find("love")

if b in a:
  print("true")
else:
  print("false")
# Q19. Split 'a::b::c' on '::' and rejoin with ' | '.
# Q20. Format the number 1234567.89 with commas and 2 decimal places using f-string.