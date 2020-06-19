import math

# A B H Mの入力
A, B, H, M = map(int, input().split())

# 規定時間時の短針の先端ベクトル
Ax = A * math.cos(math.radians(H * 30 + 0.5 * M))
Ay = A * math.sin(math.radians(H * 30 + 0.5 * M))

# 規定時間時の長針の先端ベクトル
Bx = B * math.cos(math.radians(6 * M))
By = B * math.sin(math.radians(6 * M))

print(math.sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2))