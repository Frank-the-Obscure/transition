# -*- coding: utf-8 -*-
# author: Frank Hu, Frank-the-Obscure @ GitHub
# 对比两个预测文件, 并可视化
# i: two file
# o: compare/visualize line

from sys import argv
import matplotlib.pyplot as plt

script, file1, file2 = argv

def file_to_list(filename):
    """

    i: csv format: line, date, hour, y
    o: list of x, date-y10, date-y15
    """

    file_input = open(filename, encoding='utf-8')

    import re
    t = re.compile(',')

    date_y10 = []
    date_y15 = []

    for line in file_input:
        columns = t.split(line)

        date = columns[1] + columns[2]
        if columns[0] == '线路10':
            date_y10.append((date, int(columns[3])))
        else:
            date_y15.append((date, int(columns[3])))

    date_y10.sort(key=lambda x:x[0])
    date_y15.sort(key=lambda x:x[0])

    # transfer to x,y list
    x = []
    y10 = []
    y15 = []
    for i in range(0,len(date_y10)):
        x.append(i)
        y10.append(date_y10[i][1])
        y15.append(date_y15[i][1])

    return x, y10, y15


def plot(file1, file2):

    x, y10_1, y15_1 = file_to_list(file1)
    x, y10_2, y15_2 = file_to_list(file2)

    plt.plot(x,y10_1,color='b')
    plt.plot(x,y15_1,color='b')
    plt.plot(x,y10_2,color='r')
    plt.plot(x,y15_2,color='r')

    plt.show()


plot(file1, file2)
