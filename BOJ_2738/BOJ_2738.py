# 행렬 크기 N, M 입력
N, M = map(int, input().split())

# 빈 행렬 A와 B 생성
A = []
B = []

# 행렬 A 입력
for _ in range(N):
    A.append(list(map(int, input().split())))

# 행렬 B 입력
for _ in range(N):
    B.append(list(map(int, input().split())))

# 두 행렬의 합 계산 및 출력
for i in range(N):
    result_row = [A[i][j] + B[i][j] for j in range(M)]
    print(' '.join(map(str, result_row)))
