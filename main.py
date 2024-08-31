while True:
    opt = int(input("convert decimal to any radix (1)\nor from any radix to decimal (2)\n"))
    if opt == 1:
        num = int(input("enter the number: "))
        rad = int(input("enter the radix: "))
        ans = ""
        while(num>=1):
            rem = num % rad
            ans = ans + str(rem)
            num = num // rad
        ans = ans[::-1]
        print(ans)
    elif opt == 2:
        rad = int(input("enter radix: "))
        num = input("enter number: ")
        s=0
        for i in range (len(num)-1,-1,-1):
            s=s+(int(num[i])*(rad(**(len(num)-1-i)))
        print(s)
    else:
        break
