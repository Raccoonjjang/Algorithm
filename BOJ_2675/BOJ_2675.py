S = int(input())
for _ in range(S):
  R, Z = input().split()
  R = int(R)
  E = "".join([char * R for char in Z])
  print(E)