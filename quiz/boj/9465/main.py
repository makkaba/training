def solution(arr):
	
	'''
	D[i][j] = i번째에 j(위/아래)를 선택했을 경우 누적 기대값의 최대
	D[0][0] 
	
	'''
	size = len(arr[0])
	D = [[0 for j in range(3)] for i in range(size)]
	D[0][0] = arr[0][0]
	D[0][1] = arr[1][0]
	D[1][0] = D[0][1]+arr[0][1]
	D[1][1] = D[0][0]+arr[1][1]
	for i in range(2, size):
		D[i][0] = max(D[i-1][1], D[i-2][1]) + arr[0][i]
		D[i][1] = max(D[i-1][0], D[i-2][0]) + arr[1][i]
	
	return max(D[size-1][0], D[size-1][1])

def run():
	
	T = int(input())
	arr = [[] for v in range(T)]
	
	for i in range(T):
		
		n = int(input())
		arr[i].append([int(v) for v in input().split(' ')])
		arr[i].append([int(v) for v in input().split(' ')])
	
	for i in range(T):
		print(solution(arr[i]))
	
		
if __name__ == "__main__":
	run()