x = int(input())
a = []
b = []
for i in range(1, x+1):
    a.append(i**2)
    b.append(i**3)
c = list(set(a + b))
if x!= 1:
    print(c[x])
if x==1:
    print(1)
