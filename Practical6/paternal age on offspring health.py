import matplotlib.pyplot as plt
age = 30
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
pair={}
for i in range(len(chd)):
    pair[paternal_age[i]]=chd[i]
plt.scatter(pair.keys(),pair.values())
plt.show()
print(age,pair[age])