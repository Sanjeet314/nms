# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()


def myreduce(cbFunc, sequence):


  result = sequence[0]

  for item in sequence[1:]:
   result = cbFunc(result, item)

  return result

# test myreduce
def sum(x,y): return x + y

print (str(myreduce(sum, [1,2,3])) )