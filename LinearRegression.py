import matplotlib.pyplot as plt
import pandas
import numpy as np

# Doc File CSV
data = pandas.read_csv('data_linear.csv').values


# Tong so diem 
N = data.shape[0]
# Du lieu cot 1
x = data[:,0]
# Du lieu cot 2
y = data[:,1]

print(x)
print(y)

# Doi thanh matran cot
x = x.reshape(-1,1)
y = y.reshape(-1,1)

print(x)
print(y)


# Ve do thi bieu dien gia tri
plt.scatter(x, y)
plt.title('Giá nhà theo mét vuông')
plt.xlabel('mét vuông')
plt.ylabel('giá')
#plt.show()

# Thêm cột giá trị = 1 vào matran
x = np.hstack((np.ones((N, 1)), x))

print(x)

# Khởi tạo matran W

w = np.array([[0],[1]])
print(w)

# Khoi tap gia tri du doan voi Yi = x*w
Yi = np.dot(x,w)
print(Yi)

print(Yi-y)