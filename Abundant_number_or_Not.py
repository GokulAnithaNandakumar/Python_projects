# An abundant number or excessive number is a number for which the sum of its all factors is greater than the number itself.
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum>n:
    print("Abundant number")
else:
    print("Not Abundant number")