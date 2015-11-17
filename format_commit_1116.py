# author: Frank Hu, Frank-the-Obscure @ GitHub
# 读取数据
# add top row for csv format files

import re

f = open('commit_1117_0.txt', encoding='utf-8')

output = open('gd_predict_1117.txt', 'w', encoding='utf-8')

t = re.compile(',')

for line in f:
    columns = t.split(line)
    #print(columns)
    hour = int(columns[2])
    if hour < 10:
        columns[2] = '0' + columns[2]
    output.write(','.join(columns))