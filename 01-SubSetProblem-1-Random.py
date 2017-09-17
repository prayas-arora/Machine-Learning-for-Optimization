#-------------------------------------------------------------
# To solve subset problem using randomly.
#-------------------------------------------------------------
# Problem Statement:
# Find the total number of subsets from a set of
# numbers whose sum is zero.
#
# Set={-12,-3,-6,7,2,-2,6,3,9,-7,-5,-8,1,11,-9,-4}
# Constraint: Subset size must be 5
#-------------------------------------------------------------
# Python version: 2.6 / 2.7
#-------------------------------------------------------------




#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random
    

#-------------------------------------------------------------
# Step 2: Parameter Setting
#-------------------------------------------------------------
Set         = set([-12,-3,-6,7,2,-2,6,3,9,-7,-5,-8,1,11,-9,-4])
SetSize     = 5
ResultList  = set()    # Store Result List i.e. list of sets whose sum is zero
Iterations  = 5000   # Number of Iterations


#-------------------------------------------------------------
# Step3: Start Program
#-------------------------------------------------------------

# Loop till number of Iterations
for i in range(Iterations):
    # Select number of elements from Set
    Chromosome=tuple(random.sample(Set,SetSize))
    
    # Sum the number of elements in the Chromosome
    if sum(Chromosome) == 0:
        ResultList.add((Chromosome))

# Print all the sets whose sum is zero
for r in ResultList:
	print r

# Print total sets
print "\nTotal Sets: ", len(ResultList)







