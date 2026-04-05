N = int(input())

stack = []

for i in range(N):
    stack.append(int(input()))

stack.sort()

print('\n'.join(map(str, stack)))