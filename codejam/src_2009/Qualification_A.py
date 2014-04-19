'''
Created on 2014. 4. 16.

@author: Alice
'''


from pprint import pprint


def file_into_problem(file_name):
    with open(file_name, 'r+') as f:
        temp_txt = [int(i) for i in f.readline().split()]
        word_length, example_word_number, case_number = temp_txt[0], temp_txt[1], temp_txt[2]
        example_words = [f.readline().strip() for word in xrange(example_word_number)]
        cases = [f.readline().strip() for case in xrange(case_number)]
        problem = {
                   'cases': cases,
                   'word_length': word_length,
                   'example_words': example_words,
                   'case_number': case_number
                   }
    return problem


def solve_problem(problem):
    case_number = problem['case_number']
    example_words = problem['example_words']
    word_length = problem['word_length']
    example_transpose = [[] for i in xrange(word_length)]
    # example word transpose
    for word in example_words:
        for i, char in enumerate(word):
            example_transpose[i].append(char)
    with open('result.out', 'w+') as f:
        for no, case in enumerate(problem['cases']):
            # disassemble_word
            temp = []
            disassembled = []
            flag = False
            for c in case:
                if c == '(':
                    flag = True
                elif c == ')':
                    flag = False
                    disassembled.append(temp)
                    temp = []
                elif flag == True:
                    temp.append(c)
                else:
                    disassembled.append(c)
            assume = [[] for i in xrange(word_length)]
            assume_index = range(len(example_words))
            for i, v in enumerate(zip(disassembled, example_transpose)):
                d, e = v[0], v[1]
                for j, echar in enumerate(e):
                    delete_flag = True
                    for dchar in d:
                        if dchar == echar:
                            delete_flag = False
                    if delete_flag == True:
                        try:
                            assume_index.remove(j)
                        except ValueError:
                            pass
#             print assume_index
#             possible_number = min([len(a) for a in assume])
            possible_number = len(assume_index)
            f.write("Case #%d: %d\n" % (no + 1, possible_number))
    return

if __name__ == '__main__':
#     p = file_into_problem('A-small-practice.in')
    p = file_into_problem('A-large-practice.in')
#     p = file_into_problem('qatest.in')
    pprint(p)
    solve_problem(p)
