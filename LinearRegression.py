import matplotlib.pyplot as plt
import pandas
import numpy

# Doc File CSV
data = pandas.read_csv('data_linear.csv').values



N = data.shape[0]
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

print(N)
print(x)
print(y)