x = int(input())
a = []
b = []
for i in range(x):
    a.append(i^2)
    b.append(i^3)
c = list(set(a + b)).sort()
print(c[x])