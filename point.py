import random

class Point:
    '''
    A class that represents a point in 2D space
    '''

    :param x: the x-coordinate (position on the horizontal axis)
    :param y: the y-coordinate (position on the vertical axis)
    def __init__(self,x,y):
        '''
        Initialize (create and set up) a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        '''
        self.x = x # define x attribute via self.x
        self.y = y # and assign the value x to it

    def __str__(self):
        '''
        Magic method that is called when we try to print an instance
        :return: <x,y>
        '''
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        '''
        Magic method that is called when we try to represent an instance
        :return: <x,y>
        '''
        return self.__str__() # use the same way of printing as str

    def distance_orig(self):
        '''
        Calculate the distance from the point to the origin (0,0)
        :return: the distance from point to the origin
        '''
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x and y squared

    def __gt__(self, other):
        '''
         Compare two points distances based on their distance to the origin.
        :param other: another Point
        :return: True if self is farther than the other point
        '''
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        '''
        See if two points are at the same distance from the origin.
        :param other: another point
        :return: True if the distances of the self and the other point is equal
        '''
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance
if __name__ == "__main__":
    # now we need to instantiate it! #instantiate you create a particular point
    p = Point(1,2) # p is an instance of 1 and 2
    print(f"p.x = {p.x} and p.y = {p.y}")
    p.x = 20
    print(f"p.x = {p.x} and p.y = {p.y}")
    print(p)
    #create a list of 5 random point
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10,10), # x value
                                           random.randint(-10,10))) # y value
    print("I got these 5 random points: ")
    print(points)
    p = Point(3, 4)
    print(p.distance_orig()) # expect 5 answer
    p2 = Point(1, 1)
    print(f" I am comparing p and p2: {p > p2}") # I expect to have True
    print("the sorted list of points is: ")
    points.sort()
    print(points)
