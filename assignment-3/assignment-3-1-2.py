# 1.2 Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()


def myfilter(anyfunc, sequence):

    result = []

    for item in sequence:
        if anyfunc(item):
            result.append(item)


    return result

# test myfilter function
def ispositive(x):
 if (x <= 0):
  return False
 else:
  return True

print (str(myfilter(ispositive, [-1, 1, 2])))
