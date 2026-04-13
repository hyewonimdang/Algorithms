N = int(input())
A = set(map(int, input().split())) # set 중복 허용 X

M = int(input())
arr = list(map(int, input().split()))

for x in arr:
    if x in A:
        print(1)
    else: 
        print(0)