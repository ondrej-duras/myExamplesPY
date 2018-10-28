#!/usr/bin/env python2

"""
Pocitajme sustavu rovnic:
 3*X0 +   X1 = 9
   X0 + 2*X1 = 8

Teda
 | 3, 1|   |X0|   |9|
 | 1, 2| x |X1| = |8|
 
Korene rovnice su potom:
"""

import numpy

a=numpy.array([[3,1],[1,2]])
b=numpy.array([9,8])
x=numpy.linalg.solve(a,b)

print __doc__
print x


