def wrams(func):
    def dfg(*args):
        return func(args)

    return dfg


@wrams
def sume(a):
    print(f'{sume.__name__} is started')
    print(f'{sume.__name__} is stoped')
    return a


def gener(k):
    print('Piy')
    while True:
        print(k)
        print(sume(k))
        yield k


if __name__ == '__main__':
    print(sume(2))
    next(gener(12))