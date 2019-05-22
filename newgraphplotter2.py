import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('lsmplot.dat','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[1]))
        y.append(int(row[2]))
        z.append(int(row[3]))
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.zlabel('z')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
