import math
from math import e
def trap_composite(a, b, n):
    #n is how many subintervals there are
    #a and b are the beginning and end of the interval, respectively
    h = (b-a)/n #the difference between x values
    #the func is e^-x * cos(x)
    startVal = e**(a*-1)*math.cos(a)
    endVal = e**(b*-1)*math.cos(b)
    midVals = 0
    for i in range(1,n):
        x = h*i
        #print(x/math.pi, "pi\n")
        midVals += e**(-1*x) * math.cos(x)
    ans = (h/2)*(startVal + endVal) + h*midVals
    return ans
    