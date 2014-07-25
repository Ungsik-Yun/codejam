def file_into_problem(file_name):
    problem = {}
    problem["cases"] = []
    with open(file_name, 'r+') as f:
        T = int(f.readline())
        problem["T"] = T
        for case in xrange(T):
            N = int(f.readline().strip())
            naomi = [float(i) for i in f.readline().split()]
            ken = [float(i) for i in f.readline().split()]
            case = {"N": N,
                    "naomi": naomi,
                    "ken": ken
                    }
            problem['cases'].append(case)
    return problem


def solve_prolbem(problem, file_name):
    with open(file_name + '.out', 'w+') as f:
        cases = problem['cases']
        for no, case in enumerate(cases, start=1):
            # war
            naomi = list(case['naomi'])
            ken = list(case['ken'])

            naomi.sort(reverse=True)
            ken.sort(reverse=True)

            war_score_board = {'naomi': 0, 'ken': 0}
            for n in xrange(case['N']):
                naomi_chosen = naomi.pop()
                ken_chosen_cadidate = [
                    chosen for chosen in ken if chosen > naomi_chosen]

                if len(ken_chosen_cadidate) == 0:
                    ken_chosen = ken.pop()
                else:
                    ken_chosen = min(ken_chosen_cadidate)
                    ken.remove(ken_chosen)

                if ken_chosen > naomi_chosen:
                    war_score_board['ken'] += 1
                else:
                    war_score_board['naomi'] += 1

            # Deceitful war
            naomi = list(case['naomi'])
            ken = list(case['ken'])

            naomi.sort(reverse=True)
            ken.sort(reverse=True)

            deceitful_war_score_board = {'naomi': 0, 'ken': 0}
            for n in xrange(case['N']):

                if min(naomi) < min(ken):
                    naomi_chosen = naomi.pop()
                    naomi_tell = max(ken) - 0.00001
                elif min(naomi) > min(ken):
                    naomi_chosen = naomi.pop()
                    naomi_tell = max(ken) + 0.00001

                ken_chosen_cadidate = [
                    chosen for chosen in ken if chosen > naomi_tell]

                if len(ken_chosen_cadidate) == 0:
                    ken_chosen = ken.pop()
                else:
                    ken_chosen = min(ken_chosen_cadidate)
                    ken.remove(ken_chosen)

                # print "%d: %.6f\t%.6f\t%.6f" % (no, naomi_chosen, naomi_tell,
                # ken_chosen)

                if ken_chosen > naomi_tell:
                    deceitful_war_score_board['ken'] += 1
                else:
                    deceitful_war_score_board['naomi'] += 1

            f.write("Case #%d: %d %d\n" %
                    (no, deceitful_war_score_board['naomi'], war_score_board['naomi']))


if __name__ == '__main__':
    inputs = ['test.in', 'D-small-practice.in', 'D-large-practice.in']
    # inputs = ['test.in']
    for each_file in inputs:
        p = file_into_problem(each_file)
        solve_prolbem(p, each_file)
        # pprint(p,width=30)
