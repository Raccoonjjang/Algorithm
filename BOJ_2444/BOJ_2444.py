S = int(input())
T = 2*S-1
for i in range(1,S+1):
  space = ' ' * (S-i)
  star = '*' * (2*i-1)
  print(space + star)
for i in range(S-1,0,-1):
  space = ' ' * (S-i)
  star = '*' * (2*i-1)
  print(space + star)