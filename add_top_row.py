# add top row for csv format files
# author: Frank Hu, Frank-the-Obscure @ GitHub

#import re

f = open('gd_train_data.txt', encoding='utf-8')

output = open('gd_train_data_100.csv', 'w', encoding='utf-8')

output.write('Use_city,Line_name,Terminal_id,Card_id,Create_city,Deal_time,Card_type\n')

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

for line in f:
    time = line[-15:-5] # magic numbers: slice for datetime
    #print(to_datetime(time))
    output.write(line[:-15]+to_datetime(time)+line[-5:])  

#print(to_datetime(str(2014111206)))