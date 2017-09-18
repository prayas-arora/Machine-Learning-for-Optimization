#-------------------------------------------------------------
# To solve Set Partition Problem using randomly.
#-------------------------------------------------------------
# Problem Statement:
# Partition a set into two sub sets such that the difference
# between sum of subsets is min.
#
# Set=[12,23,26,27,22,25,36,13,39,17,15,18,21,11,19,14]
# Constraint: Difference in set size not greater than 5.
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
setMain     = set([12,23,26,27,22,25,36,13,39,17,15,18,21,11,19,14])
set1        = set() # Subset 1
set2        = set() # Subset 2

iterations  = 100  # Number of Inerations

#-------------------------------------------------------------
# Step3: Start Program
#-------------------------------------------------------------
# Loop till number of Iterations

for i in range(iterations):

    # Select a set size randomly
    setSize=random.randint(len(setMain)/2,len(setMain)/2+3)

    # Set1
    s1=set(random.sample(setMain,setSize))
    sumS1=sum(s1)
    
    # Set2
    s2=setMain - s1
    sumS2=sum(s2)

    if i==1:
        set1=s1
        set2=s2
    sumSet1=sum(set1)
    sumSet2=sum(set2)

    if abs(sumSet1 - sumSet2) > abs(sumS1 - sumS2):
        set1=s1
        set2=s2

    print i,"\t", abs(sum(set1) - sum(set2))

print set1,"\n",set2











