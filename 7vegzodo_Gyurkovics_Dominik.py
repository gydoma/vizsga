i = int(input('Adj meg egy pozitív egész számot: '))
sz = 0
for x in range(i):
    print(x, end=' ')
    if x % 10 == 7:sz+=1
print(f'\n7-re végződőek száma: {sz}')
