import random

a = range(0, 100)
print len(a), a[:10]
b = random.sample(a, 5)
print b

i=0
j=0
for i in range (0,len(b)):
    for k in range (i,len(b)):
        j=len(b)-k+i-1
        if b[j-1]>b[j]:
            b[j-1],b[j]=b[j],b[j-1]
print b
