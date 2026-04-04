arr = list(map(int, input().split()))

# 3개 다 동일
if len(set(arr)) == 1:
    result = 10000 + arr[0] * 1000
    
# 2개만 동일
elif len(set(arr)) == 2:
    for x in arr:
        if arr.count(x) == 2:
            result = 1000 + x * 100
            break
            
# 다 다를 경우
else:
    result = max(arr) * 100
    
print(result)