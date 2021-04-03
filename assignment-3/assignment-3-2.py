# 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]



stringParam = "ACADGILD"
lettersPresent = [letter for letter in stringParam]
print(stringParam + " compreRes= " + str(lettersPresent))



inputList = ['x','y','z']
result = [item*num for item in inputList for num in range(1,5)]
print("compreRes=" + str(result))



inputList = ['x','y','z']
result = [item*num for num in range(1,5) for item in inputList]
print("compreRes=" + str(result))


inputList = [2,3,4]
result = [[item+num] for item in inputList for num in range(0,3)]
print("compreRes=" + str(result))


inputList = [2,3,4,5]
result = [[item+num for item in inputList] for num in range(0,4)]
print("compreRes=" + str(result))


inputList=[1,2,3]
result = [(b,a) for a in inputList for b in inputList]
print("compreRes=" + str(result))

