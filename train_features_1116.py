# author: Frank Hu, Frank-the-Obscure @ GitHub
# 读取数据
# add top row for csv format files

import re
import pandas as pd

f = open('gd_train_data.txt', encoding='utf-8')

output = open('gd_train_data_1116.csv', 'w', encoding='utf-8')

output.write('Use_city,Line_name,Terminal_id,Card_id,Create_city,Deal_time,Date,Hour,Weekday,Card_type\n')

def to_datetime(time):
    return '{}-{}-{} {}:00:00'.format(time[:4],time[4:6],time[6:8],time[8:])

'''
for i in range(100): # test for range
    s = f.readline()
    time = s[-15:-5] # magic numbers: slice for datetime
    #print(to_datetime(time))
    output.write(s[:-15]+to_datetime(time)+s[-5:])
'''

# extract whole file

split = re.compile(',')

for line in f:
    columns = split.split(line)
    #print(columns)
    time = columns[5]
    columns[5] = to_datetime(time)
    columns.insert(-1, time[4:8]) # add date
    columns.insert(-1, time[8:]) # add hour
    columns.insert(-1, str(pd.Timestamp(columns[5]).weekday())) # add weekday 0(Mon)-6(Sun)

    #print(columns)

    #print(to_datetime(time))
    output.write(','.join(columns))  
    #break
#print(to_datetime(str(2014111206)))