import sys 

N = int(input())
n = sys.stdin.readline().strip() # \n 제거용
sum = 0

for i in n:
    sum += int(i);
   
print(sum)