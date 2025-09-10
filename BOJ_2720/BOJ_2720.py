T = int(input())
for i in range(T):
    a =b=c=d=f=0
    b = int(input())
    if b >= 25:
        a = b // 25
        b = b % 25
    if b >= 10:
        c = b // 10
        b = b % 10
    if b >= 5:
        d = b // 5
        b = b % 5
    if b >= 1:
        f = b // 1
    print(a,c,d,f)