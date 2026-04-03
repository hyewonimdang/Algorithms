import sys

T = int(input())
for i in range(T):
	dict = {}
	sentence = sys.stdin.readline().strip()
	count = 0
	
	for j in range(len(sentence)):
		# 공백 처리
		if sentence[j] == ' ':
			continue
		
		# 만약 이미 있다면 +1 카운트
		if sentence[j] in dict:
			dict[sentence[j]] += 1
		else:
			dict[sentence[j]] = 1
		
	# 최대값 찾기
	max_count = max(dict.values())
	
	result = ''
	for key in dict:
		# values가 가장 많은 key 찾기
		if dict[key] == max_count:
			max_key = key
			count += 1
			result = key
			
	# 여러 개인 경우 고려
	if count == 1:
		print(result)
	else:
		print('?')