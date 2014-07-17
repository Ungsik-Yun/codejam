'''
Created on 2014. 4. 16.

@author: Alice
'''


def file_into_problem(file_name):
    with open(file_name, 'r+') as f:
        case_number = int(f.readline())
        problem = []
        for i in xrange(case_number):
            problem.append(f.readline().split())

        return problem


def solve_problem(p):
    with open('b_result.out', 'w+') as f:
        for i in xrange(len(p)):
            f.write("Case #%d: " % (i + 1))
            for word in p[i][::-1]:
                f.write('%s ' % word)
            f.write('\n')

if __name__ == '__main__':
    p = file_into_problem('B-large-practice.in')
    solve_problem(p)
