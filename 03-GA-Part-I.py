#-------------------------------------------------------------
#       Part - I: GA--> Generate Random Chromosomes
#-------------------------------------------------------------
# Python version: 2.6 / 2.7
#-------------------------------------------------------------



#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random

#-------------------------------------------------------------
# Step 2: GA parameters
#-------------------------------------------------------------
PopSize     = 10    # Size of the Population(i.e Number of Chromosomes)
Pop         = []    # Store Population with fitness

#-------------------------------------------------------------
# Step 3: Problem parameters
#-------------------------------------------------------------
D       = 5         # Problem Dimension
LB      = -30       # Set Size Lower Bound
UB      = 30        # Set Size Upper Bound

class Individual:
    def __init__(self, C, F):
        self.Chromosome=C
        self.Fitness=F



#-------------------------------------------------------------
# Step 4: Functions Definations
#-------------------------------------------------------------


# Function 1: Generate the initial Pop
def Init():
    for i in range (0, PopSize):
      Chromosome = [round(random.uniform(LB,UB),2) for j in range(0,D)]
      Fitness = FitnessFunction(Chromosome)
      NewIndividual = Individual(Chromosome,Fitness)
      Pop.append(NewIndividual)
        

# Function 2: Fitness Function
def FitnessFunction(x):
    s=(x[4] - x[3]**2)**2 + (x[3] - x[2]**2)**2 + \
       (x[2] - x[1]**2)**2 + (x[1] - x[0]**2)**2
    return round(s,2)
        
        

#-------------------------------------------------------------
# Step 5: Start Program
#-------------------------------------------------------------

Init()

for p in Pop:
    print "Chromosome:", p.Chromosome, "\t Fitness:", p.Fitness

print "\n"














