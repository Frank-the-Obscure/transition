# -*- coding: utf-8 -*-
# author: Frank Hu, Frank-the-Obscure @ GitHub
# 读取数据
# add top row for csv format files

import re

f = open('predict_rf_1123.csv', encoding='utf-8')

output = open('gd_predict_1123.txt', 'w', encoding='utf-8')

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

    # col 1 1/1/15 to 20150101
    days = re.findall('\d+', columns[1])
    day = '20'+days[2]+'0'+days[0]+'0'+days[1]

    new_col_10.append(day)
    new_col_15.append(day)
    if int(columns[2]) < 10:
        new_col_10.append('0' + columns[2]) 
        new_col_15.append('0' + columns[2])  
    else:
        new_col_10.append(columns[2]) 
        new_col_15.append(columns[2])  
    new_col_10.append(columns[3])
    new_col_15.append(columns[4])    

    output.write(','.join(new_col_10) + '\n')
    output.write(','.join(new_col_15))


