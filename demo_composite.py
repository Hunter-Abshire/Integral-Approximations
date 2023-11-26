from trap_composite import trap_composite
from simpson_composite import simpson_composite
import math
from math import e
trueVal = (1-e**(-2*math.pi))/2
ans1 = trap_composite(0,2*math.pi,2)
ans2 = simpson_composite(0,2*math.pi,2)
trapError = abs(ans1-trueVal)/trueVal*100
simpError = abs(ans2-trueVal)/trueVal*100
print("n = 2:\ntrap composite: ",ans1,"\nsimpson composite: ",ans2,"\nrelative errors: ","\ntrap:",trapError,"%\nsimpson: ",simpError,"%\n")
ans1 = trap_composite(0,2*math.pi,4)
ans2 = simpson_composite(0,2*math.pi,4)
trapError = abs(ans1-trueVal)/trueVal*100
simpError = abs(ans2-trueVal)/trueVal*100
print("n = 4:\ntrap composite: ",ans1,"\nsimpson composite: ",ans2,"\nrelative errors: ","\ntrap:",trapError,"%\nsimpson: ",simpError,"%\n")
ans1 = trap_composite(0,2*math.pi,6)
ans2 = simpson_composite(0,2*math.pi,6)
trapError = abs(ans1-trueVal)/trueVal*100
simpError = abs(ans2-trueVal)/trueVal*100
print("n = 6:\ntrap composite: ",ans1,"\nsimpson composite: ",ans2,"\nrelative errors: ","\ntrap:",trapError,"%\nsimpson: ",simpError,"%\n")
ans1 = trap_composite(0,2*math.pi,8)
ans2 = simpson_composite(0,2*math.pi,8)
trapError = abs(ans1-trueVal)/trueVal*100
simpError = abs(ans2-trueVal)/trueVal*100
print("n = 8:\ntrap composite: ",ans1,"\nsimpson composite: ",ans2,"\nrelative errors: ","\ntrap:",trapError,"%\nsimpson: ",simpError,"%\n")