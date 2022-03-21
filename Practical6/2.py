import matplotlib.pyplot as plt
import numpy as np
marks = [45,36,86,57,53,92,65,45]
marks.sort()
print(marks)
plt.boxplot(marks)
plt.show()
mean = np.mean(marks)
print(mean)
print('pass') if mean > 60 else print('fail an exam ')