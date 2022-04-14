import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([
        [1, 100, 7, 42, 0], [1, 150, 7, 62, 0], [1, 118, 6, 40, 0], [1, 123, 6, 54, 0], [1, 112, 6, 42, 0],
        [1, 99, 6, 56, 0], [1, 124, 7, 51, 1], [1, 150, 6, 32, 0], [1, 342, 10, 42, 1], [1, 300, 9, 14, 1],
        [1, 123, 6, 32, 0], [1, 155, 6, 30, 0], [1, 98, 5, 30, 0], [1, 112, 6, 32, 0], [1, 102, 5, 46, 1],
        [1, 150, 6, 32, 0], [1, 166, 8, 50, 0], [1, 149, 7, 22, 1], [1, 138, 6, 17, 0], [1, 150, 7, 23, 0]
      ])
# x1 = diện tích
x1 = data[:,1].reshape(-1,1)
# x2 = số phòng
x2 = data[:,2].reshape(-1,1)
# x3 = tuổi căn nhà
x3 = data[:,3].reshape(-1,1)
# x4 = số bếp lửa
x4 = data[:,4].reshape(-1,1)
# y là giá tiền nhà
y = np.array([259, 295, 279, 259, 299, 299, 309, 289, 849, 829, 359, 315, 310, 309, 300, 289, 369, 419, 405, 439]).reshape(-1,1)


w = np.array([[0],[1],[1],[1],[1]])
r = np.dot(data,w)-y
print(r)
# r = Yi - y
print(r)