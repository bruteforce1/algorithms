"""@package genrandforsorting
This module simply generates random numbers to use within the sorting 
algorithms.
"""

import random
import sys
import time

class genrandforsorting:
    def __init__(self, 
                 seed=1,
                 minimum=0, 
                 maximum=10000, 
                 count=100, 
                 filename='in.txt'):
        """Initializes genrandforsorting class."""
        self.seed = seed
        self.min = minimum
        self.max = maximum
        self.count = count
        self.filename = filename

    def genrandom(self):
        """Generates random data in output file."""
        random.seed(self.seed)
        with open(self.filename, 'w') as f:
            for i in range(self.count):
                f.write(str(random.randint(self.min, self.max)))
                f.write('\n')


def main():
    """Main function, executed if this file is run."""
    genrandforsorting(time.time()).genrandom()
    return 0

if __name__ == "__main__":
    """Execute only if run as a script."""
    main()
