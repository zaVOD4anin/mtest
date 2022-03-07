open_f = open('readme.md')
abob = open_f.read()
open_f.close()

print(abob, end='')

try:
    with open('re34adme.md') as k:
        abob = k.read()
except:
    abob = 'Ty pidar'

print(abob)

with open('aboba.txt', 'a') as am:
    #am.write('How you do it7')
    print('\nEazy', file=am)