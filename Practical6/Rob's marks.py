import matplotlib.pyplot as plt
import numpy as np
a = input('please enter your mark:(use space between each marks)')
b = a.split(' ')                #devide each mark into list
marks = []                      #create a empty list
for i in range(len(b)):
    marks.append(int(b[i]))     #changethe str into int
marks.sort()                    #sort marks
print(marks)
plt.boxplot(marks) 
plt.title('the boxplot of whole marks')
plt.xlabel("your score")
plt.ylabel("marks")         
plt.show()
mean = np.mean(marks)           #calculate the mean value of the marks
print(mean)
print('pass') if mean > 60 else print('fail an exam ')  #print pass if mean>60  else print fail an exam