
#!------------------------------------------------------ CONDITION---------------------------------------------!#

#todo  Question.1
#? Write a program that takes a positive integer n as input and prints whether it is odd or even
#? Code:

# n=int(input())
# if n%2==0:
#   print("Even")
# else:
#   print("Odd")

#todo  Question.2
#? Write a program that takes a student's score (out of 100) and outputs their grade based on the following conditions:
#? Code:

# marks=int(input("Enter your marks: "))
# if marks>=90:
#     print("A")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# elif marks>=60:
#     print("D")
# else:
#     print("F")

# #todo  Question.3
# #? Write a program that categorizes a person's age into different life stages based on the following conditions:
# #? Code:

# age=int(input("Enter the age: "))
# if age <=2:
#   print("Infant")
# elif age<=12:
#   print(" Child")
# elif age<=19:
#   print("Teenager")
# elif age<=65:
#   print("Adult")
# else :
#   print("Senior")


# #todo  Question.4
# #? Write a program that suggests an activity based on the current temperature (in Celsius), following these guidelines:
# #? Code:

# temp=int(input("Enter the temperature: "))
# if temp>30:
#   print("It's hot. Let's go swimming!")
# elif temp>20:
#   print("Perfect for a picnic.")
# elif temp>10:
#   print("Maybe wear a jacket?")
# else:
#   print("Too cold! Best to stay indoors.")


# #todo  Question.5
# #? Write a program that takes three numbers as input and prints the largest number.
# #? Code:

# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>n2 and n1>n3:
#   print(n1)
# elif n2>n1 and n2>n3:
#   print(n2)
# else:
#   print(n3)


# #todo  Question.6
# #? Write a program that takes three numbers as input and prints the numbers in ascending order. This program doesn't use an array.
# #? Code:

# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1<n2 and n1<n3:
#   if n2<n3:
#     print(n1,end=" ")
#     print(n2,end=" ")
#     print(n3,end=" ")
#   else:
#     print(n1,end=" ")
#     print(n3,end=" ")
#     print(n2,end=" ")
# if n2<n1 and n2<n3:
#   if n1<n3:
#     print(n2,end=" ")
#     print(n1,end=" ")
#     print(n3,end=" ")
#   else:
#     print(n2,end=" ")
#     print(n3,end=" ")
#     print(n1)
# if n3<n1 and n3<n2:
#   if n1<n2:
#     print(n3,end=" ")
#     print(n1,end=" ")
#     print(n2,end=" ")
#   else:
#     print(n3,end=" ")
#     print(n2,end=" ")
#     print(n1,end=" ")



# #!----------------------------------------------------- LOOPS----------------------------------------------!#

# #todo  Question.7
# #? You are given an integer n. Print "Hello World" n times.
# #? code:

# n=int(input())
# i=1
# while  i<=n:
#   print("Hello World")
#   i+=1


# #todo  Question.8
# #? You are given an integer n. Print * n times in the same line with space in between.
# #? Code:


# n=int(input())
# i=1
# while i<=n:
#   print("*", end="")
#   i+=1


# #todo  Question.9
# #? You are given an integer n. Print the first n natural numbers.
# #? Code:


# n=int(input())
# i=1
# while i<=n:
#   print(i, end=" ")
#   i+=1

# #todo  Question.10
# #? You are given an integer n. Print all the even numbers less than equal to n
# #? code:

# n=int(input())
# i=1
# while i<=n:
#   if i%2==0:
#     print(i,end=" ")
#   i+=1


# #todo  Question.11
# #? You are given an integer n. Print all the square numbers less than equal to n.
# #? code:
  

# n = int(input("Enter the number of squares to print: "))
# i = 1
# while i <= n:
#     print(i**2, end=" ")
#     i += 1


# #todo  Question.12
# #? You are given an integer n. Print the first n even numbers.
# #? Code:

# n=int(input())
# i=1
# while i<=n*2:
#   if i%2==0:
#     print(i,end=" ")
#   i+=1

# #todo  Question.13
# #? You are given an integer n. Print the first n odd numbers.
# #? code:

# n = int(input())
# i = 1
# while i <= n*2:
#   if i % 2 !=0:
#     print(i,end=" ")
#   i += 1


# #todo  Question.14
# #? You are given an integer n. Print the first n square numbers.
# #? Code:

# n=int(input())
# i=1
# while i<=n:
#   print(i**2,end=" ")
#   i+=1

# #todo  Question.15
# #? You are given an integer n. Print the multiplication table of n till count 10.
# #? code:

# n=int(input())
# i=1
# while i<=10:
#   print(n*i,end=" ")
#   i+=1


# #todo  Question.16
# #? Write a program that takes a number n as input and prints all the factors of the number.
# #? code:

# n=int(input())
# i=1
# while i<=n:
#   if n%i==0:
#     print(i,end=" ")
#   i+=1


# #todo  Question.17
# #? You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…
# #? Code:

# n=int(input())
# count=3
# i=1
# while i<=n:
#     print(count,end=" ")
#     count+=2
#     i+=1


# #todo  Question.18
# #? You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…
# #? Code:


# n=int(input())
# count=2
# i=1
# while i<=n:
#   print(count,end=" ")
#   count+=3
#   i+=1


# #todo  Question.19
# #? You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
# #? Code:

# n=int(input())
# count=3
# i=1
# while i<=n:
#   print(count,end=" ")
#   count*=2
#   i+=1


# #todo  Question.20
# #? You are given an integer n. Print the sum of the first n Natural Numbers.
# #? Code:



# n=int(input())
# sum=0
# i=1
# while i<=n:
#   sum+=i
#   i+=1
# print(sum)


# #?todo  Question.21
# #? You are given an integer n. Print the sum of the first n terms of the series 3, 5, 7, 9, 11….
# #? Code:


# n=int(input())
# sum=0
# count=3
# i=1
# while i<=n:
#   sum+=count
#   count+=2
#   i+=1
# print(sum)


# #todo  Question.22
# #? Write a program to calculate the factorial of a given number n.
# #? Code:

# n=int(input())
# fac=1
# i=1
# while i<=n:
#   fac*=i
#   i+=1
# print(fac)




# #?todo  Question.23 
# #?? Write a program that takes a number n as input and prints the number of digits the number has.
# #?? Code:

# n=int(input())
# count=0
# while n>0:
#   rem=n%10
#   count+=1
#   n=n//10
# print(count)

# #?todo  Question.24
# #?? Write a program that calculates the sum of all the digits in a given number n.
# #?? Code:

# n=int(input())
# sum=0
# while n>0:
#   rem=n%10
#   sum+=rem
#   n=n//10
# print(sum)

#!------------------------------------------------- Advance Loops-------------------------------------------!#
# #todo  Question.25
# #? Write a program that takes a number n as input and prints the first n terms of the Fibonacci Series.
# #? Code:

# n=int(input())
# x=0
# y=1
# z=0
# while n>0:
#   print(z,end=" ")
#   x=y
#   y=z
#   z=x+y
#   n-=1

# #todo  Question.26
# #? Write a program that takes a number n as input and prints the reverse of the given number.
# #? Code:



# n=int(input())
# while n>0:
#   rev=n%10
#   print(rev,end="")
#   n=n//10

# #todo  Question.27
# #todo  Question.28


# #todo  Question.29
# #? Write a program that takes a Binary Number B as input and prints the Decimal equivalent of the given input.
# #? Code:

# n=int(input())
# sum=0
# i=0
# while n>0:
#   rem=n%10
#   sum+=rem*(2**i)
#   n=n//10
#   i+=1
# print(sum)

# #todo  Question.30
# #? Write a program that takes a Decimal Number D as input and prints the Binary equivalent of the given input.
# #? Code:

# n=int(input())
# sum=""
# while n>0:
#   rem=n%2
#   sum=str(rem)+sum
#   n=n//2
# print(sum)

# #todo  Question.31
# #? You are given an integer n. Print yes, if it is a prime number. Print no, if it is not a prime number.
# #? Code:

# n=int(input())
# count=0
# i=1
# while i<=n:
#   if n%i==0:
#     count+=1
#   i+=1
# if count==2:
#   print("Yes")
# else:
#   print("No")

#todo  Question.32
#? Is Perfect Number?:
#? You are given an integer n. Print yes, if it is a Perfect Number. Print no, if it is not a Perfect Number.
#? A Perfect Number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
#? Code:

# n = int (input())
# sum=0
# i=1
# while i<n:
#   if n%i==0:
#     sum+=i
#     i+=1
#   else:
#     i+=1
# if sum==n:
#   print("Yes")
# else:
#   print("No")


#todo  Question.33
#? Is Armstrong Number?:
#? You are given an integer n. Print yes, if it is an Armstrong Number. Print no, if it is not an Armstrong Number.
#? An Armstrong Number is a positive number that equals the sum of its digits, each raised to the power of the number of digits.

# n = int (input())
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

# todo  (Q.34) Print the following pattern based on the given input
#! *
#! **
#! ***
#! ****
#! *****
#! ******

# n=int(input())
# i=1
# while i<=n:
#   print("*"*i)
#   i+=1

# todo  (Q.35) Print the following pattern based on the given input
#!      *
#!     **
#!    ***
#!   ****
#!  *****
#! ******

# n=int(input("enter the value ::"))
# i=1
# j=n
# while i<=n:
#   print(" "*j, end=" ")
#   print("*"*i)
#   j-=1
#   i+=1

# todo  (Q.36) Print the following pattern based on the given input
#! *
#!   *
#!     *
#!       *
#!         *
#!           *

# n=int(input("enter the value ::"))
# j=0
# while n>0:
#   print(" "*j, end=" ")
#   print("*")
#   j+=1
#   n-=1

# todo  (Q.37) Print the following pattern based on the given input
#!     *
#!    ***
#!   *****
#!  *******
#! *********

# n = int (input("enter the value ::"))
# i=0
# while i<n:
#   print(" "*(n-i-1),end="")
#   print("*"*(2*i+1))
#   i+=1


#todo  (Q.38) You are given an integer n. Print the first n prime numbers.
# n = int(input("enter the value:: "))
# c=0
# number = 2

# while c != n:
#     count=0
#     i=1
#     while i<=number:
#         if number%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print(number)
#         c += 1
#     number += 1
    

#!-------------------------------------------- Array Traversal-----------------------------------------------!#
#todo  (Q.39) Square - Each Array Element:
#? You are given an integer array. Traverse through the array and print the square for each element.

# list =[]
# n=int(input("Enter:: "))
# i=0
# while i<n:
#     ele = int(input("enter ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# while i<len(list):
#     arr = list[i]**2
#     print(arr,end=" ")
#     i+=1


#todo  (Q.40) Odd or Even - Each Array Element:
#? You are given an integer array. Traverse through the array and for each element, if the element is odd print "Odd", else print "Even".

# list=[]
# n= int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele=int(input("Enter ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         print("Even")
#     else:
#         print("Odd")
#     i+=1

#todo  (Q.41) Odd Count in an Array:
#? You are given an integer array. Print the number of odd numbers in the array.

# list=[]
# n= int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele=int(input("Enter ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# count=0
# while i<len(list):
#     if list[i]%2!=0:
#      count+=1
#     i+=1
# print(count)


#todo  (Q.42) Number Count in an Array:
#? You are given an integer array. You are also given a number. Print the number of times the number appears in the array.

# list=[]
# n=int(input("Enter length:: "))
# i=0
# while i<n:
#     ele=int(input("Enter Ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# count=0
# target = int(input("Enter target:: "))
# while i<len(list):
#     if list[i]==target:
#         count+=1
#     i+=1
# print(count)


#todo  (Q.43) Sum of Elements in an Array:
#? You are given an integer array. Add all the numbers present in the array and print the sum.

# list=[]
# n=int(input("Enter length:: "))
# i=0
# while i<n:
#     ele=int(input("Enter Ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# sum=0
# while i<len(list):
#     sum+= list[i]
#     i+=1
# print(sum)


#todo   (Q.44) Average of Elements in an Array:
#? You are given an integer array. Find the average of all the numbers present in the array.

# list=[]
# n=int(input("Enter length:: "))
# i=0 
# while i<n:
#     ele = int(input("Enter ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# sum=0
# while i<len(list):
#     sum+=list[i]
#     i+=1
# print(sum/i)


#todo   (Q.45) Product of Elements in an Array:
#? You are given an integer array. Multiply all the numbers present in the array and print the final product.

# list=[]
# n=int(input("Enter length:: "))
# i=0 
# while i<n:
#     ele = int(input("Enter ele:: "))
#     i+=1
#     list.append(ele)
# i=0
# product=1
# while i<len(list):
#     product*=list[i]
#     i+=1
# print(product)


#todo   (Q.46) Minimum in an Array:
#? You are given an integer array. Find the minimum element of the array.

# list = []
# n= int(input("Enter Length:: "))
# i=0 
# while i<n:
#     ele = int(input("Enter ele:: "))
#     i+=1
#     list.append(ele)

# i=0
# min = list[i]
# while i<len(list):
#     if list[i]<min:
#         min=list[i]
#     i+=1
# print(min)            

#todo   (Q.47) Minimum Index in an Array:
#? You are given an integer array. Find the index of the minimum element of the array. If there are multiple occurrences of the minimum number, print the index of the first occurrence of the minimum number. 

# list = []
# n= int(input("Enter Length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter ele:: "))
#     i+=1
#     list.append(ele)

# i=0
# index = 0
# min = list[i]
# while i<len(list):
#     if list[i]<min:
#         min=list[i]
#         index = i
#     i+=1
# print(index+1)


#todo   (Q.48) Maximum Sum of Two Consecutive Elements
#? You are given an integer array. Print the maximum sum of two consecutive integers in the given array.

# list= []
# n= int(input("Enter Length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the element:: "))
#     i+=1
#     list.append(ele)
# i=0
# max = 0
# while i<len(list)-1:
#     sum = list[i]+list[i+1]
#     if max<sum:
#         max = sum
#     i+=1
# print(max)

#todo  (Q.49) Count Elements until Negative:
#? You are given an integer array. Count all the numbers present in the array till you encounter a negative number and print the count. If no negative number is present, count till the end.

# list = []
# n = int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the element:: "))
#     i+=1
#     list.append(ele)
# i=0
# count =0 
# while i<len(list):
#     if list[i]>0:
#         count+=1
#     else:
#         break
#     i+=1
# print(count)

#todo  (Q.50)  Sum until Zero:
#? You are given an integer array. Add all the numbers present in the array till you encounter a 0 and print the sum. If no 0 is present, add till the end.

# list = []
# n = int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the value:: "))
#     i+=1
#     list.append(ele)
# i=0
# sum=0
# while i<len(list):
#     if list[i]>0:
#         sum+=list[i]
#     else:
#         break
#     i+=1
# print(sum)


#todo   (Q.51)  Linear Search:
#? You are given an integer array. Take another number as input and search if the number is present in the given array. If the number is present, print "Yes", else print "No".

# list = []
# n = int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the value:: "))
#     i+=1
#     list.append(ele)
# i=0
# count=0
# t = int(input("Enter the target:: "))
# while i<len(list):
#     if list[i]==t:
#         count+=1
#     else:
#         count+=0
#     i+=1
# if count==1:
#     print("YES")
# else:
#     print("NO")


#todo (Q.52) Check Array for Negative Numbers:
#? You are given an array of integers. Check if the array has any negative numbers. If the array has any negative number, print yes. Else, print no.

# list = []
# n=int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the element:: "))
#     i+=1
#     list.append(ele)
# i=0
# while i<len(list):
#     if list[i]<0:
#         print("YES")
#         break
#     i+=1
# else:
#     print("NO")


#todo (Q.53) Check Array for Ascending Order:
#? You are given an array of integers. Check if the array is in Ascending Order. If yes, print "Yes", else print "No.

# list = []
# n= int(input("Enter the length:: "))
# i=0
# while i < n :
#     ele = int(input("Enter the Element:: "))
#     i+=1
#     list.append(ele)
# i=0
# while i < len(list)-1:
#     if list[i]>list[i+1]:
#         print("NO")
#         break
#     i+=1
# else:
#     print("YES")


#todo (Q.54) First Perfect Square:
#? You are given an array of integers. Print the first element of the array that is a perfect square. If there are no perfect squares, print No.

# list = []
# n= int(input("Enter the length :"))
# i=0
# while i<n:
#     ele = int(input("Enter the element : "))
#     i+=1
#     list.append(ele)
# i=0
# while i<len(list):
#     j = 0
#     while j * j < list[i]:
#         j+=1
#     if j * j == list[i]:
#         print(list[i])
#         break
#     i+=1
# else:
#     print("NO")



#todo (Q.55) First Element Greater Than K:
#? You are given an array of integers and another integer K. Print the first element of the array that is greater than K. If there are no elements greater than K, print No.

# list = []
# n= int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the value:: "))
#     i+=1
#     list.append(ele)
# k=int(input("Enter your K element:: "))
# i=0
# while i<len(list):
#     if list[i]>k:
#         print(list[i])
#         break
#     i+=1
# else:
#     print("NO")


#todo (Q.56) Longest Subarray with Increasing Numbers:
#? You are given an integer array. Print the length of the longest subarray with increasing numbers. A subarray is defined as a contiguous portion of an array.Try not to use nested loop.

# list = []
# n= int(input("Enter the length:: "))
# i=0
# while i<n:
#     ele = int(input("Enter the value:: "))
#     i+=1
#     list.append(ele)

# list = list(map(int,input().split()))
# i =1
# while i<len(list):
#     j=i
#     arr = []
#     while j <len(list):
#         if list[j-1] <= list[j]:
#             arr.append(list[j-1])
#             j+=1
#         else:
#             if len(arr) > 1:
#                 arr.append(list[j-1])
#                 print(arr)
#             break
#     print(j)
#     if j == len(arr):
#         arr.append(list[j-1])
#         print(arr)
#         break
#     else:
#         i=j+1


#todo (Q.57) Reverse an Array:
#? You are given an array of integers. Create a new array with elements in reverse order. Print the new array.

# list = list(map(int,input().split()))

# arr = []
# i= len(list) - 1

# while i >= 0:
#     arr.append(list[i])
#     i-=1
# print(arr)


#todo (Q.58) Check Array for Palimdrome:
#? You are given an array of integers. Check if the given array is a Palindrome. If it is a Palindrome array, print yes, else print no.

# list = list(map(int,input().split()))

# arr = []
# i= len(list) - 1

# while i >= 0:
#     arr.append(list[i])
#     i-=1
# if arr == list:
#     print("YES")
# else:
#     print("NO")


#todo Maximum Frequency in an Array:
#? You are given an array of integers. Find the element that appears the maximum number of times in an array. If multiple elements appear maximum number of times, you can print any.

# list = list(map(int,input().split()))
# i=0
# count=0
# while i < len(list):
#     j=1
#     while j < len(list):
#         if list[i] == list[j]:
#             count=list[j]
#             j+=1
#         else:
#             j+=1
#     i+=1 
# if count !=0:
#     print(count)
        

# Write a program to count the total number of 1s in the binary representation of a given positive integer n.
# If n = 19 (binary: 10011), the total number of 1s is 3.
# If n = 15 (binary: 1111), the total number of 1s is 4.
# If n = 8 (binary: 1000), the total number of 1s is 1.


n = int(input())
binary = 0
i = 1
count = 0

while n > 0:
    rem = n%2
    if rem == 1:
        count+=1
    binary += rem * i
    n //= 2
    i *=10
print(binary, count)














        




















        





    


















    
    
    



