import math as m
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 5    # Problem Dimension
LB      = -30   # Set Size Lower Bound
UB      = 30    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s=0
    for i in range(D-1):
        s = s + abs(x[i]*m.sin(x[i]) + 0.1 * x[i])
        
    return round(s,2)













