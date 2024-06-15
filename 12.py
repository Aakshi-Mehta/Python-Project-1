#12. Write a python program that calculates the sum of the digits of a given number.

n=int(input("enter the no:"))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print(sum)