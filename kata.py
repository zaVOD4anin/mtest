def main(num):
    exp = ''
    for z, a in enumerate(reversed(str(num))):
        if a != '0':
            exp += '0' * z + a + ' + '

    print(exp[-4::-1])



main(20505)
