#construct array of length 20 with random numbers between 6 and 7

import random
a=[]
for i in range(20):
    a=a+[random.uniform(6,7)]

s=0
for i in range(20):
    s=s+a[i]
    
#print s/20



a=[]
b=[]
for i in range(len(a)):
    b=b+[
