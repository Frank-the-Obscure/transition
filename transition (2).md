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

dataframe.groupby('column_name').count() 可以很方便地进行统计

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

数据先清理掉不正常的五天(8.11-8.13, 8.15, 8.18), 再清理掉所有的法定假期和调休

9.8, 9.28, 10.1-7, 10.11

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

pandas 整理数据 提取矩阵

把所有数据整理到一个 csv 中, 用 pandas 整理和处理即可

i/o

- 使用 `read_csv` 读入; `to_csv`输出
- `DataFrame.as_matrix()` 导出为一个 numpy矩阵 -> 输入scikit-learn

```python
train_matrix = pd.read_csv('matrix_1117.csv') # 读入csv
train_matrix # pandas dataframe

matrix_line10 = train_matrix.as_matrix(columns=['hour','is_workday','line10']) # 选取某些列
matrix_line10 # numpy array

```

整理数据
- `astype()` 进行格式转换
- `pd.concat([df or series], axis)`  axis = 1 是按列合并 [pandas-merging](http://pandas.pydata.org/pandas-docs/stable/merging.html)

```
predict_matrix is a DataFrame
s10, s15是sklearn预测的列表 (numpy list)
s10 = pd.Series(y10_predict, name='y10').astype(int) 
s15 = pd.Series(y15_predict, name='y15').astype(int)
predicted = pd.concat([predict_matrix, s10, s15], axis=1)

```

ipynb 跑 sklearn 也比较靠谱 `1117.ipynb`

便于记录调试结果等, 命令行则没有记录.

输出为 np.txt, 后续应该整理为更好的格式, 输出回矩阵为好(已用pandas实现)

需要一个一键从预测矩阵生成最终 txt 的脚本(待进行)

还需要一个计算 & 可视化 precision 的脚本(待进行)

更长远则是 pipeline