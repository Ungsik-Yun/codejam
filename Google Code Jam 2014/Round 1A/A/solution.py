from pprint import pprint


def file_into_problem(file_name):
    problem = {}
    problem["cases"] = []
    with open(file_name, 'r+') as f:
        T = int(f.readline())
        for case in xrange(T):
            N, L = [int(i) for i in f.readline().split()]
            divices = [eval("0b" + i) for i in f.readline().split()]
            outlets = [eval("0b" + i) for i in f.readline().split()]
            problem['cases'].append({
                                    'N': N,
                                    'L': L,
                                    'devices': divices,
                                    'outlets': outlets
                                    })

    return problem


def solve_prolbem(problem, file_name):
    with open(file_name + '.out', 'w+') as f:
        cases = problem['cases']
        for no, case in enumerate(cases, start=1):
            devices = case['devices']
            outlets = case['outlets']
            devices_set = set(devices)
            # devices.sort()
            # outlets.sort()
            fliped = "NOT POSSIBLE"

            for i in xrange(2 ** case['L']):
                switched = [outlet ^ i for outlet in outlets]
                # switched.sort()
                # print i, devices, switched, outlets
                print no, i
                if set(switched) == devices_set:
                    fliped = bin(i).count('1')
                    break
            f.write("Case #%d: %s\n" % (no, str(fliped)))

if __name__ == '__main__':
    # inputs = ['A-small-practice.in', 'A-large-practice.in']
    # inputs = ['A-small-practice.in']
    inputs = ['A-large-practice.in']
    # inputs = ['test.in']
    for each_file in inputs:
        p = file_into_problem(each_file)
        solve_prolbem(p, each_file)
        # pprint(p, width=30)
