# amount=p(1+r/100)^t
# ci=amount-p
p=float(input())
r=float(input())
t=float(input())
amt=p*((1+(r/100))**t)
c=amt-p
print(round(c,3))