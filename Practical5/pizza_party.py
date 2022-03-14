#use a list to record pieces by increasing cuts
p = [1,]
n = 0
while p[n] <= 64:
    n += 1
    p.append((n**2 + n + 2) / 2)
    print('total number of pieces of pizza = ' + str(p[n]) + ' by ' + str(n) +' cuts')