import math
N = int(input())
N_range = int(math.sqrt(N)) + 1
list = []

for i in range(1,N_range):
    if N % i == 0:
        print(i)
        if (i**2 != N):
            list.append(int(N /i))

for name in reversed(list):
    print(name)
