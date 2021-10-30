X,Y,A,B = map(int, input().split())

## 次の瞬間の最低値を考える
cnt = 0
flg = True
XA = X * A
XB = X + B

if(XA >= Y and XB >= Y):
    print(cnt)
else:
    while(X<Y):
        XA = X * A
        XB = X + B
        if (XA >= XB):
            ##Bを選択
            flg = False
            break
        else:
            ##Aを選択
            X = XA
            cnt += 1
            
    if(flg):
        print(cnt-1)
    else:
        if (Y-X) % B == 0:
            Bcnt = int((Y-X)/B) - 1 
        else:
            Bcnt = int((Y-X)/B)
        print(Bcnt + cnt)
