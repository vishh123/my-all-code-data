
# ? (Q.1) Write a program that categorizes a person's age into different life stages based on the following conditions:

# 0-2 years: Infant
# 3-12 years: Child
# 13-19 years: Teenager
# 20-65 years: Adult
# Above 65 years: Senior

# age=int(input("enter the age ::"))
# if age<=2:
#   print("Infant")

# elif age<=12:
#   print("Child")

# elif age<=19:
#   print("Teenager")

# elif age<=65:
#   print("Adult")

# else:
#   print("Senior")


# ? (Q.2) Write a program that suggests an activity based on the current temperature (in Celsius), following these guidelines:

# Above 30°C: "It's hot. Let's go swimming!"
# 20°C to 30°C: "Perfect for a picnic."
# 10°C to 19°C: "Maybe wear a jacket?"
# Below 10°C: "Too cold! Best to stay indoors."
  
# temp=int(input("enter the temprature ::"))
# if temp>30:
#   print("It's hot. Let's go swimming!")

# elif temp>=20 and temp<=30:
#   print("Perfect for a picnic.")

# elif temp>=10 and temp<=19:
#   print("Maybe wear a jacket?")

# else:
#   print("Too cold! Best to stay indoors.")


#? (Q.3)Write a program that takes three numbers as input and prints the largest number.
#! Note: Do not use an array

# num_1=int(input("enter 1st number ::"))
# num_2=int(input("enter 1st number ::"))
# num_3=int(input("enter 1st number ::"))

# if num_1>num_2 and num_1>num_3:
#   print(num_1,"is greater number")

# elif num_2>num_1 and num_2>num_3:
#   print(num_2 ,"is greater number")

# else:
#   print(num_3 ,"is greater number")
  
# ?(Q,4) Write a program that takes three numbers as input and prints the numbers in ascending order.
#! Note: Do not use an array

# num1 = int(input("enter your first value ::"))
# num2 = int(input("enter your second value ::"))
# num3 = int(input("enter your third value ::"))

# if num1<num2 and num1<num3:
#   if num2<num3:
#     print(num1)
#     print(num2)
#     print(num3)
#   else:
#     print(num1)
#     print(num3)
#     print(num2)
# elif num2<num1 and num2<num3:
#   if num1<num3:
#     print(num2)
#     print(num1)
#     print(num3)
#   else:
#     print(num2)
#     print(num3)
#     print(num1)
# elif num3<num1 and num3<num2:
#   if num1<num2:
#     print(num3)
#     print(num1)
#     print(num2)
#   else:
#     print(num3)
#     print(num2)
#     print(num1)

# ?(Q.5) Write a program to calculate the factorial of a given number n.
# ! NOTE:The factorial of a number n is the product of all positive integers less than or equal to n

# n = int(input("enter the value ::"))
# fact =1
# i=n
# while i>0:
#   fact=fact*i
#   i=i-1
# print(fact)
    
# ? (Q.6) Write a program that takes a number n as input and prints all the factors of the number.
#!  Note: The factors need to be printed in the same line, separated by a blank space.

# n=int(input("enter the value :: "))
# i=1
# while i<=n:
#   if n%i==0:
#     print(i, end=" ")
#   i=i+1

# ? (Q.7) Write a program that calculates the sum of all the digits in a given number n.

# n= int(input("enter the value :: "))
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem
#   n=n//10
# print(sum)

# ? (Q.8) Write a program that takes a Binary Number B as input and prints the Decimal equivalent of the given input

# b=int(input("enter the value ::"))
# i=0
# sum=0
# # todo by while loop
# while b>0:
#   rem=b%10
#   sum+=rem*(2**i)
#   b=b//10
#   i+=1
# print(sum)
#todo  NOTE : by for loop
# for i in range (b):
#   rem=b%10
#   sum+=rem*(2**i)
#   b=b//10
# print(sum)

# ? (Q.9)Write a program that takes a number n as input and prints the first n terms of the Fibonacci Series.

#! NOTE: The Fibonacci Series is a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1

# n=int(input("enter the value ::"))
# x=0
# y=1
# z=0
#todo by while
# while n>0:
#   print(z)
#   x=y
#   y=z
#   z=x+y
#   n-=1

# todo by for 
# for i in range (n):
#   print(z, end=" ")
#   x=y
#   y=z
#   z=x+y

# ? (Q.10) Write a program that takes a number n as input and prints the reverse of the given number.
# n=int(input("enter the value ::"))
# rev=0
# while n>0:
#   rem=n%10
#   rev=rev*10+rem
#   n=n//10
# print(rev)
#todo by for loop
# sum = 0
# for i in range(len(str(n))):
#   t = n%10
#   sum = sum*10+t
#   n = n//10
# print(sum)

# ? (Q.11)You are given an integer n. Print yes, if it is an Armstrong Number. Print no, if it is not an Armstrong Number.

#! NOTE: An Armstrong Number is a positive number that equals the sum of its digits, each raised to the power of the number of digits
# n =int(input("enter the value ::"))
# i=n
# count=0
# sum=0
# j=n
# while n>0:
#  n=n//10
#  count+=1
# while i>0:
#   rem=i%10
#   sum+=rem**count
#   i=i//10
# if sum==j:
#   print(sum," :is a armstrong")
# else:
#   print(sum," :is not a armstrong")

# ? (Q.12) Print the following pattern based on the given input
# *
# **
# ***
# ****
# *****
# ******

#todo by for loop
# n = int(input("enter the value ::"))
# print(n, end=" ")
# for i in range(n):
#   print("*"*i)

#todo by while
# i=1
# while i<=n:
#   print("*"*i)
#   i+=1

# ? (Q.13) Print the following pattern based on the given input
#      *
#     **
#    ***
#   ****
#  *****
# ******

# n=int(input("enter the value ::"))
# i=1
# j=n
# while i<=n:
#   print(" "*j, end=" ")
#   print("*"*i)
#   j-=1
#   i+=1

# ? (Q.14) Print the following pattern based on the given input
# *
#   *
#     *
#       *
#         *
#           *

# n=int(input("enter the value ::"))
# j=0
# while n>0:
#   print(" "*j, end=" ")
#   print("*")
#   j+=1
#   n-=1

# ? (Q.15) Print the following pattern based on the given input
#     *
#    ***
#   *****
#  *******
# *********

# n = int (input("enter the value ::"))
# i=0
# while i<n:
#   print(" "*(n-i-1),end="")
#   print("*"*(2*i+1))
#   i+=1

# ? (Q.16) print the prime number 
n=int(input("enter the value ::"))
count=1
for i in range(1,n):
  if n%i==0:
    count+=1
if count==2:
  print("prime")
else:
  print("not a prime")
          
  








  


  
  

    