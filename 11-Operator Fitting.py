
import random

seq=['6','5','4','3','2']
target=32

op=['+','-','*','/']

for x in range(100):
  finalSeq=[]
  finalSeq.append(seq[0])
  for i in seq[1:]:
    finalSeq.append(''.join(random.sample(op,1)))
    finalSeq.append(i)
  exp=''.join(finalSeq)
  print exp, eval(exp)
  
  if eval(exp) ==target:
    break
  
print "Done"






