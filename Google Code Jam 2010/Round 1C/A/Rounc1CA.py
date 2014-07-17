'''
Created on 2014. 4. 20.

@author: Alice
'''
from pprint import pprint


def read_problem(filename):
    with open(filename, 'r+') as f:
        number_of_cases = int(f.readline())
        cases = []
        for case in xrange(number_of_cases):
            lines = []
            number_of_lines = int(f.readline())
            for line in xrange(number_of_lines):
                lines.append([int(l) for l in f.readline().split()])
            cases.append(lines)
        problem = {
                   'cases':cases,
                   'number_of_cases':number_of_cases,
                   }
        return problem


def solve_problem(problem):
    with open('result.out', 'w+') as f:
        for no, case in enumerate(problem['cases'], start = 1):
            numbers_of_lines = len(case)
            sum_of_intersection = 0
            for line in case:
                intersection_counter = 0
                for y in xrange(numbers_of_lines):
                    if line[0] < case[y][0] and line[1] > case[y][1]:
                        intersection_counter += 1
                sum_of_intersection += intersection_counter
            f.write("Case #%d: %d\n" % (no, sum_of_intersection))
if __name__ == '__main__':
    p = read_problem('A-large-practice.in')
    pprint(p, width = 40)
    solve_problem(p)
