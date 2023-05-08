'''
随机森林模型
'''

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# 引入数据
cwd = os.getcwd()
datasets_path = os.path.join(cwd, 'data_final_2.xlsx')
df = pd.read_excel(datasets_path)
# print(df.columns)
# print(df.index)  # [37833, 15]

Train, val_test = train_test_split(df, test_size=0.4, random_state=0, shuffle=True)  # 训练集占60%
val, test = train_test_split(df, test_size=0.5, random_state=0, shuffle=True)   # 验证集和测试集各占20%

# 训练集、验证集和测试集
X_Train = Train.iloc[:, :14].values
Y_Train = Train.iloc[:, 14].values

X_Val = val.iloc[:, :14].values
Y_Val = val.iloc[:, 14].values

X_Test = test.iloc[:, :14].values
Y_Test = test.iloc[:, 14].values

# 特征缩放
sc_X = StandardScaler()
X_Train = sc_X.fit_transform(X_Train)
X_Test = sc_X.transform(X_Test)

# Fitting the classifier into the Training set
model = RandomForestClassifier(n_estimators = 200, max_depth=8, criterion = 'entropy', random_state = 0)  # 决策树的深度为属性数量的一半
model.fit(X_Train, Y_Train)
# print(model.score(X_Train, Y_Train))

# Predicting the test set results
Y_Pred = model.predict(X_Test)

from sklearn.metrics import confusion_matrix
# print(Y_Test)
# print(Y_Pred)
cm = confusion_matrix(Y_Test, Y_Pred)

# 混淆矩阵
print('confusion matrix:')
print(cm)

# 计算测试集Rec, Pre, f1, Acc
# Rec=正确的正样本数/样本中的正样本数；Pre=正确的正样本数/预测为正例的样本数；f1=2*Rec*Pre/Rec+Pre。被攻击的为正样本，样本标签为1
A = 0  # 预测为正，实际为正的样本数
B = 0  # 预测为负，实际为正的样本数
C = 0  # 预测为正，实际为负的样本数
D = 0  # 预测为负，实际为负的样本数

for e in range(0,len(Y_Test)):
    if Y_Pred[e] != Y_Test[e]:
        if Y_Test[e] == 1:
            B = B + 1  # 预测为负，但实际为正
        else:
            C = C + 1  # 预测为正，但实际为负
    else:
        if Y_Test[e] == 1:
            A = A + 1  # 预测为正，实际为正
        else:
            D = D + 1  # 预测为负实际为负
Acc = (A + D)/(A + B + C + D)
Rec = A/(A + B)
Pre = A/(A + C)
f1 = 2*Rec*Pre/(Rec + Pre)
print('Accuracy: ', Acc)
print('Recall: ', Rec)
print('Precision: ', Pre)
print('F1: ', f1)

