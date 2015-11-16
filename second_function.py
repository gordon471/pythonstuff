#import first_function
#import first_function

#from first_function import *

#tellMe(10) doesnt work
#first_function.tellMe(11)
#srt.tellMe(10)
#tellMe(11)


def zeros(n):
    a=[]
    for i in range(n):
        a=a+[0]
    return a

def uni_array(stuff,n):
    a=[]
    for i in range(n):
        a=a+[stuff]
    return a
def rand_array(low,high,num):
    a=[]
    for i in range(num):
        a=a+[random.uniform(low,high)]
    return a
print uni_array(95,5)
print uni_array("hi",4)
print rand_array()
        
