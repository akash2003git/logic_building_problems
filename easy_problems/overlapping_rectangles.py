# Given two rectangles, find if the given two rectangles overlap or not.
# Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates. 
# l1: Top Left coordinate of first rectangle. 
# r1: Bottom Right coordinate of first rectangle. 
# l2: Top Left coordinate of second rectangle. 
# r2: Bottom Right coordinate of second rectangle.
# Note : It may be assumed that the rectangles are parallel to the coordinate axis.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def do_overlap(l1, r1, l2, r2):
    if (l2.x > r1.x or l1.x > r2.x):
        return False
    if (r2.y > l1.y or r1.y > l2.y):
        return False
    return True

if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if do_overlap(l1, r1, l2, r2):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")
