# OPERATORS
#?  (Q.1) Write a program to take three varibales to store your birth date, birth month, and birth year, respectively, 
# and then print them one by one in a specified order.

# date = int(input("enter the date :"))
# month = input("enter the month :")
# year =int(input("enter the year :"))

# print(date,month,year)

#? (Q.2) Write a program to take input from the user, and print it  to the output.

# a=int(input("enter the value :"))
# print(a) 

#? (Q.3)Write a program to take two values from the user and swap them. 

# a = int(input("enter the value :"))
# b = int(input("enter the value :"))
# tem=a
# a=b
# b=tem
# print(a)
# print(b)

# ? (Q.4) Write a program to take two numbers from the user and perform Six basic operations (addition, subtraction, multiplication, division, integer division and modulus) on those two numbers.

# a= int(input("enter the value :"))
# b =int(input("enter the value :"))
# print ("add",a+b,"sub",a-b, "multi",a*b,"modlus", a%b,"floor", a//b,"divide",a/b )

# ?(Q.5)Write a program to take two numbers A and B from the user and calculate the quotient and remainder when number A is divided by number B.
 
# a= int(input("enter the value :"))
# b =int(input("enter the value :"))
# print("quotient is",a//b,"remainderis", a%b)

#? (Q.6) Write a program to take a positive number from the user and then display the last digit of that number.

# a = int(input("enter the value :"))
# b= a%10
# print(b)

#? (Q.7) Write a program to convert a temperature from Celsius to Fahrenheit using the formula  C/5 = (F-32)/9

# C = int(input("enter tem in celcius :"))
# f = 9*(C/5)+32
# print(f)

# ?(Q.8) Write a program to take two inputs from the user and swap them without using a temporary or third variable.

# a = int(input("enter the value :"))
# b = int(input("enter the value :"))
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# ?(Q.9) Write a program to take two numbers, A and B from the user. Your task is to find the largest number that is less than A and can be divided evenly by B. Can you figure out that number?
# a = int(input("enter the value :"))
# b = int(input("enter the value :"))

# c=a%b
# value=a-c
# print(value)

# ?(Q.10) write a program to take a number from the user and print that number as Odd and Even

# n=int(input("enter the value ::"))
# if n%2==0:
#   print("even")
# else:
#   print("odd")

# ? (Q.11) write a program to takw a number from the user and output whether that number is negative, poasitive or zero.
# n=int(input("enter the value ::"))
# if n>0:
#   print("positive no.")
# elif n<0:
#   print("negative no.")
# else:
#   print("zero")

# ? (Q.12) write a program to take an integer as input and print the smallest integer that is a multiple of both 2 and n
# n=int(input("enter the value ::"))
# if n%2==0:
#   print(n)
# else:
#   print(n*2)

# ? (Q.13) write a program to take three number from the user and print grater number.
# a=int(input("enter the value :;"))
# b=int(input("enter the value :;"))
# c=int(input("enter the value :;"))

# if a>b and a>c:
#   print(a,"max")
# elif b>a and b>c:
#   print(b,"max")
# else:
#   print(c,"max")

# ? (Q.14)Write a program to take four numbers from the user and print the greater number of the four number
# a=int(input("enter the value :;"))
# b=int(input("enter the value :;"))
# c=int(input("enter the value :;"))
# d=int(input("enter the value :;"))

# if a>b and a>c and a>d:
#   print(a,"max")
# elif b>a and b>c and b>d:
#   print(b,"max")
# elif c>a and c>b and c>d:
#   print (c,"max")
# else:
#   print(d,"max")

# ? (Q.15) find year is a leap year or not
# year = int(input("enter the year ::"))
# if year%400==0 or year%4==0 and year%100!=0:
#   print("yes")
# else:
#   print("No")

# ? (Q.16) 
# a = int(input("enter the value ::"))
# b = int(input("enter the value ::"))
# c = int(input("enter the value ::"))
# max =0
# smax=0
# if a>b:
#    max=a
#    smax=b
# else:
#    max=b
#    smax=a
# if a>c:
#    max=a
#    smax=c
# else:
#    max=c
#    smax=a
# if b>c:
#    max=b
#    smax=c
# else:
#    max=c
#    smax=b
# print(smax)

# ? (Q.17) HRA and DA
# salary=int(input("enter the salary ::"))
# if salary<=10000:
#   HRA=salary*20/100
#   DA=salary*80/100
#   tsalary=HRA+DA
#   print(tsalary+salary)
# elif salary<=20000:
 
#    HRA=salary*25/100
#    DA=salary*90/100
#    tsalary=HRA+DA
#    print(tsalary+salary)
# else:
#    HRA=salary*30/100
#    DA=salary*95/100
#    tsalary=HRA+DA
#    print(tsalary+salary)
  
# ?(Q)
# * prime number
# n=int(input("enter the value ::"))
# count=1
# for i in range (1,n):
#   if n%i==0:
#     count+=1
# if count==2:
#   print("it is prime number")
# else:
#   print("it is not a prime number")

# todo by while loop
# n= int(input("enter the value ::"))
# count=0
# i=1
# while i<=n:
#   if n%i==0:
#     count+=1
#   i+=1
# if count==2:
#   print("prime number")
# else:
#   print("not a prime number")

# ? (Q)
# * series question
# n= int(input("enter the value ::"))
# for i in range(1,n+1):
#  print(i*2+1,end=" ")

 # ?(Q.18) Write a program to take 4 numbers from the user and output the third max of these 4 numbers.
# n=int(input("enter 1st value ::"))

#! perfect number::
#* A perfect number is a positive integer that is equal to the sum of its proper divisor
# n=int(input("enter the value::"))
# sum=0
# for i in range(1,n):
#  if n%i==0:
#   sum+=i
# if sum==n:
#  print("perfect number")
# else:
#  print("not a perfect number")

# todo by while loop
# n=int(input("enter the value::"))
# sum=0
# i=1
# while i<n:
#   if n%i==0:
#     sum+=i
#   i+=1
# if sum==n:
#   print("perfect number")
# else:
#   print("not perfect number")

# n=int(input("enter the value::"))
# sum=0
# i=n/2
# while i>0:
#   if n%i==0:
#     sum+=i
#   i-=1
# if sum==n:
#   print("perfect number")
# else:
#   print("not perfect number")

# ? (Q) print a series 3,5,7,9 and so on 

# todo while loop series
# n=int(input("enter the value::"))
# i=1
# while i<=n:
#   print(i*2+1,end=" ")
#   i+=1

# todo for loop series
# n=int(input("enter the value ::"))
# for i in range (1,n+1):
#   print(i*2+1, end=" ")


#! ###############------perfect number-------#################
# ? by for loop
# n=int(input("enter the value ::"))
# sum=0
# for i in range (1,n):
#   if n%i==0:
#     sum+=i
# if sum==n:
#   print("perfect")
# else:
#   print("not perfect")

# ? by while loop
# n = int (input("num"))
# i=n-1
# sum=0
# while i>0:
#   if n%i==0:
#     sum+=i
#   i-=1
# if sum==n:
#   print("per")
# else:
#   print(" n per")

#! #####################----------series--------#####################
# ? by for loop
# n=int(input("number ::"))
# for i in range(1,n+1):
#   print(i*2, end=" ")

# n=int(input("num ::"))
# i=1
# while i<=n:
#   print(i*2+1, end=" ")
#   i+=1

# ! ##########----sum of  the digit------#############
# n = int(input("enter the value ::"))
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem
#   n=n//10
# print(sum)

# ! ##########------count of the digit--------##########
# n=int(input("enter the value ::"))
# count=0
# while n>0:
#   rem=n%10
#   count+=1
#   n=n//10
# print(count)

# ? by function
# n=input("enter the value ::")
# count=0
# i=0
# while i<len(n):
#   count+=1
#   i+=1
# print(count)

# ? by for loop
# n= int(input("enter the value ::"))
# count=0
# for _ in str(n):
#   count+=1

# print(count)

# n=int(input("enter :"))
# sum=0
# i=n-1
# while i>0:
#   if n%i==0:
#     sum+=i
#   i-=1
# if sum==n:
#   print("yes")
# else:
#   print("no")
  
# ! spy number
# n =int(input("enter the value ::"))
# sum=0
# num=n
# product=1
# while n>0:
#   rem=n%10
#   sum+=rem
#   product*=rem
#   n=n//10
# if sum==product:
#   print("yes")
# else:
#   print("no")

#! binary to decimal
# n=int(input("enter ::"))
# i=0
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem*(2**i)
#   n=n//10
#   i+=1
# print(sum)

# ! prime number
# n=int(input("enter ::"))
# i=1
# count=0
# while i<=n:
#   if n%i==0:
#     count+=1
#   i+=1
# if count==2:
#   print("prime number")
# else:
#   print("no")

# ! perfect number
# n=int(input("enter ::"))
# i=1
# sum=0
# while i<n:
#   if n%i==0:
#     sum+=i
#   i+=1
# if sum==n:
#   print("perfect number")
# else:
#   print("not a perfect number")

# ! decimal to binary
# i=int(input("enter the value ::"))
# sum=""
# while i>0:
#  b=i%2
#  sum=str(b)+sum
#  i=i//2
# print(sum)

# ! palindrome number
# n=int(input("enter the value ::"))
# j=n
# rev=0
# while n>0:
#   rem=n%10
#   rev=rev*10+rem
#   n=n//10
# if rev==j:
#   print("yes")
# else:
#   print("no")
  
# ! binary to decimal
# n=int(input("enter ::"))
# i=0
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem*(2**i)
#   n=n//10
#   i+=1
# print(sum)

# ! decimal to binary
# n=int(input("enter ::"))
# sum=""
# while n>0:
#   b=n%2
#   sum= str(b)+sum
#   n=n//2
# print(sum)

# ! spy number
# n=int(input("enter ::"))
# sum=0
# product=1
# while n>0:
#   rem=n%10
#   sum+=rem
#   product*=rem
#   n=n//10
# if sum==product:
#   print("spy")
# else:
#   print("not a spy")

# ! factorial
# n=int(input("enter ::"))
# i=1
# product=1
# while i<=n:
#   product*=i
#   i+=1
# print(product)


# ! decimal to binary
# n=int(input("enter ::"))
# sum=""
# while n>0:
#   rem=n%2
#   sum= str(rem)+sum
#   n=n//2
# print(sum)

# ! binary to decimal
# n=int(input("enter ::"))
# i=0
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem*(2**i)
#   n=n//10
#   i+=1
# print(sum)

# ! palindrome
# n=int(input("enter ::"))
# j=n
# rev=0
# while n>0:
#   rem=n%10
#   rev=rev*10+rem
#   n=n//10
# if rev==j:
#   print("palindrome")
# else:
#   print("not a palindrome")

# ! series
# n=int(input("enter thr value ::"))
# i=1
# while i<=n:
#   print(i*5, end=" ")
#   i+=1

# ! decimal to binary
# n=int(input("enter ::"))
# sum=""
# while n>0:
#   rem= n%2
#   sum= str(rem)+sum
#   n=n//2
# print(sum)

# ! binary to decimal
# n=int(input("enter ::"))
# i=0
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem*(2**i)
#   n=n//10
#   i+=1
# print(sum)

# ! sum of digit
# n=int(input("enter ::"))
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem
#   n=n//10
# print(sum)

# ! count the digit
# n=int(input("enter the value ::"))
# count=0
# while n>0:
#   rem=n%10
#   count+=1
#   n=n//10
# print(count)

# ! spy number
# n=int(input("enter ::"))
# sum=0
# multi=1
# while n>0:
#   rem=n%10
#   sum+=rem
#   multi*=rem
#   n=n//10
# if sum==multi:
#   print("spy")
# else:
#   print("not a spy")

# ! prime number
# n=int(input("enter ::"))
# count=0
# i=1
# while i<=n:
#   if n%i==0:
#     count+=1
#   i+=1
# if count==2:
#   print(n, "is prime")
# else:
#   print(n,"not a prime")

# ! octa to binary
# sum=0
# n =int(input("enter ::"))
# octa = ""
# while n>0:
#   rem=n%10
#   sum=""
#   while rem>0:
#     dec=rem%2
#     sum=str(dec)+sum
#     rem=rem//2
#   i = int(sum)
#   # print(i)
#   count = 0
#   while i>0:
#     i = i//10
#     count += 1
#   while count <3:
#     sum = "0" + sum
#     count += 1
#   octa = sum + octa
#   n = n//10
# print(octa)

# ! armstrong number
# n=int(input("enter the value ::"))
# j=n
# i=n
# sum=0
# count=0
# while n>0:
#   rem=n%10
#   count+=1
#   n=n//10
# while i>0:
#   rem=i%10
#   sum+=rem**count
#   i=i//10
# if sum==j:
#   print("arm")
# else:
#   print("not a arm")

# ! perfect number
# n=int(input("enter ::"))
# i=1
# sum=0
# while i<n:
#   if n%i==0:
#     sum+=i
#   i+=1
# if sum==n:
#   print("perfect number")
# else:
#   print("not a perfect number")



  
  
    
























  





    