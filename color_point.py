from point import Point
import random

# This is a custom exception for points
class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        '''
        Initialize (create and set up) a ColorPoint object.
        :param x: the x position (must be int or float)
        :param y: the y position (must be int or float)
        :param color: the color of the point
        '''
        #raise an exception if we try to have not a number
        if not isinstance(x,(int, float)): #if its not an integer and float
            raise TypeError("x must be an number") #generate the type error
        if not isinstance(y,(int,float)):
            raise TypeError("y must be an number")

        super().__init__(x,y) #this replaces the self.x and self.y
        self.color = color

    def __str__(self):
        '''
        Represents ColorPoint in a string.
        :return: string in the format <color: x, y>
        '''
        return f"<{self.color}: {self.x}, {self.y}>"
if __name__ == "__main__":
    '''
    Run some tests if the file is executed directly.
    '''
    p = ColorPoint(1,2,"red")
    print(p.distance_orig())
    print(p)
    # colors = ["red", "green", "blue", "yellow", "black", "magenta",
    #           "cyan", "white", "burgundy", "periwinkle", "marsala"]
    # color_points = []
    # for i in range(10):
    #     color_points.append(
    #         ColorPoint(random.randint(-10,10),
    #                                    random.randint(-10,10),
    #                                    random.choice(colors)))
    # print(color_points)
    # color_points.sort()
    # print(color_points)
