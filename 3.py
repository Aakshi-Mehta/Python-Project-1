#3. Write a python program that calculates the factorial of a given number.

num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial is",fact)