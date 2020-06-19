X,Y = map(int,input().split())

if Y % 2 == 1:
    print('No')
else:
    if 4 * X >= Y:
        if 2 * X > Y:
            print('No')
        else:
            print('Yes')
    else:
        print('No')