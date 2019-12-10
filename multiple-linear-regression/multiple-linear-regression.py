import numpy as np
import csv
from sklearn import datasets,linear_model
def ReadCSVFile(filepath,encoding='utf-8'):
    data = []
    with open(filepath,'r',encoding=encoding,) as f:
        reader = csv.reader(f)
        for i in reader:
            data.append(i)
    print('has read {length} data.'.format(length=len(data)))
    return data

data = ReadCSVFile('traindata.csv')
mydata = []
for i in data[1:]:
    del(i[0])
    mydata.append(i)


x = np.array(mydata)
X = x[:,:-1]
Y = x[:,-1]
# 训练数据
regr = linear_model.LinearRegression()
regr.fit(X,Y)
xishu = regr.coef_
pianyi = regr.intercept_

test = mydata[:10]
result = []
for i in test:
    tmp = 0
    for j in range(4):
        tmp += float(i[j])*(xishu[j].item())
    result.append(tmp+(pianyi.item()))
print(result)