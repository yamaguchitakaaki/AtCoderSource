N = int(input())
C = [input() for i in range(N)]


ACcnt = C.count("AC")
WAcnt = C.count("WA")
TLEcnt = C.count("TLE")
REcnt = C.count("RE")

print('AC x ' + str(ACcnt))
print('WA x ' + str(WAcnt))
print('TLE x ' + str(TLEcnt))
print('RE x ' + str(REcnt))