# # • Write a program: input a number, print whether it is Positive, Negative, or Zero.
# # if (num > 0):
# #     print("positve number")
# # elif (num <0):
# #     print("Negative number")
# # else:
# #     print("zero")



# # • Build a simple ATM check: if withdrawal amount <= balance fi success, else fi 'Insufficient funds'

# # Withdrawl = int(input("Enter the withdrawl amount" ))
# # balance = 10000
# # balance = balance = Withdrawl
# # print("success" if Withdrawl <= balance else "Fail")

# # WAP  in which convert if/elif/else into match case:-

# age = int(input("Enter the age: "))

# if age>18 and age<30:
#   print("you are eligible to vote")
# elif age > 30 and age < 60:
#   print("you area an adult")
# elif age > 60 and age < 100:
#   print("You are an old person")
# else:
#   print("you are just a kid bro")


# MATCH CASE:-

# age = int(input("Enter your age: "))

# match age:
#   case age<=30:








# Homework (post answers in comments):
# • Print the sum of numbers from 1 to 100 using a loop

#total = 0
# for i in range(1,101):
#   total = total + i
    # print("sum =" total)

# • Print only even numbers from 1 to 20 using continue.

# for i in range (1,21):
  
#   if i%2!=0:
#     continue
#   print(i)


# • Take a number and check if it is prime, using a loop with break.


# num = int(input("enter a number: "))

# if num <2:
#   print("it is not a prime number")
# else:
#   for i in range(2,num):
#     if num%i == 0:
#       print("it is not an prime number")
#       break
#     else:
#       print('it is a prime number')
  
# WAP to find the facors of n using while loop:-

# n = int(input("Enter a number: "))
# i = 1

# while i<=n:
#   if n%i==0:
#     print(i)
#   i = i+1


# SQUARE PATTERN using NESTED LOOPS :-

# for i in range(4):
  
#   for j in range(5):
#     print("*",end='')
    
#   print("\n")

# icreasing TRIANGLE PATTERN using NESTED LOOPS:-

# for i in range(6):
#   for j in range(i):
#     print("*", end="")
#   print()


#decreasing TRIANGLE using nested loops:-

# for i in range(4):
#   for j in range(i):
#     print(" ",end='')
#   for k in range(4-i):
#     print("*",end='')
#   print()

# alphabetic TRIANGLE pattern using NESTED loops:-

# for i in range(5):
#   for j in range(i+1):
#     print(chr(65+i), end='')
#   print()
