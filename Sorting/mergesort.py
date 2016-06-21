"""@package mergesort
This module is a working merge sort for learning purposes.

Merge sort runs in time O(n lg n) = 2T(n/2) + O(n).  Replace "O" with
Big Theta, as this is the average case.

It is a divide-and-conquer algorithm, as it breaks the problem
recursively into subproblems (divide), solves each problem individually
(conquer), then combines the solutions back together. 
"""

import argparse
import math
import os.path

def merge(la, lb):
    """Merge function which handles the combining of subarrays."""
    lc = []
    

def mergesort(mylist):
    """Merge sort function, handles divide and conquer."""
    if (len(mylist) <= 1):
        return mylist
    a = mergesort(mylist[:math.floor(len(mylist)/2)])
    b = mergesort(mylist[math.floor(len(mylist)/2)+1:])
    return merge(a,b)

def main(inputfile, outputfile):
    """Main function, executed if this file is run."""
    if not os.path.exists(inputfile):
        return -1

    tosort = []
    with open(inputfile, 'r') as f:
        for line in f:
            tosort.append(int(line.rstrip()))

    sortlist = mergesort(tosort)
    with open(outputfile, 'w') as o:
        for num in sortlist:
            o.write(str(num))

    return 0

if __name__ == '__main__':
    """Execute only if run as a script."""
    parser = argparse.ArgumentParser(description='Merge sort example.')
    parser.add_argument("inputfile", 
                       help="Input file with data to sort.")
    parser.add_argument("outputfile", 
                       help="Destination file for sorted output.")
    args = parser.parse_args()
    main(args.inputfile, args.outputfile)
