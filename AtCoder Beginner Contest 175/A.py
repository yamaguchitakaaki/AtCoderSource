S= input()

if S.count('RRR') == 1:
    print(3)
elif S.count('RR') == 1:
    print(2)
elif S.count('RSR') == 1 or S.count('RSS') == 1 or S.count('SRS') == 1 or S.count('SSR') == 1:
    print(1)
else:
    print(0)
