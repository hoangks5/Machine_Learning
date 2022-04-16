import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

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





number = 100000

learning_rate = 0.000002
cost = np.zeros((number,1))
w = [[1],[1],[1],[1],[1]]
''' for i in range(number):
      r = np.dot(data,w)-y
      cost[i] = 0.5*np.sum(r*r)
      print(cost[i])
      w[0] = w[0] - learning_rate*np.sum(r)
      w[1] = w[1] - learning_rate*np.sum(np.multiply(r,data[:,1].reshape(-1,1)))
      w[2] = w[2] - learning_rate*np.sum(np.multiply(r,data[:,2].reshape(-1,1)))
      w[3] = w[3] - learning_rate*np.sum(np.multiply(r,data[:,3].reshape(-1,1)))
      w[4] = w[4] - learning_rate*np.sum(np.multiply(r,data[:,4].reshape(-1,1)))
      #print(np.array(w)) '''
      

w = [ 7.42113182,
  1.86950514,
 25.57630942,
 -2.27245749,
 22.0105757 ]

while True:
      xa = int(input('Diện tích: '))
      xb = int(input('Số phòng: '))
      xc = int(input('Tuổi: '))
      xd = int(input('Bếp: '))
      tien = w[0]+xa*w[1]+xb*w[2]+xc*w[3]+xd*w[4]
      print(tien) 