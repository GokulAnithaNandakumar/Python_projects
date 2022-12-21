num=int(input("Enter a two digit number you want to convert to Roman numeral: "))

sol=[]

x="x"
if int(num/10)==0:
 pass

elif int(num/10)==1:
 sol.append('x')

elif int(num/10)==2:
 sol.append('xx')

elif int(num/10)==3:
 sol.append('xxx')

elif int(num/10)==4:
 sol.append('xv')

elif int(num/10)==5:
 sol.append('v')

elif int(num/10)==6:
 sol.append('vx')


elif int(num/10)==7:
 sol.append('vxx')

elif int(num/10)==8:
 sol.append('vxxx')

elif int(num/10)==9:
 sol.append('xc')



if num%10==0:
 pass

elif num%10==1:
 sol.append('i')

elif num%10==2:
 sol.append('ii')

elif num%10==3:
 sol.append('iii')

elif num%10==4:
 sol.append('iv')

elif num%10==5:
 sol.append('v')

elif num%10==6:
 sol.append('vi')

elif num%10==7:
 sol.append('vii')

elif num%10==8:
 sol.append('viii')

elif num%10==9:
 sol.append('ix')

roman=''.join(sol)

print(roman)