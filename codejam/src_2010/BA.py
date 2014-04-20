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
            temp = [int(n) for n in f.readline().split()]
            exist_number, to_make_number = temp[0], temp[1]
            exist_paths = [f.readline().strip() for i in xrange(exist_number)]
            to_make_paths = [f.readline().strip() for i in xrange(to_make_number)]
            cases.append({
                          'exist_number':exist_number,
                          'exist_paths':exist_paths,
                          'to_make_number':to_make_number,
                          'to_make_paths':to_make_paths
                          })
        problem = {
                   'cases':cases,
                   'number_of_cases':number_of_cases
                   }
        return problem


def make_tree(exist_paths, to_be_added_path):
    creation_count = 0
    result = exist_paths
# create exist path tree
    for path in to_be_added_path:
        target = result
        for directory in path:
            if directory not in target:
                target[directory] = dict()
                target = target[directory]
                creation_count += 1
            elif directory != '':
                target = target[directory]

    return (result, creation_count)


def solve_problem(problem):
    with open('result.out', 'w+') as f:
        number_of_cases = problem['number_of_cases']
        for no, case in enumerate(problem['cases'], start = 1):
            exist_number, to_make_number = case['exist_number'], case['to_make_number']
            exist_paths, to_make_paths = [path.split('/') for path in case['exist_paths']], [path.split('/') for path in case['to_make_paths']]

            # only has root
            if exist_number == 0:
                exist_paths.append([''])
            initail_tree = {'':{}}
            result, counter = make_tree(initail_tree, exist_paths)
            result, counter = make_tree(result, to_make_paths)
#             print counter
            f.write("Case #%d: %d\n" % (no, counter))


if __name__ == '__main__':
#     p = read_problem('batest.in')
#     p = read_problem('A-small-practice.in')
    p = read_problem('A-large-practice.in')
    solve_problem(p)
