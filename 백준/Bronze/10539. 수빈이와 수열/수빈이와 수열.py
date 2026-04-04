# N 입력 받기
N = int(input())

B = []
A = [0] * N 
sum = 0
total = 0

# B 입력 받기
B = list(map(int, input().split()))

for i in range(N):
    A[i] = B[i] * (i+1) - total
    total += A[i]
    
    print(A[i], end= ' ')