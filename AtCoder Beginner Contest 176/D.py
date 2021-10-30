import collections
H,W,M = map(int, input().split())
hw = [map(int, input().split()) for _ in range(M)]
h, w = [list(i) for i in zip(*hw)]
nyuuryoku_set = set(zip(h, w))

ch = collections.Counter(h)
cw = collections.Counter(w)
ch_zyunn = ch.most_common()
cw_zyunn = cw.most_common()

ch_max = [i[0] for i in ch.items() if i[1] >= ch_zyunn[0][1]]
cw_max = [i[0] for i in cw.items() if i[1] >= cw_zyunn[0][1]]

test = [[0] * 2 for i in range((len(ch_max) * len(cw_max)))]
count = 0
for i in range(len(ch_max)):
    for j in range(len(cw_max)):
        test[count] = (ch_max[i],cw_max[j])
        count += 1
print(test)
print(nyuuryoku_set)
if not (set(test) in nyuuryoku_set):
    print(ch_zyunn[0][1] + cw_zyunn[0][1])
else:
    print(ch_zyunn[0][1] + cw_zyunn[0][1] - 1)

