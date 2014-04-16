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
    case_number = problem['case_number']
    with open('A result.out', 'w+') as f:
        for case in problem['cases']:
            result = 0
            x = sorted(case['x'])
            y = sorted(case['y'])

            for i in xrange(len(x)):
                result += x.pop(0) * y.pop()

            f.write("Case #%d: %d\n" % (case['no'], result))

if __name__ == '__main__':
    p = file_into_problem('A-large-practice.in')
    solve_problem(p)
