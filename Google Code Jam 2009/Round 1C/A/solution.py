from pprint import pprint

def file_into_problem(file_name):
    problem = {}
    cases = []
    with open(file_name, 'r+') as f:
        T = int(f.readline())
        for i in xrange(T):
            cases.append(f.readline().strip())

    problem['T'] = T
    problem['cases'] = cases
    return problem


def solve_problem(problem):

    cases = problem['cases']
    with open('result.out', 'w+') as f:

        for no, case in enumerate(cases, start=1):
            base = len(set(case))
            number_dict = {i: -1 for i in set(case)}

            # find appear oder
            counter = 1
            for index, enc_num in enumerate(case):
                if number_dict[enc_num] == -1:
                    if counter == 2:
                        number_dict[enc_num] = 0
                    else:
                        number_dict[enc_num] = counter
                    counter += 1

            # set correct number to number_dict.
            for i, v in number_dict.items():
                if v > 2:
                    number_dict[i] -= 1

            # calculate minimum time
            minimum_time = 0
            # print case
            if base == 1:
                base = 2
            for i, c in enumerate(case[::-1]):
                # print i, c, number_dict[c], int(number_dict[c])*(base**i)
                minimum_time += int(number_dict[c])*(base**i)
            # print minimum_time
            f.write("Case #%d: %s\n" % (no, minimum_time))
    return

if __name__ == '__main__':
    # p = file_into_problem('A-small-practice.in')
    p = file_into_problem('A-large-practice.in')
    # p = file_into_problem('test.in')
    # pprint(p, width=30)
    solve_problem(p)
