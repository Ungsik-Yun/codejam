'''
Created on 2014. 4. 20.

@author: Alice
'''
from pprint import pprint


def read_problem(filename):
    with open(filename, 'r+') as f:
        number_of_cases = int(f.readline())
        cases = []
        problem = []
        for case in xrange(number_of_cases):
            pass
        return problem


def solve_problem(problem):
    with open('result.out', 'w+') as f:
        for no, case in enumerate(problem['cases'], start=1):
            pass

if __name__ == '__main__':
    p = read_problem('sample.in')
    pprint(p, width=40)
    # solve_problem(p)
