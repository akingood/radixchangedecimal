while True:
    opt = int(input("convert decimal to any radix (1)\nor from any radix to decimal (2)\n"))
    if opt == 1:
        n = int(input('enter number: '))
        r = int(input('enter radix to convert: '))
        x = []
        while n > 1:
            a = n % r
            x.append(a)
            n = n // r
        x.append(n)
        x.reverse()
        print(x)
    elif opt == 2:
        b = 0
        r = int(input('enter radix of the number: '))
        x = []
        print('enter number and q to exit: ')
        while True:
            x.append(input())
            if x[-1] == 'q':
                x.remove('q')
                break
        print(x)
        x.reverse()
        for i in range(len(x) -1, -1, -1):
            b += int(x[i]) * (r ** i)
        print(b)
    else:
        break