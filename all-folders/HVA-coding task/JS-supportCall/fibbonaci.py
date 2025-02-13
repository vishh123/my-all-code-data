# 1st fibonacci number is 0 find the 2578th number.

n=int(input("enter the length"))
z=0
x=0
y=1
while n>2:
  z=x+y
  x=y
  y=z
  n-=1
else:
  print(z)

