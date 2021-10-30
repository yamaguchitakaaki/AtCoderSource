r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

# 移動ベクトルを考える 最大3手でいける
r3 = r2 - r1 
c3 = c2 - c1

x = abs(abs(c3) - abs(r3))

if (r3 == 0 and c3 == 0):
    print(0)
elif (r3 == c3 or r3 + c3 == 0 or abs(r3) + abs(c3) <= 3):
    print(1)
elif (x == 1 or x == 3 or x % 2 == 0):
    print(2)
else:
    print(3)