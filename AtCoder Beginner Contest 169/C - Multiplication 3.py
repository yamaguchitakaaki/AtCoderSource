from decimal import Decimal
import math

A, B = input().split()
A = Decimal(A)
B = Decimal(B)

print(math.floor(A * B))