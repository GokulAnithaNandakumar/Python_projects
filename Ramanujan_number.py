def ram(a):
  c=0
  for i in range(1,a+1):
    for j in range(1,a+1):
      if (j*j*j)+(i*i*i)==a:
        c=c+1
      if c==2:
        return True
        break
  else:
    return False

a=int(input())
ram(a)

if ram(a)==True:
  print("Yes")
else:
  print("No")