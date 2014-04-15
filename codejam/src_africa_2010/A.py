# -*- coding: utf-8 -*-
'''
Created on 2014. 4. 14.

Problem

You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first).

Input

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

One line containing the value C, the amount of credit you have at the store.
One line containing the value I, the number of items in the store.
One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
Each test case will have exactly one solution.
Output

For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.

Limits

5 �� C �� 1000
1 �� P �� 1000

Small dataset

N = 10
3 �� I �� 100

Large dataset

N = 50
3 �� I �� 2000

Sample


Input
3
100
3
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3

Output
Case #1: 2 3
Case #2: 1 4
Case #3: 4 5


@author: Alice
'''
from pprint import pprint
from datetime import datetime

def file_into_problem(file_name):
    with open(file_name, 'r+') as f:
        case_number = int(f.readline())
        problem = {'case_number':case_number}
        problem['cases'] = []
        for i in xrange(case_number):
            credit = int(f.readline())
            product_number = int(f.readline())
            product_cost = [int(i) for i in f.readline().split()]
            problem['cases'].append({'credit':credit, 'product_number':product_number, 'product_cost': product_cost})
    return problem


def solve_problem(problem):
    now = datetime.now().strftime("%m%d_%H%M%S")
    with open('result' + now + '.out', 'w+') as f:
        for case in problem['cases']:
            credit = case['credit']
            product_list = [item for item in case['product_list'] if item < credit].sort()
            product_number = len(product_list)
            possilbe_sets = []
            for i in xrange(product_number):
                temp_credit = credit
                a = [item for item in product_list if item > (credit / 2)]
                b = [item if  for item in product_list.remove if item < (credit / 2)]
                

if __name__ == '__main__':
    p = file_into_problem('a_test.in')
    solve_problem(p)
