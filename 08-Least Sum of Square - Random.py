#-------------------------------------------------------------
#                       LSS: Least Sum of Square
#-------------------------------------------------------------
# To solve Least Sum of Square (LSS) using randomly.
#-------------------------------------------------------------
# Python version used: 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
import csv
import numpy as np
from copy import deepcopy

startTime = time.time()

#-------------------------------------------------------------
# Step 2: Parameters
#-------------------------------------------------------------

# 2.1 Random Algorithm Parameters
algoName    = "RandomBasic"	# Algo Name

# 2.2 Global Parameters
iterations  = 200       # Number of Iterations
maxFunEval  = 100000    # Maximum allowable function evaluations
funEval	    = 0		# Count function evaluations
bestFitness = 99999999  # Store Best Fitness Value
bestChromosome = []     # Store Best Chromosome

# 2.3 Result Saving Parameters
resultFileName="result"+algoName+".csv"

# 2.4 Problem parameters
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

# Saving Result
fp=open(resultFileName,"w")
fp.write("Iteration,Fitness,Chromosome\n")

# Running till number of iterations
for i in range(0,iterations):
  chromosome = []
  for j in range(0,D):
    chromosome.append(round(random.uniform(LB,UB),2))
  fitness = FitnessFunction(chromosome)
  funEval = funEval + 1
  if fitness < bestFitness:
    bestFitness=fitness
    bestChromosome=chromosome
  if funEval >=maxFunEval:
    break
    
  if i%10==0:
    print "I:",i,"\t Fitness:",bestFitness
    fp.write(str(i) + "," + str(bestFitness)+ "," + str(bestChromosome) + "\n")

print "I:",i+1,"\t Fitness:",bestFitness
fp.write(str(i+1) + "," + str(bestFitness)+ "," + str(bestChromosome) + "\n")
fp.close()

print "Done"
print "\nBestFitness:", bestFitness
print "Best chromosome:", bestChromosome
print "Total Function funEval: ",funEval
print "Result is saved in", resultFileName
print "Total Time Taken: ", round(time.time() - startTime,2), " sec\n"

