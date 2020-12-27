"""
Q.Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for i in range(1, 10+1, 1):
    if i <= 5:
        for j in range(1, i+1, 1):
            print('*', end=' ')
    else:
        for j in range(10-i, 0, -1):
            print('*', end=' ')
    print('\n')
