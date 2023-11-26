import math
from math import e
def simpson_composite(a,b,n):
    oddX = 0
    evenX = 0
    h = (b-a)/n #the difference between x values
    #the func is e^-x * cos(x)
    startVal = e**(a*-1)*math.cos(a)
    endVal = e**(b*-1)*math.cos(b)
    for i in range(1,n):
        x = h*i
        #print(x/math.pi, "pi\n")
        if i % 2 == 1:
            oddX += e**(-1*x) * math.cos(x)
        elif i % 2 == 0:
            evenX += e**(-1*x) * math.cos(x)
    ans = (h/3)*(startVal + endVal + 4*oddX + 2* evenX)
    return ans