# BIODS253 Assignment 1
# Original Author: Eashan M.
# Modified by: Gustavo A. Araújo R.

from math import comb

def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(comb(i,j), end=" ")
        print("\n")

pascal_triangle(10)