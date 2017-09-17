#-------------------------------------------------------------
# Generate Random Chromosome
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random


#-------------------------------------------------------------
# Step 2: Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
        # f(x) = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
	s = sum (x)
	return s

#-------------------------------------------------------------
# Step 3: Start Program
#-------------------------------------------------------------

# Parameter Setting
Iterations=10

print "Chromosomes:"
for i in range(0,Iterations):
        x=[]
        x.append(random.randint(10, 100))
        x.append(random.randint(-9, 0))
        x.append(random.randint(-50, -10))
        x.append(random.randint(-20, -10))
        x.append(round(random.uniform(0, 1),2))
        x.append(round(random.uniform(0.1, 0.5),2))
        x.append(round(random.uniform(-1, 0),2))
        x.append(round(random.uniform(-5.0, -1.0),2))

        Fitness=FitnessFunction(x)

        print "x = ", x , "Fitness: ", Fitness



