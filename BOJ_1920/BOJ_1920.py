# 입력받기
N = int(input())
A = list(map(int, input().split()))

M = int(input())
check_numbers = list(map(int, input().split()))

# 리스트 A를 집합으로 변환하여 탐색 시간 최적화
A_set = set(A)

# M개의 수에 대해 존재 여부를 확인하고 결과 출력
for number in check_numbers:
    if number in A_set:
        print(1)
    else:
        print(0)