#use a list to record pieces by increasing cuts
p = [1,]
n = 0
while p[n] <= 64:               #if piece more than 64, then break the loop
    n += 1                      #n = n + 1
    p.append((n**2 + n + 2) / 2)# calculate (n^2+n+2)/2 and add it to the list
print('total number of pieces of pizza = ' + str(p[n]) + ' by ' + str(n) +' cuts') #print the the last item in the list