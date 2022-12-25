import cmath

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
dis = (b ** 2) - (4 * a * c)

rt1 = (-b - cmath.sqrt(dis)) / (2 * a)
rt2 = (-b + cmath.sqrt(dis)) / (2 * a)

print(int(min(rt1.real, rt2.real)))
print(int(max(rt1.real, rt2.real)))
