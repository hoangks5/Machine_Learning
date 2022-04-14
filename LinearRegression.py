import matplotlib.pyplot as plt
import pandas
import numpy

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