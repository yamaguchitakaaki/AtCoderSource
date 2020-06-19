import collections
# Nの入力
N = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

c = collections.Counter(prime_factorize(N))
result = 0
for i in list(c.values()):
    j = 1
    if i == 1:
        result += 1
    else:
        while i >= j:
            i = i - j
            result += 1
            j += 1
print(result)