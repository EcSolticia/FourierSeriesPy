
#customizables
codomain = [0, 1, 2]
delta = 0.1
start = 0

#slope-point approximation
#----

domain = []
slopes = []

def initialize():
    global domain
    global slopes
    
    for i in range(len(codomain)):
        #fix domain
        domain.append(start + delta * i)
        
        if i < len(codomain) - 1:
            #compute slopes
            this_slope = (codomain[i + 1] - codomain[i])/delta
            slopes.append(this_slope)
        
from math import floor
    
def func(x):
    if len(codomain) != 0 and len(domain) == 0:
        initialize()
        
    if max(domain) < x or x < start:
        print("Input out of domain")
        return
    
    index = int(floor((x - start)/delta))
    
    if index < len(codomain) - 1:
        out = slopes[index] * (x - domain[index]) + codomain[index]
    else: #index is max iff the input is max   
        out = codomain[len(codomain) - 1]
    return out
   
