X,K,D = map(int, input().split())


if D * K < abs(X):
    #届かない場合
    print(abs(X) - D * K)
else:
    #届く場合、何回移動すると一番近くなるかを算出
    cnt = int(abs(X) / D) 
    distance = abs(X) % D
    if distance > (D/2):
        cnt = cnt + 1
        distance = abs(distance - D)
    #残り移動回数が奇数の場合は一個動く、偶数の場合は確定
    if (K - cnt) % 2 == 0:
        print(distance)
    else:
        print(abs(distance - D))