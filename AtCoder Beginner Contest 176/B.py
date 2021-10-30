N = int(input())
sum = 0
N_string = str(N)
for i in range(len(N_string)):
    sum += int(N_string[i])
if sum % 9 == 0:
    print('Yes')
else:
    print('No')