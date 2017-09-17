#-------------------------------------------------------------
# To solve subset problem using randomly.
#-------------------------------------------------------------
# Problem Statement:
# Find the total number of subsets from a set of
# numbers whose sum is zero.
#
# Set={-12,-3,-6,7,2,-2,6,3,9,-7,-5,-8,1,11,-9,-4}
# Constraint: Subset size must be 3 to 6 only.
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
SetLB       = 3     # Set Size Lower Bound
SetUB       = 6     # Set Size Upper Bound
ResultList  = set()    # Store Result List i.e. list of sets whose sum is zero
Iterations  = 20000   # Number of Inerations

#-------------------------------------------------------------
# Step3: Start Program
#-------------------------------------------------------------
# Loop till number of Iterations
for i in range(Iterations):

    # Select set size randomly
    SetSize=random.randint(SetLB,SetUB)
	
    # Select number of elements from Set
    z=random.sample(Set,SetSize)
    z.sort()
    Chromosome=tuple(z)
	
    # Sum the number of elements in the Chromosome
    if sum(Chromosome) == 0:
        ResultList.add((Chromosome))

# Print all the sets whose sum is zero
for r in ResultList:
	print r

# Print total sets
print "\nTotal Sets: ", len(ResultList)







