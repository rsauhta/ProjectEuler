# https://projecteuler.net/problem=102
#
# Three distinct points are plotted at random on a Cartesian plane, for which -1000 = x, y = 1000, such that a triangle is formed.
# 
# Consider the following two triangles:
# 
# A(-340,495), B(-153,-910), C(835,-947)
# 
# X(-175,41), Y(-421,-714), Z(574,-645)
# 
# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
# 
# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
# 
# NOTE: The first two examples in the file represent the triangles in the example given above.
# 


from collections import namedtuple

Point = namedtuple('Point', 'x y')


# Area computed using cartesian cooridnates, per wikipedia
def triangleArea(p1, p2, p3):
        return 0.5*abs(p1.x*p2.y - p1.x*p3.y + p2.x*p3.y - p2.x*p1.y + p3.x*p1.y - p3.x*p2.y)
        


def testTriangleArea():
        assert(triangleArea(Point(0,2), Point(0,0), Point(2,0)) == 2)
        assert(triangleArea(Point(0,10), Point(0,0), Point(10,0)) == 
               triangleArea(Point(2,12), Point(2,2), Point(12,2)))



#testTriangleArea()
Filename = "p102_triangles.txt"
totalCounter=0
triangleWithOrigin=0

origin = Point(0,0)

with open(Filename) as f:
        for line in f:
                points = line.split(',')    # no error checking 
                p1 = Point(int(points[0]), int(points[1]))
                p2 = Point(int(points[2]), int(points[3]))
                p3 = Point(int(points[4]), int(points[5]))

                totalCounter +=1
                if (triangleArea(p1,p2,p3) == (triangleArea(p1,p2,origin) + triangleArea(p1,origin,p3) + triangleArea(origin,p2,p3))) :
                        triangleWithOrigin += 1


                
print "Total = ", totalCounter
print "Triangle with origin = ", triangleWithOrigin

