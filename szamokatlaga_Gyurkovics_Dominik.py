from random import randint
sz=[]
for x in range(10):
    sz.append(randint(0,100))
print(f'A számok átlaga: {sum(sz)/len(sz)}')

for i in range(len(sz)):
    if sz[i] % 3 == 0 and sz[i] % 4 != 0:
        print(sz[i], end=', ')