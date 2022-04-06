2022/4/3
#江苏大学
#董佳斌
#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import Ridge,RidgeCV
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import lightgbm as lgb
from sklearn.preprocessing import StandardScaler
import streamlit as st

d=[]
x=[]
y=[]
#读取数据
alldata_15G=np.loadtxt("F:\\3x3\\3x3xin\\python\\hebing.dat")
for i in range (len(alldata_15G)):
    q = alldata_15G[i, 0:49]
    e = alldata_15G[i, 49:50]
    q = q.tolist()
    e = e.tolist()
    x.append(q)
    y.append(e)
# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
plt.style.use('ggplot')
#x标准化
scale = StandardScaler()
#x = scale.fit_transform(x)
# 将数据集拆分为训练集和测试集  比例为8:2

X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=12345)

LGBR = lgb.LGBMRegressor(objective='regression', boosting_type='goss',
                             max_depth=4,
                             learning_rate=0.007, n_estimators=2100,
                             bagging_fraction=0.8, feature_fraction=0.8)  # 导入模型，模型参数默认 返回一个线性回归模型
LGBR.fit(X_train, y_train)  # 一元线性回归进行模型训练
y_pred = LGBR.predict(X_test)  # 预测模型,此时输出类别数据
r = r2_score(y_test, y_pred)
print("Mean squared error: %.5f" % mean_squared_error(y_test, y_pred))  # 打印均方误差值 两位小数float
print("RMSE: %lf" % np.sqrt(np.sum(np.square(y_test - y_pred)) / len(y_test)))  # 打印RMSE值
print('r2_score: %.5f' % r2_score(y_test, y_pred))  # r2值
# 设置图形大小
plt.figure(figsize=(8, 4), dpi=80)
plt.plot(range(len(y_test)), y_test, ls='-.',lw=2,c='r',label='真实值')
plt.plot(range(len(y_pred)), y_pred, ls='-',lw=2,c='b',label='预测值')

# 绘制网格
plt.grid(alpha=0.4, linestyle=':')
plt.legend()
plt.xlabel('number') #设置x轴的标签文本
plt.ylabel('泊松比') #设置y轴的标签文本
# 展示
plt.show()
st.pyplot()

ysorted= sorted(y_test)    #按行对给定的数组的元素进行排序
xx = np.linspace(ysorted[0], ysorted[-1], len(ysorted))  #创建等差数列。开始，结束，生成的样本数据量。
plt.plot(xx, xx, 'r')
plt.plot(y_test,y_pred,'ch', alpha=0.5)
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.title('MLPRegressor Regression')
plt.show()
st.pyplot()
#y_test = np.reshape(y_test,(187,1))
#y_pred = np.reshape(y_pred,(187,1))
#print(y_test,y_pred)
