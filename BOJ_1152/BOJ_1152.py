T = input()
S = T.split(" ")
A = []
for i in range(len(S)):
  if S[i] != '':
    A.append(S[i])
print(len(A))