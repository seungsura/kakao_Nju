import pandas as pd

data1 = pd.read_csv("data.csv", encoding= 'cp949')

#print(data1['id']=='934c812fbf79c3d675bae6d9df6721193286925c4c2afce3ee5d374f7cbaee9d85', data1['year'], data1['month'], data1['day'])

a = data1[data1['id'] == '934c812fbf79c3d675bae6d9df6721193286925c4c2afce3ee5d374f7cbaee9d85']
print(a)
len(a)
a = a.to_numeric()
#a.dtype
#if data1['id'] == '934c812fbf79c3d675bae6d9df6721193286925c4c2afce3ee5d374f7cbaee9d85':
 #   for i in range():
  #      name1 = data1['name']
  #      year1 = data1['year']
  #      month1 = data1['month']#
