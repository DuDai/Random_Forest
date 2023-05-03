'''
将数据集进行裁剪，方便操作
数据集以3000行为单位进行裁剪
'''
import pandas as pd


count = 0
f = 'normal_report.csv'
# 读取csv文件
try:
    df = pd.read_csv("./dataset/" + f, dtype=str, keep_default_na="", encoding='utf-8').head(0)  # 获取表头
except:
    df = pd.read_csv("./dataset/" + f, dtype=str, keep_default_na="", encoding='utf-8').head(0)  # 获取表头
# 拆分成每10行为一个小文件
for i, chunk in enumerate(pd.read_csv("./dataset/" + f, chunksize=3000, encoding="utf-8")):  # 注意编码格式
    # 添加表头
    # print(i,chunk)
    chunk = pd.concat([df.head(1), chunk])
    # 保存为新文件
    count+=1
    chunk.to_csv(f"./data_cut/{f}结果{str(count)}.csv", index=False)  # 保存

