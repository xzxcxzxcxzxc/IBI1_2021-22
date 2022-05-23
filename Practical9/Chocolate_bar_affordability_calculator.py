
#function
def chocolate(totalMoney,price):
    bar = totalMoney // price
    rest = totalMoney % price
    return bar,rest


#example
totalMoney = 100
price = 7
bar,rest = chocolate(totalMoney, price)
print('%.0f' % bar, '%.2f' % rest)

totalMoney = float(input('input your money:'))
price = float(input('input your price'))
bar,rest = chocolate(totalMoney, price)
print('%.0f' % bar, '%.2f' % rest)