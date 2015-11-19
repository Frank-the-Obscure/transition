# -*- coding: utf-8 -*-
# author: Frank Hu, Frank-the-Obscure @ GitHub
# 读取数据
# add top row for csv format files

import re

f = open('predict_rf_all_1118.csv', encoding='utf-8')

output = open('gd_predict_1118.txt', 'w', encoding='utf-8')

t = re.compile(',')

for line in f:
    break

for line in f:
    new_col_10 = []
    new_col_15 = []

    columns = t.split(line)
    #print(columns)

    new_col_10.append('线路10') 
    new_col_15.append('线路15')
    new_col_10.append(columns[1])
    new_col_10.append(columns[2])    
    new_col_15.append(columns[1])
    new_col_15.append(columns[2])    
    new_col_10.append(columns[3])
    new_col_15.append(columns[4])    

    output.write(','.join(new_col_10) + '\n')
    output.write(','.join(new_col_15))


