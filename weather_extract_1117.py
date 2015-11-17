# -*- coding: utf-8 -*-
# Author: 无名的弗兰克 @ ChemDog
# https://github.com/Frank-the-Obscure/
# weather extract, 20151117


import re

f = open('gd_weather_report.txt',encoding='utf-8')
fileout = open('gd_weather_report_1117.txt', 'w', encoding='utf-8')

t = re.compile(',')
slash = re.compile('/')

for line in f:
    columns = t.split(line)
   #print(columns)
    if(len(columns) > 1):
        output = []
        output.append(columns[0])
        for i in range(1,4):
            add = slash.split(columns[i])
            output += add

        fileout.write(','.join(output))

