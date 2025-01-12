# BIODS253 Assignment 1
# Original Author: Eashan M.
# Modified by: Gustavo A. Araújo R.

from math import comb
import argparse

def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(comb(i,j), end=" ")
        print("\n")

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description="Print `n_rows` lines from Pascal's triangle and optionally time how long it takes to generate it.")
    parser.add_argument('n_rows', metavar='n_rows', type=int, nargs="?", default=15,
                    help="number of lines to print from Pascal's triangle")
    args = parser.parse_args()
    parser.print_help()    
    
    # Print lines
    print(f"\nOutput: These are the first {args.n_rows} lines of Pascal's triangle ")
    pascal_triangle(args.n_rows)
