# 公交线路客流预测

outline

- 赛题
- 起始思路
- 数据统计与处理


## 赛题

>本次大赛要求选手根据广州市内及广佛同城公交线路的历史公交刷卡数据，挖掘固定人群在公共交通中的行为模式。建立公交线路乘车人次预测模型，并用模型预测未来一周（20150101-20150107）每日06时至21时每小时段各个线路的乘车人次。Part2将更换一批新数据。

>大赛开放20140801至20141231五个月广东部分公交线路岭南通用户刷卡数据，共涉及近200万用户2条线路约800多万条数据记录。同时大赛提供20140801至20150131期间广州市的天气状况信息。

预测线路乘车人次

## 起始思路

先对已有数据进行统计和可视化, 分析数据规律.

## 数据统计与处理

使用 Pandas 进行数据处理. `first-test.ipynb`

1. 数据没有标签行, 在已有 data 前面加上标签行.

train data:
8926604 rows × 7 columns

用前1000行写测试文件

2. 初步测试 Pandas groupby

ok

DataFrame.groupby('column_name').count() 可以很方便地进行统计

时间戳: 需要格式化

可以整理为文件存储, 或者转化成标准格式, 每次读取统计;

考虑使用次数, 如果需要反复调用并且数据量较大, 则应该预先处理(类似于准备一个完整的 feature 文件);

3. troubles

groupby等处理之后, 标签变成了第二行, 无法作为后续的行列标题.

尝试用时间序列调整每天的数据, 但是目前的数据 DataFrame 不是 Series, 似乎不可用.

4. 回归目标

目标: 两条线路的可视化

基本数据: 忽略用户层次信息, 只看统计结果

每天每小时两条线路的用户数量. 即下述表格:

- row: date time
- column: line 10/15
- data: count of people

未必一定要用 pandas. 处理完初步数据之后, 行数并不太多, excel等作图也可以考虑...

另外关于时间序列, 也可先用 python 处理成两列暂时统计着, 不必一直死磕. 有更多经验之后会处理得更好.


## First commit

1. 已有数据按照两条路线每天每小时归类
2. 可视化看趋势
3. 预测 CV 集
4. CV
5. 预测测试集并提交

### 1. 归类

基本正常, 有1000多 count 的时间标签格式不对, 暂时不管了(一共 900w)
转到 excel 里面做 pivottable

### 2. 可视化

`plot_1119.xlsx-plot_by_hour`: 按小时的plot

明显表现出早晚高峰的特征, 初步看来方差并不大.
可用平均值预测一次.

### 3. 预测 CV

### 4. CV 质控

### 5. 预测测试集

直接调整 excel 文件

0101用周日的数据

0102,0103用周六的数据

4,5,6,7用周一二三四的数据

只需要预测6-21的数据, 其它删去.


## 20151116 second commit

- 读取清理数据
- 拍脑门设计第二次提交

### 读取并清洗数据

初步看整体趋势:

随周末变化明显; 假期效果明显(9.6-8中秋; 10.1-7国庆: 9.28 10.11上班)

8.11-8.13, 8.15, 8.18数据明显异常

### 拍脑门设计第二次提交

从整体趋势看: 新年三天按 周六 周日 周日 预测可能比较科学
后面四天按 周一 周二 周三 周四 预测

数据先清理掉不正常的五天, 再清理掉所有的法定假期和调休

9.8

9.28

10.1-7

10.11

files:

整理的数据 `gd_train_data_1116.csv`

- 包括如下 features: `Use_city,Line_name,Terminal_id,Card_id,Create_city,Deal_time,Date,Hour,Weekday,Card_type`

归类后的数据 `count_1116.csv`

下面进入 excel 整理

`first_pivot`: 整理为 line 10/15 和横轴
 
`clean_up`: 清除掉上述异常值, 法定假日04和调休 

(inbox: 月份变化)

## 20151117 first model

### 整理 model 数据

cleaned data(去除特殊日期后) 6-21

X hour, is_workday
y line10 count

整理为 `matrix_1117.csv`

用 pandas 整理为 numpy array, 准备用

pandas 整理数据 提取矩阵好用

ipynb 跑 sklearn 也比较靠谱 `1117.ipynb`

输出为 np.txt, 后续应该整理为更好的格式, 输出回矩阵为好

需要一个一键生成最终 txt 的脚本

更长远则是 pipeline

```
line10 rf train 0.946813459599
line10 rf cv 0.949336870506
line15 rf train 0.927900606389
line15 rf cv 0.927390457474

```

precision: `1118`


## 20151118 second model `1118-2.ipynb`

weekday 转换为周一-周日的数据

- crosstab 整合信息
- 整理为 0/1 特征
- model/可视化
- CV
- predict

### crosstab 整合信息 by pandas

`train_1118.csv`: 基本信息

`weather_1118.csv`: 天气信息

用 `date` join 两个列表: `join_1118.csv`

`feature_01_1118.py`: 整理为01变量, `features_1118.csv`

0.992296797628
0.946711671255
0.990874187631
0.941209986176

### predict

数据未整理...迅速整理为相同格式的输入

写了简单的输出格式化脚本 `format_predict_1118.py`, 需要进一步整合成更大的 workflow

### todo 

hour 是否要转成 0/1 

1/1 可能要按周日预测, 而非周六(看一下十一的情况)

btw: 

1. log 保持跟踪很重要
2. 夜了...搞到一点实在累. 尽量避免

## 20151119 plot and CV `1119.ipynb`

Outline:

- 作图, 发现问题


### plot in matplotlib

`%matplotlib inline` in first cell

1118: precision 

line10 0.7735

line15 0.7331


测试 models

linear model 明显表现不行, SVM 表现也不行.

猜测是 hour 的问题, 转换为一系列 0/1 features

RF 无明显变化

linear model 与 SVM 表现有所提高, 但与 RF 仍有明显差距.

### final predict

50 features 预测

1.1-1.3 全部按周日预测

注: 最后 csv -> txt 需要改一下日期格式, 回头整合.


inbox: 也许可加一个异常天气变量(如 temp-ave_temp)表征异常天气

## 20151120 what's wrong?

- 昨夜提交的结果很差(56.81%), 先确定问题所在
- 确定之后, 再继续尝试提高在预测集上的表现; 
  - 也许应该固定预测集为某些日期 (如十二月最后几天)

### 确定问题

先排除明显的预测失误, 或者文件写错等问题

也就是说有1/4的数据格式不对...留待明天再测试正确的值吧

写代码, 可视化两个预测文件(final txt file), 便于对比

猜测是过拟合?

! **发现了明显的预测失误...所有的 6-9 没有写成 06-09**

大约会差 1/3 的预测值: 如果这么理想的话, 大约能提高到 75% (等待新的预测值)

不过, 与 1118 的预测相当相当接近(只在 1.1 是周六还是周日上有明显区别, 其余都是细微差别), 但 1118 只有 71.99%. 因此也并不乐观.

写可视化脚本, 从输出文件可视化 `compare_predict_1120.py`

matplotlib: 

用 x,y list 作图

可视化后发现一个明显的疑点: `predict_1118_1119.png`

最新的预测 1.1-1.3 的晚高峰都比早高峰还高?

查看已有数据, 似乎并没有这样的趋势

怀疑是过拟合导致的? 如何验证? 用训练数据(CV集可视化)

### 下一步

拍脑门不是很好的思路, 需要系统整理算法和结果. 通过 CV 寻找继续优化的方法.

需要进行的操作: 

1. 整理出部分数据集(固定划分一组 train/CV set)
2. workflow 来可视化对应的结果

行动:

1. `1120.ipynb`: 分隔数据集, 用 12.25-12.31 作为测试集
2. 初步可视化: 在这几天之中, 似乎周六的表现最差
  - 有必要具体挑出误差最大的一些点, 来进行后续分析

拍脑门预测大法:

手动调整如下曲线: 参照 12月末, 调整 1.1-1.3 早晚高峰(下调), 1.4 早高峰(下调)

## 1121: 调参与新的预测

1120结果: 74.63%; 拍脑门之后是 74.62%

74.63% 是目前最好的结果 :)

不过排名 19 位, 还需要继续努力啊 :)

### 下面的思考: 调整模型还是调整特征?

- 模型方面: 
  - RF 容易过拟合, 似乎并不是这个题目(样本量并不大)的最佳算法
  - train/cv过后, 最好再用同样参数跑一次完整训练集
  - 训练误差的定义, 是否需要考虑一下归一化的问题?
- 特征方面: 需要尝试
  - 思考的问题: 哪些情况可能会影响人们坐公交车出行?
  - 下雨可能是一个特征: 把目前的一大串天气参数简化为 2-3 个特征再看其方差?
    - 简化的可能作用: 因天气信息很稀疏, 合并可增加样本量, 防止过拟合
  - 异常天气(特别高温, 低温) 可用当天天气与邻近几天天气作差的绝对值来表征
  - 未利用的信息: 
    - 卡类型: 需要先做统计
    - uid: 

### 提交版本

1121.ipynb

GBRT 预测: 防止 RF 过拟合

调参: 在 12月最后一周的 precision: 0.7407 / 0.7219

提交用完整训练集预测的结果(相同模型, 但用全部数据)


## 1122:

需要先看看训练集的拟合误差是多少, 只看 R^2 不够.

太夜了, 改改 RF 提交一版吧.

calculation of columns in pandas

[link](http://stackoverflow.com/questions/12376863/adding-calculated-columns-to-a-dataframe-in-pandas)


## 1123:

1122结果还不如前几天...似乎倒是有些奇怪

合并天气:

day: 0.7485, 0.7128

day & night: 0.7520, 0.7182

想法似乎可行, 得到目前最好的测试集表现

Next: 整理不同用户卡类型, 分开几个模型(简单模型)再做预测

## 1124

1123结果也略差于最优值.

进行卡分类预测:

1. 可视化
2. 分数据集到几个 y, join 成为完整数据集
3. 分开预测几部分的 y
4. 加和 CV/预测

可视化:

1. 老人卡的表现和普通卡明显不同:
  - 周末早高峰不变
  - 无晚高峰
2. 普通卡占大部分, 老人卡和学生卡占较小部分, 其余卡加一起占更小部分

RF predict type

```
normal
0.993263496326
0.953579947464
0.992488415843
0.948221158748
old
0.99138055293
0.944289100172
0.988783034231
0.922316514118
student
0.969928796501
0.846463008305
0.96264429538
0.800492588234
police
0.834648893918
-0.012024059452
0.811800596985
-0.592655356584
disabled
0.930740251633
0.589455507083
0.89440492528
0.368967252547
crew
0.928662635615
0.556015857068
0.900310076116
0.252132134549
```

## 1125

1124 separated file: RF 表现与之前最佳值相当.

before add new features: GBRT

```
normal
0.981288947395
0.964491279057
0.976407811871
0.95502075003
old
0.976097456812
0.957631340588
0.967049487063
0.930488736037
student
0.925585098226
0.868378180176
0.901300696587
0.821672424332
police
0.421784628709
-0.0532401835954
0.526830402909
-0.622867814165
disabled
0.795346233879
0.630695109934
0.674757944817
0.396824348102
crew
0.749686944917
0.581272175067
0.651058738563
0.278522282323
```

after add new features GBRT

```
normal
0.792526409061
0.743877252628
old
0.684513758636
0.593670558929
student
0.465016246673
0.447581956045
police
0.0302968316151
0.0
disabled
0.373235344839
0.256554081804
crew
0.376439892761
0.282215987168
```


最终考虑:

比较按卡分类分开预测的模型和全模型

- 分开预测: GBRT; `1125.ipynb`

在本地测试中 GBRT 表现略好于 RF

- 全模型: RF `1125-all.ipynb`

注意:

新数据按天的可视化和挖掘一定在一上来就处理!


## 1126

new data mean predict

cleanup: 去掉异常值和假日

另外: 是否试试神经网络?

因为时间突然有限, 这是最后一次预测了. 结果是 72.74%.