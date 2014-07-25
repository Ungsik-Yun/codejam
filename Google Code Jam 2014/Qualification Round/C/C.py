'''
Created on 2014. 4. 13.

@author: Alice
'''


def file_into_problem(file_name):
    problem = {}
    with open(file_name, 'r+') as f:
        case_number = int(f.readline())
        problem['case_number'] = case_number
        problem['cases'] = []
        for i in xrange(case_number):
            problem_text = f.readline()
            problem_float = [int(n) for n in problem_text.split()]
            problem['cases'].append(problem_float)

    return problem


def solve_problem(problem):
    case_number = problem['case_number']
    case_counter = 1
    for case in problem['cases']:
        row = case[0]
        column = case[1]
        mines = case[2]
        field_size = row * column
        safty_zone = field_size - mines
        if field_size > 9 and safty_zone < 9:
            result_message = "Impossible"
            print "Case #%d:\n%s" % (case_counter, result_message)
        case_counter += 1

if __name__ == '__main__':
    p = file_into_problem('test c')
    print p
    solve_problem(p)
