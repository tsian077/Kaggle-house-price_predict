import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


x_train = pd.read_csv('train.csv')
print(x_train)


#畫出x_train的關係矩陣
corrmat = x_train.corr()
#figsize(長，寬)
f ,ax = plt.subplots(figsize=(20,9))
sns.heatmap(corrmat,vmax=0.8,square=True,cmap='Blues')
#plt.show()


#OverallQual 總評價
#YearBuilt 建造年分
#YearRemodAdd 重裝潢的日期
#TotalBsmtSF 地下室面積
#1stFlrSF 一樓面積
#GrLiveArea 生活區面積
#FullBath 是否有浴室
#TotRmsAdbGrd 房間總數
#GarageCars 車庫可容納車數
#GarageArea 車庫面積

cols = ['Id','OverallQual','YearBuilt','YearRemodAdd','TotalBsmtSF','1stFlrSF','GrLivArea','FullBath','TotRmsAbvGrd','GarageCars','GarageArea']
x_train=x_train[cols]

#重裝潢日-建築的日子
x_train['YearRemodAdd-YearBuilt']=x_train['YearRemodAdd']-x_train['YearBuilt']

#建了多久=現在的年份-建造的年份
x_train['Now-YeatBulit']=(2018-x_train['YearBuilt'])//10
print(x_train)
