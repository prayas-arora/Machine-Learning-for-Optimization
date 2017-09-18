#-------------------------------------------------------------
#                       LSS: Least Sum of Square
#-------------------------------------------------------------
# To solve Least Sum of Square (LSS) using DE.
#-------------------------------------------------------------
# Python version used: 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
import numpy as np
from copy import deepcopy


startTime = time.time()

#-------------------------------------------------------------
# Step 2: Parameters
#-------------------------------------------------------------

# 2.1 DE Parameters
algoName    = "DEBasic" # Algo Name
CR 	    = 0.9  	# Crossover Rate
F 	    = 0.5       # Inertiea

# 2.2 Global Parameters
iterations  = 200       # Number of iterations
popSize     = 100       # Population Size(i.e Number of Chromosomes)
pop         = []        # Store Population with Fitness
maxFunEval  = 100000    # Maximum allowable function evaluations
funEval	    = 0		# Count function evaluations
bestFitness = 99999999  # Store Best Fitness Value
bestChromosome = []     # Store Best Chromosome


# 2.3 Result Saving Parameters
resultFileName="result"+algoName+".csv"


# 2.4 Stores Chromosome and its fitness collectively
class Individual:
    def __init__(self, C, F):
        self.chromosome=C
        self.fitness=F

# 2.5 Problem parameters
# These parameters will be re assingment later
inputFileName   = "inputData.csv"   # input data file name
D               = 0     # Problem Dimension
total           = 0     # Total no of records(rows)
LB              = 0     # Set Size Lower Bound
UB              = 0     # Set Size Upper Bound

        
#-------------------------------------------------------------
# Step 3: Fitness Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
def FitnessFunction(x):
    global dataSet
    s=0
    for i in range(total):
        s = s + abs(dataSet[i][0] - dataSet[i,1:].dot(x))
    return round(s,2)
                

# Function 2: Generate Random Initial population
def Init():
    global funEval
    for i in range (0, popSize):
        chromosome = []
        for j in range(0,D):
            chromosome.append(round(random.uniform(LB,UB),2))
        fitness = FitnessFunction(chromosome)
        funEval = funEval + 1
        newIndividual = Individual(chromosome,fitness)
        pop.append(newIndividual)
        

# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest():
    global bestFitness,bestChromosome
    for p in pop:
        if p.fitness < bestFitness:
            bestFitness=p.fitness
            bestChromosome = deepcopy(p.chromosome)


# Function 4: Perform DE Operation
def DEOperation():
    global funEval
    for i in range(0,popSize):

        # Choose three random indices
        i1,i2,i3=random.sample(range(0,popSize), 3)

	# Iterate for every Dimension
        newChild=[]
        for j in range(D):
            if (random.random() <= CR):
                k = pop[i1].chromosome[j] + \
                    F * (pop[i2].chromosome[j] - pop[i3].chromosome[j])

                # If new dimention cross LB
                if k < LB:
                    k = random.uniform(LB,UB)

                # If new dimention cross LB
                if k > UB:
                    k = random.uniform(LB,UB)
                
                newChild.append(round(k,2))
                
            else:
                newChild.append(pop[i].chromosome[j])

	# Child Fitness
        newChildFitness=FitnessFunction(newChild)
        funEval = funEval + 1
		
        # Select between parent and child
        if newChildFitness < pop[i].fitness:
            pop[i].fitness=newChildFitness
            pop[i].chromosome=newChild
                

    
#-------------------------------------------------------------
# Step 4: Start Program
#-------------------------------------------------------------

# Reading Data: from CSV to Matrix
dataSet=np.loadtxt(open(inputFileName,"r"),delimiter=",",skiprows=1)

# Re assinging problem parameters
D       = dataSet.shape[1] - 1  # Problem Dimension
total   = dataSet.shape[0]      # Total no of records(rows)
LB      = -10  # Set Size Lower Bound
UB      = 10   # Set Size Upper Bound

Init()
globalBest=pop[0].chromosome
globalBestFitness=pop[0].fitness
MemoriseGlobalBest()

# Saving Result
fp=open(resultFileName,"w")
fp.write("Iteration,Fitness,Chromosome\n")


# Running till number of iterations
for i in range(0,iterations):
    DEOperation()
    MemoriseGlobalBest()
	
    if funEval >=maxFunEval:
        break

    if i%10==0:
        print "I:",i,"\t Fitness:", bestFitness
        fp.write(str(i) + "," + str(bestFitness) + "," + str(bestChromosome) + "\n")

print "I:",i+1,"\t Fitness:", bestFitness
fp.write(str(i+1) + "," + str(bestFitness) + "," + str(bestChromosome))    
fp.close()

print "Done"
print "\nBestFitness:", bestFitness
print "Best chromosome:", bestChromosome
print "Total Function funEval: ",funEval
print "Result is saved in", resultFileName
print "Total Time Taken: ", round(time.time() - startTime,2), " sec\n"






