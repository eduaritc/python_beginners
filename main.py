# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from numpy import genfromtxt
import csv

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    emp_id = np.arange(1, 11)
    rand_numb = np.random.randint(100, 200, 10)
    print(emp_id)
    print(rand_numb)
    index_gt_five = np.where(emp_id > 5)
    print(index_gt_five)
    print(emp_id[index_gt_five])
    ids = genfromtxt('C:/Users/eduar/Desktop/input.csv', delimiter=',')
    print(ids)
    with open('C:/Users/eduar/Desktop/input.csv') as f:
        id2 = list(csv.reader(f, delimiter=','))
    id3 = np.array(id2[0:][0])
    print('id2: \n {}'.format(id2))
    print('id3: \n {}'.format(id3))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
