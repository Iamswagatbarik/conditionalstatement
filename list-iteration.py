
#listiterationusingforloop
n=[2,3,'Hello',[5,6,7]]
l=len(n)
for a in range(l):
    print(n[a])
for a in n:
    print(a)
for a in range(l-1,-1,-1):
    print(n[a])