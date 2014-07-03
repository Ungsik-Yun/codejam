'''
Created on 2014. 7. 3.

@author: Alice
'''
from pprint import pprint


def read_problem(filename):
    with open(filename, 'r+') as f:
        number_of_cases = int(f.readline())
        problem = []
        for case in xrange(number_of_cases):
            tmp = f.readline().split()
            n, k = int(tmp[0]), int(tmp[1])
            problem.append({"n": n, "k": k})
            board = []
            for line in xrange(n):
                board.append(f.readline().strip())
            problem[case]["board"] = board
        return problem


def solve_problem(problem):
    with open('result.out', 'w+') as f:
        for no, case in enumerate(problem, start=1):
            gravited_board = gravity_from_right(case['board'])
            winner = check_winner(gravited_board, case['k'])
            print "No.",no, ":",case['k'], winner
            pprint(gravited_board, width=10)
            f.write("Case #%d: %s\n" % (no, winner))


def gravity_from_right(board):
    n = len(board)

    gravited = []
    for line in board:
        gravited.append(line.replace(".","").rjust(len(board),"."))

    return gravited


def check_winner(board, k):
    n = len(board)
    red_target = "R"*k
    blue_target = "B"*k
    is_red_win = False
    is_blue_win = False

    for line in board:
        # check horizon
        is_red_win = is_red_win or (line.find(red_target) >= 0)
        is_blue_win = is_blue_win or (line.find(blue_target) >= 0)


    for column_no in xrange(len(line)):
        # check vertical
        column = ""
        for line in board:
            column += line[column_no]
        is_red_win = is_red_win or (column.find(red_target) >= 0)
        is_blue_win = is_blue_win or (column.find(blue_target) >= 0)


    right_lower_board = [i[::-1] for i in board[::-1]]
    for diagonal_no in xrange(n):
        diagonal_left_upper = ""
        diagonal_right_lower = ""
        for line in xrange(diagonal_no+1):
            diagonal_left_upper += board[line][diagonal_no-line]
            diagonal_right_lower += right_lower_board[line][diagonal_no-line]
        is_red_win = is_red_win or (diagonal_left_upper.find(red_target) >= 0)
        is_blue_win = is_blue_win or (diagonal_left_upper.find(blue_target) >= 0)
        is_red_win = is_red_win or (diagonal_right_lower.find(red_target) >= 0)
        is_blue_win = is_blue_win or (diagonal_right_lower.find(blue_target) >= 0)


    left_lower_board = [i[::-1] for i in board[::-1]]
    for column_no in xrange(n):
        diagonal_left_lower = ""
        diagonal_right_upper = ""
        for line in xrange(column_no-1,-1,-1):
            diagonal_left_lower += board[line][column_no-line-1]
            diagonal_right_upper += left_lower_board[line][column_no-line-1]
        is_red_win = is_red_win or (diagonal_left_lower.find(red_target) >= 0)
        is_blue_win = is_blue_win or (diagonal_left_lower.find(blue_target) >= 0)
        is_red_win = is_red_win or (diagonal_right_upper.find(red_target) >= 0)
        is_blue_win = is_blue_win or (diagonal_right_upper.find(blue_target) >= 0)


    if is_red_win and is_blue_win:
        result = "Both"
    elif is_red_win:
        result = "Red"
    elif is_blue_win:
        result = "Blue"
    else:
        result = "Neither"

    return result


if __name__ == '__main__':
    # p = read_problem('A-small-practice.in')
    p = read_problem('sample.in')
    # pprint(p, width=10)
    solve_problem(p)
