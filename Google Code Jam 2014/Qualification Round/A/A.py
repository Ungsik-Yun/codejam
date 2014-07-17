'''
Created on 2014. 4. 13.

@author: Alice
'''

from pprint import pprint

def file_to_problem(f):
    '''
    {'case_number': 100,
     'cases': [{'first': {'answer': 2,
                          'cards': [['7', '9', '1', '5'],
                                    ['15', '16', '14', '11'],
                                    ['13', '3', '12', '4'],
                                    ['10', '8', '6', '2']]},
                'no': 0,
                'second': {'answer': 3,
                           'cards': [['3', '14', '10', '4'],
                                     ['7', '16', '11', '5'],
                                     ['8', '12', '15', '9'],
                                     ['13', '2', '1', '6']]}},
    ...

    '''

    problem = {}
    with open(f, 'r+') as problem_file:
        case_number = int(problem_file.readline())
        problem['case_number'] = case_number
        problem['cases'] = []
        line_number = 0
        for i in xrange(case_number):
            problem['cases'].append(dict())
            problem['cases'][i] = {'no' : i + 1}

            problem['cases'][i]['first'] = {'answer': int(problem_file.readline())}
            problem['cases'][i]['first']['cards'] = []
            for j in xrange(4):
                problem['cases'][i]['first']['cards'].append([card for card in problem_file.readline().split()])

            problem['cases'][i]['second'] = {'answer': int(problem_file.readline())}
            problem['cases'][i]['second']['cards'] = []
            for j in xrange(4):
                problem['cases'][i]['second']['cards'].append([card for card in problem_file.readline().split()])

    return problem


def solve_problem(problem):
    print 'Start problem solving...'
    case_number = problem['case_number']
    if case_number > 100:
        exit('casenumber over 100!')
    if case_number < 1:
        exit('casenumber under 1!')
    cases = problem['cases']
    with open('result A.txt', 'w+') as f:
        for case in cases:
            first_answer = case['first']['answer']
            second_answer = case['second']['answer']

            first_candidate = case['first']['cards'][first_answer - 1 ]
            second_candidate = case['second']['cards'][second_answer - 1]
            result = []
            for n in first_candidate:
                if n in second_candidate:
                    result.append(n)

            result_message = ''
            if len(result) == 1:
                result_message = str(result[0])
            elif len(result) == 0:
                result_message = 'Volunteer cheated!'
            else:
                result_message = 'Bad magician!'


            print "Case #%s: %s" % (case['no'], result_message)

            f.write("Case #%s: %s\n" % (case['no'], result_message))

if __name__ == '__main__':
    f = 'A-small-attempt1.in'

    problem = file_to_problem(f)
    solve_problem(problem)
