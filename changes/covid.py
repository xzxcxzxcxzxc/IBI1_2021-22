import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data.csv")
location = covid_data.loc[:, 'location']
print(covid_data.iloc[10:21, [0, 3]])
rowNumAf = []
rowNum = []
rowNumWorld = []
totalDeathNum = []
totalNewCases = []
for i in location:
    if i == 'Afghanistan':
        rowNumAf.append(True)
    else:
        rowNumAf.append(False)
print(covid_data.iloc[rowNumAf, :])
for i in location:
    if i == 'China':
        rowNum.append(True)
    else:
        rowNum.append(False)
for i in location:
    if i == 'World':
        rowNumWorld.append(True)
    else:
        rowNumWorld.append(False)
totalDeathNum = covid_data.loc[rowNumWorld, 'new_deaths']
totalNewCases = covid_data.loc[rowNumWorld, 'new_cases']
print(totalDeathNum)
print(totalNewCases)
date = covid_data.loc[rowNum, 'date']
China_news = covid_data.loc[rowNum, 'new_cases']
China_deaths = covid_data.loc[rowNum, 'new_deaths']
print(len(date), len(China_deaths), len(China_news))
print(np.mean(China_deaths))
print(np.mean(China_news))
plt.figure(figsize=(15, 8), dpi=100)
plt.suptitle('The plot of COVID-19')
plt.subplot(232)
plt.plot(date, China_deaths, 'r', label='new_death')
plt.xticks(date.iloc[0:len(date):4], rotation=-90)
plt.ylabel('number of people')
plt.title('new deaths in China')
plt.legend()
plt.subplot(233)
plt.plot(date, China_news, 'b', label='news_cases')
plt.xticks(date.iloc[0:len(date):4], rotation=-90)
plt.ylabel('number of people')
plt.title('new cases in China')
plt.legend()
plt.subplot(231)
plt.boxplot(China_news, showfliers=False)
plt.title('The boxplot of news cases in China')
plt.ylabel('number of people')
plt.subplot(234)
plt.boxplot(China_deaths, showfliers=False)
plt.title('The boxplot of deathes in China')
plt.ylabel('number of people')
plt.subplot(235)
plt.title('New deaths in World')
plt.plot(date, totalDeathNum, 'r', label='DeathNum')
plt.xticks(date.iloc[0:len(date):4], rotation=-90)
plt.ylabel('number of people')
plt.legend()
plt.subplot(236)
plt.title('New cases in World')
plt.plot(date, totalNewCases, 'b', label='NewCases')
plt.xticks(date.iloc[0:len(date):4], rotation=-90)
plt.ylabel('number of people')
plt.legend()
plt.tight_layout()
plt.show()
