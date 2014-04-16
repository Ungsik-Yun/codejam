'''
Created on 2014. 4. 16.

@author: Alice
'''

import multiprocessing
from pprint import pprint

def file_into_problem(file_name):
    with open(file_name, 'r+') as f:
        case_number = int(f.readline())
        problem = {'case_number':case_number}
        problem['cases'] = list()
        for i in xrange(case_number):
            numbers = int(f.readline())
            x = [int(n) for n in f.readline().split()]
            y = [int(n) for n in f.readline().split()]
            case = {}
            case['numbers'] = numbers
            case['x'] = x
            case['y'] = y
            case['no'] = i + 1
            problem['cases'].append(case)
    return problem

def solve_problem(problem):
    pass

if __name__ == '__main__':
    pprint (file_into_problem('a_test.in'))
