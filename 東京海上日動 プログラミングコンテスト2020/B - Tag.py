
A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

if (W >= V ):
    print('NO')
elif (A > B):
    length = A - B
    speed = V - W
    if(speed * T >= length):
        print('YES')
    else:
        print('NO')
else:
    length = B - A
    speed = V - W
    if(speed * T >= length):
        print('YES')
    else:
        print('NO')