from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    '''
    An advanced point class that extends ColorPoint and adds
    properties, class methods, and static methods.
    '''
    COLORS = ["red", "blue", "green", "yellow", "periwinkle", "black", " white"]
    def __init__(self, x,y, color):
        '''
        Initialize (create and set up) an AdvancedPoint object.
        :param x: x-coordinate
        :param y: y-coordinate
        :param color: color of the point, must be in COLORS
        '''
        if color not in self.COLORS:
            raise PointException(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        '''
        Getter (returns) for x-coordinate.
        :return: x value
        '''
        return self._x #getter method

    @x.setter
    def x(self, value):
        '''
        Setter (change the value returned on getter function) for x-coordinate.
        :param value: new x value
        :return: None
        '''
        self._x = value #"setter" method

    @property
    def y(self):
        '''
        Getter (returns) for y-coordinate.
        :return: y value
        '''
        return self._y

    @property
    def color(self):
        '''
        Getter (returns) for color.
        :return: color of the point
        '''
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color for our class
        :return: new color to add
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color = "red"):
        """
        Create a new point from a tuple rather than 2 individual values
        :param coordinate: tuple with (x, y)
        :param color: color of the point (default is "red")
        :return: new AdvancedPoint instance
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1,p2):
        '''
        Calculate distance between two points p1 and p2.
        :param p1: first AdvancedPoint
        :param p2: second AdvancedPoint
        :return: distance between p1 and p2
        '''
        return((p1.x - p2.x) ** 2 + (p1.y - p2.y)**2) ** 0.5

    def distance_to_other(self, p):
        '''
        Calculate distance from this point (self) to another point.
        :param p: another AdvancedPoint
        :return: distance to point p
        '''
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "rojo")
print(p.x)
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p,p2))
print(p.distance_to_other(p2))