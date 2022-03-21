a = 19245301        #7 March, 2022  cases of COVID-19
b = 4218520         #2021   cases of COVID-19
c = 271             #2020   cases of COVID-19
d = abs(b - c)      #difference between 2020 and 2021
e = abs(a - b)      #difference between 2022 and 2021
if d > e:           #compare d and e
    print('d > e')  #if d > e then print 'd > e '
else:
    print('d < e')  #elseif d<= e then print 'd < e"
print(d/c)          #rate of new cases in 2020
print(e/b)          #rate of new cases in 2021
if d/c > e/b:       # compare the rate in 2020 and 2021
    print('rate in 2020 is much bigger than 2021')
else:
    print('rate in 2021 is much bigger than 2020')
X = 'a5fc'
Y = 'abc'
W = X and Y
print(W)
W = Y and X
print(W)