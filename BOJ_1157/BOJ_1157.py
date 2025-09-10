S = input().upper()
A = set(S)
z = 0
a = ""
for i in A:
  if S.count(i) > z:
    a = i
    z = S.count(i)
  elif S.count(i) == z:
    a = "?"
print(a)