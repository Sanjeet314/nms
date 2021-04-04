""":arg
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""


class polygonSides(object):

    # The init method or constructor
    def __init__(self):
        # Instance Variable
        lst = []
        # iterating till the range
        for i in range(0, 3):
            ele = float(input())
            if (ele <= 0):
                print("Not in this Universe 😃")
                print("Sanjeet Handle the error")
                break
                return

            lst.append(ele)  # adding the element
        self.sides = lst

    # Retrieves instance variable
    def getSides(self):
        return self.sides


class triangle(polygonSides):
    def __init__(self):
        # Instance Variable
        polygonSides.__init__(self)

    def getHeronArea(self):
        sides = self.getSides()
        semiPerimeter = (sides[0] + sides[1] + sides[2]) / 2
        self.area = float((semiPerimeter * (semiPerimeter - sides[0]) * (semiPerimeter - sides[1]) * (
                    semiPerimeter - sides[2])) ** 0.5)

        return self.area


tryMe = triangle()
print('The area of the triangle is %0.2f' % tryMe.getHeronArea())
