from matplotlib import pyplot as plt


y_1 = [3, 4, 5, 3, 2, 3, 4]
y_2 = [5, 4, 2, 2, 6, 7, 8]
plt.plot(y_1, c='red')
plt.plot(y_2, c='black')
plt.scatter(list(range(len(y_1))), y_1, c='red')
plt.scatter(list(range(len(y_2))), y_2, c='black')

plt.fill_between(list(range(len(y_1))), y_1, y_2, facecolor='red', alpha=0.1)
plt.show()
