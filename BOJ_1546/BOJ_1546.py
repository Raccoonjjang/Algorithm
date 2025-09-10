N = int(input())
M = list(map(int, input().split()))
M.sort()
avr = 0
for i in range(N):
  sum = M[i]/M[N-1]*100
  avr = avr + sum
avr = avr/(N)
print(avr)