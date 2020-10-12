zima = [1,2,12]
vesna = [3,4,5]
leto = [6,7,8]
osen = [9,10,11]
a = int(input('vvedite nomer mesyatsa: '))
for i in zima:
    if i == a:
        print('zima')
for i in vesna:
    if i == a:
        print('vesna')
for i in leto:
    if i == a:
        print('leto')
for i in osen:
    if i == a:
        print('osen')

b = int(input('vvedite nomer mesyatsa: '))
my_dict = {1:'zima', 2: 'zima', 12: 'zima', 3: 'vesna', 4: 'vesna', 5: 'vesna', 6:'leto', 7:'leto', 8:'leto',
           9:'osen', 10:'osen', 11:'osen'}
print(my_dict.get(b))
