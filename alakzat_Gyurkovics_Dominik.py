sz=int(input('Add meg, hogy hány sorból álljon az alakzat: '))

for i in range(sz):
    print(f'{"_"*(sz+i-sz)}0{"_"*(sz-i-1)}', end='\n')