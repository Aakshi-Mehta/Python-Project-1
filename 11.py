#11. Write a python program that generates the first n numbers in the Fibonacci sequence.


n=int(input("enter the no:"))
a=0
b=1
c=a+b
print(a)
print(b)
print(c)
for i in range(0,n-3):
    a=b
    b=c
    c=a+b
    print(c)