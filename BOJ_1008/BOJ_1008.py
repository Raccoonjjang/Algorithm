import sys

def count_intersections(x1, y1, r1, x2, y2, r2):
    # 제곱 거리로 비교하여 부동소수 오차 회피
    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy           # 중심 거리의 제곱
    rsum = r1 + r2
    rdiff = abs(r1 - r2)
    rsum2 = rsum*rsum
    rdiff2 = rdiff*rdiff

    # 같은 중심
    if d2 == 0:
        if r1 == r2:
            return -1            # 무한히 많음 (동일한 원)
        else:
            return 0             # 동심, 반지름 다름 -> 교점 없음

    # 떨어진 두 중심
    if d2 > rsum2:
        return 0                 # 멀어서 안 만남
    if d2 < rdiff2:
        return 0                 # 한 원이 다른 원 내부에 완전히 포함
    if d2 == rsum2 or d2 == rdiff2:
        return 1                 # 외접 또는 내접
    return 2                     # 그 외는 두 점에서 만남

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out_lines = []
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        out_lines.append(str(count_intersections(x1, y1, r1, x2, y2, r2)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()