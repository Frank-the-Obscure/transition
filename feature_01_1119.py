# author: Frank Hu, Frank-the-Obscure @ GitHub
# 读取数据
# add top row for csv format files

import re

f = open('train_join_1119.csv', encoding='utf-8')

output = open('train_features_1119.csv', 'w', encoding='utf-8')

t = re.compile(',')

output.write('top col,time,hour,weekday_x,is_workday,\
line10,line15,date,weather_day,weather_night,\
temp_day,temp_night,wind_day,wind_night,\
is_monday,is_tuesday,is_wednesday,is_thursday,\
is_friday,is_saturday,is_Sunday,\
day_sunny,day_cloudy,day_yin,day_mai,day_zhenyu,\
day_leizhenyu,day_xiaoyu,day_xiaodaozhongyu,day_zhongyu,\
day_zhongdaodayu,day_dayu,day_dadaobaoyu,\
night_sunny,night_cloudy,night_yin,night_mai,night_zhenyu,\
night_leizhenyu,night_xiaoyu,night_xiaodaozhongyu,night_zhongyu,\
night_zhongdaodayu,night_dayu,night_dadaobaoyu,\
6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21\n')

def set_hour(hour):
    s = [0] * 16
    s[int(hour) - 6] = 1
    return s

def weekday(day):
    # input is a char day 0-6
    # output: a list of is_monday to is_Sunday
    s = [0,0,0,0,0,0,0]
    s[int(day)] = 1
    return s

def weather(weather):
    s = [0] * 12
    d = {'晴':0,'多云':1,'阴':2,'霾':3,'阵雨':4,'雷阵雨':5,'小雨':6,
         '小到中雨':7,'中雨':8,'中到大雨':9,'大雨':10,'大到暴雨':11}
    s[d[weather]] = 1
    return s

for line in f:
    break

for line in f:
    new_col = []

    columns = t.split(line)
    #print(columns)

    new_col += columns[:-3]

    new_col += weekday(columns[3]) # weekday 0-6

    new_col += weather(columns[8])

    new_col += weather(columns[9])

    new_col += set_hour(columns[2])

    for i in range(0,len(new_col)):
        output.write(str(new_col[i]))
        if i < len(new_col) - 1:
            output.write(',')
        else:
            output.write('\n')

f = open('predict_join_1119.csv', encoding='utf-8')

output = open('predict_features_1119.csv', 'w', encoding='utf-8')


output.write('top col,hour,weekday_x,is_workday,\
date,weather_day,weather_night,\
temp_day,temp_night,wind_day,wind_night,\
is_monday,is_tuesday,is_wednesday,is_thursday,\
is_friday,is_saturday,is_Sunday,\
day_sunny,day_cloudy,day_yin,day_mai,day_zhenyu,\
day_leizhenyu,day_xiaoyu,day_xiaodaozhongyu,day_zhongyu,\
day_zhongdaodayu,day_dayu,day_dadaobaoyu,\
night_sunny,night_cloudy,night_yin,night_mai,night_zhenyu,\
night_leizhenyu,night_xiaoyu,night_xiaodaozhongyu,night_zhongyu,\
night_zhongdaodayu,night_dayu,night_dadaobaoyu,\
6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21\n')


for line in f:
    break

for line in f:
    new_col = []

    columns = t.split(line)
    #print(columns)

    new_col += columns[:-3]

    new_col += weekday(columns[2]) # weekday 0-6

    new_col += weather(columns[5])

    new_col += weather(columns[6])

    new_col += set_hour(columns[1])

    for i in range(0,len(new_col)):
        output.write(str(new_col[i]))
        if i < len(new_col) - 1:
            output.write(',')
        else:
            output.write('\n')