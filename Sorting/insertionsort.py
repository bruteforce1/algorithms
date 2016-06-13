#!/usr/bin/python3

import argparse
import os.path
import random
import sys
import string

def gen_random_data(filename, lines):
    with open(filename, 'w') as f:
        for i in range(lines):
            f.write(str(random.randint(0, lines*1000)) + '\n')

def insertion_sort(filename):
    if not os.path.isfile(filename):
        return ''
    
    ans = []
    with open(filename, 'r') as f:
        for line in f:
            ans.append(int(line))

    for j in range(1,len(ans)):
        pos = j
        for i in range(j-1, -1, -1):
            if ans[pos] < ans[i]:
                temp = ans[pos]
                ans[pos] = ans[i]
                ans[i] = temp
                pos -= 1
            else:
                break

    with open('ins_sort.txt', 'w') as f:
        for i in ans:
            f.write(str(i) + '\n')

def main():
    print('Generating random data...')
    gen_random_data('temp.txt', 10000)
    print('Insertion sort...')
    insertion_sort('temp.txt')
    print('Done!')
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Simple insertion sort from memory.'
        )
    args = parser.parse_args()

    sys.exit(main())

