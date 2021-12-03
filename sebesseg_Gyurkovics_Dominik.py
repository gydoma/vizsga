from random import randint

korlat=int(input('Add meg a legnagyobb megengedett sebességet: '))
seb=randint(60, 130)
print(f'Sebességed: {seb}')
if korlat+40 <= seb:print('Túllépted több mint negyvennel a megengedett legnagyobb sebességet! 50,000 Forint Bírság!')
elif korlat+20 <= seb:print('Túllépted több mint hússzal a megengedett legnagyobb sebességet! 30,000 Forint Bírság!')
elif korlat < seb:print('Nem kell büntetést fizetned!')