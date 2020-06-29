'''
Given a function that generates a random number between 0 and 1 uniformly, estimate pi.

In order to do this, we will call the function twice to generate two numbers and use them as an X and Y coordinates on a plane.
Since this 1x1 plane is a square, we can extrapolate that out in all directions giving a full 2x2 square, with a circle inside that has a radius of 1.

In this case, the ratio of the number of points inside the quarter circle to the points in total in the 1x1 square will be roughly the same as the ratio of the area of the full circle to the area of 2x2 square.

To determine if the point is inside the circle or not, you can take the square root of the point's distance to the origin, if that is less than 1 it is in the circle.

The previously mentioned ratios would be    pi(r^2)/(2r)^2 = number points in circle / number points in square
Since we know r = 1, the equation simplifies to    pi/4 =  number points in circle / number points in square
And to solve for pi we multiply both sides by 4,    pi = 4(number points in circle / number points in square)
'''

import random

def estimate_pi(points):
    '''
    # @param points: Integer - The number of points used to estimate.
    '''
    points_circle = 0
    points_total = 0
    
    for i in range(points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if (distance <= 1):
            points_circle += 1
        # if end
        points_total += 1
    # for end
    pi = 4 * (points_circle / points_total)
    return pi
# estimate_pi end

print (estimate_pi(10))      # 2.4, 3.6, 4.0, 3.6
print (estimate_pi(100))     # 2.92, 2.92, 3.2, 3.08
print (estimate_pi(1000))    # 3.14, 3.212, 3.2, 3.184
print (estimate_pi(10000))   # 3.132, 3.1412, 3.1416, 3.1664
print (estimate_pi(100000))  # 3.13872, 3.14456, 3.14316, 3.1508
print (estimate_pi(1000000)) # 3.141316, 3.139496, 3.142384, 3.142816