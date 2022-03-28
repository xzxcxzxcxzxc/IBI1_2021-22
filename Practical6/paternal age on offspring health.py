import matplotlib.pyplot as plt
paternal_age=[30,35,40,45,50,55,60,65,70,75]            #initialize
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
pair={}                                                 # create a new dictionary
for i in range(len(chd)):
    pair[paternal_age[i]]=chd[i]                        #put hte parternal_age and chd into pairs
plt.scatter(pair.keys(),pair.values(),c='g')
plt.title('The correspondence ')
plt.xlabel('paternal_age')
plt.ylabel('chd')
plt.show()                                              #show the plot    
age = input('please ener the age you want to search:')  #input the age
print(age,pair[int(age)])                