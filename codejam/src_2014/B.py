'''
Created on 2014. 4. 13.


@author: Ungsik Yun
'''

from pprint import pprint

def file_into_problem(file_name):
    problem = {}
    with open(file_name, 'r+') as f:
        case_number = int(f.readline())
        problem['case_number'] = case_number
        problem['cases'] = []
        for i in xrange(case_number):
            problem_text = f.readline()
            problem_float = [float(n) for n in problem_text.split()]
            problem['cases'].append(problem_float)

    return problem

def solve_prolbem(problem):
    with open('result B3.txt', 'w+') as f:
        limit = 150
        defalut_produce_rate = 2
        case_number = 1
        for case in problem['cases']:
            farm_cost = case[0]
            farm_produce = case[1]
            target = case[2]

            produce_rate = defalut_produce_rate
            farm_buy_timetable = []
            estimate_table = [target / produce_rate]
            for farm_number in xrange(limit):
                for i in xrange(farm_number):
                    farm_buy_timetable.append(farm_cost / produce_rate)
                    produce_rate += farm_produce

                    s = sum(farm_buy_timetable)
                    r = s + target / produce_rate
                    estimate_table.append(r)
#             print farm_buy_timetable
#             print estimate_table
            result = min(estimate_table)
            f.write("Case #%d: %.7f\n" % (case_number, result))
            case_number += 1



if __name__ == '__main__':
#     p = file_into_problem('B-small-attempt1.in')
    p = file_into_problem('B-large.in')
#     p = file_into_problem('test b')
    solve_prolbem(p)
