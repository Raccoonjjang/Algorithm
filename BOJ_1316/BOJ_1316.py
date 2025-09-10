T = int(input())
C = 0
for _ in range(T):
  S = list(input())
  m_list = []
  m_list.append(S[0])
  C = C + 1
  for i in range(1,len(S)):
    if S[i] == S[i-1]:
      m_list.append(S[i])
    elif S[i] != S[i-1]:
      if not S[i] in m_list:
        m_list.append(S[i])
      elif S[i] in m_list:
        C = C - 1
        break
print(C)