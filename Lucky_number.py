dob = input("Enter Date of Birth: ")
list = []
num = int(dob)
even = []
odd = []
sumOdd = 0
sumEven = 0
sum = 0
x = 0
if num < 1000000 or num > 99999999:
    print("Invalid Input")
else:
    for num in dob:
        list.append(num)

    for i in list:
        x += 1
        if x % 2 == 0:
            even.append(i)
        elif x % 2 != 0:
            odd.append(i)

    for i in odd:
        sumOdd = sumOdd + int(i)

    for i in even:
        sumEven = sumEven + int(i)
        res1 = sumOdd * 3

    sum = sumEven + res1
    if sum % 10 == 0:
        print(dob + ", " + "Lucky Number")
    elif sum % 10 != 0:
        print(dob + ", " + "Not a Lucky Number")