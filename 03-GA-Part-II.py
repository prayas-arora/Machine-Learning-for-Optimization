#-------------------------------------------------------------
#       Part - II: GA--> Crossover, Mutation
#-------------------------------------------------------------
# Python version: 2.6 / 2.7
#-------------------------------------------------------------



#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random
from copy import deepcopy



#-------------------------------------------------------------
# Step 2: Problem parameters
#-------------------------------------------------------------
D       = 10         # Problem Dimension
LB      = -30       # Set Size Lower Bound
UB      = 30        # Set Size Upper Bound



#-------------------------------------------------------------
# Step 4: Functions Definations
#-------------------------------------------------------------
# Function 1: Fitness Function
def FitnessFunction(x):
    s=sum(x)
    return round(s,2)


#-------------------------------------------------------------
# Step 3: Crossover
#-------------------------------------------------------------

# Choose a crossover point 
pt1 = random.randint(1,D/2)
pt2 = random.randint(D/2,D-2)

# Choose Parents
p1=[6, -2, 11, -8, -6,6, -2, 11, -8, -6]
p2=[-7, 11, 7, -2, 8,-7, 1, 7, -2, 9]

p1Fitness=FitnessFunction(p1)
p2Fitness=FitnessFunction(p2)

# Generate new childs 
c1=p1[0:pt1] + p2[pt1: pt2] + p1[pt2:]
c2=p2[0:pt1] + p1[pt1: pt2] + p2[pt2:]

c1Fitness=FitnessFunction(c1)
c2Fitness=FitnessFunction(c2)

print "********* Crossover *********"
print "pt: ", pt1," , ", pt2
print "\np1: ", p1, "\tFitness: ", p1Fitness
print "p2: ", p2, "\tFitness: ", p2Fitness
print "\nc1: ", c1, "\tFitness: ", c1Fitness
print "c2: ", c2, "\tFitness: ", c2Fitness




#-------------------------------------------------------------
# Step 4: Mutation
#-------------------------------------------------------------

pt1 = random.randint(0, D-1)
pt2 = random.randint(0, D-1)

p=[-7, 11, 7, -2, 8,-7, 1, 7, -2, 9]
pFitness=FitnessFunction(p)

c=deepcopy(p)

c[pt1] = round(random.uniform(LB,UB),0)
c[pt2] = round(random.uniform(LB,UB),0)
cFitness=FitnessFunction(c)

print "\n\n********* Mutation *********"
print "pt: ", pt1," , ", pt2
print "\np: ", p, "\tFitness: ", pFitness
print "c: ", c, "\tFitness: ", cFitness
print "\n"



