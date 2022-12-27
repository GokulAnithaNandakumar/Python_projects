from itertools import permutations
word = str(input("Enter a word: "))
list1 = list(sorted(word))
stword = []
ans = ""
for i in list1:
    if i not in stword:
        stword.append(i)

for i in range(1,len(stword)+1):
    for i in list(permutations(stword,i)):
        for k in i:
            ans += k
        print(ans)
        ans = ""