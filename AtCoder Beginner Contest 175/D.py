N,K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

if K > 5000:
    K = 5000

#Pをバブルソートすると同時にCも対応して並び替える
change = True
while change:
    change = False
    for i in range(len(P) - 1):
        if P[i] > P[i + 1]:
            P[i], P[i + 1] = P[i + 1], P[i]
            C[i], C[i + 1] = C[i + 1], C[i]
            change = True

print(P)
print(C)

#Cの累積和を求める
for i in range(len(C)):
    ruiseki[i+1] = ruiseki[i] + C[i] 
for i in K:
    for j in :
        ruiseki[]

# K以下の個数範囲でCの部分配列の最大値を検索する



