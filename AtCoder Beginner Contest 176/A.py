N,X,T = map(int, input().split())

result = int(N / X) 
amari = N % X
if amari == 0:
    print(result * T)
else:
    print((result+1) * T)