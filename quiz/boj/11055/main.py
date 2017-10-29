n =int(input())
arr = [int(v) for v in input().split()]

# D[i] = i원소를 끝으로 하는 수열의 최대 합

# 자기 자신으로 초기화
# 조심!! D = arr는 값 복사가 아니라 래퍼런스를 덮어씌워버림. 
# 따라서, D[i]를 변경하면 arr[i]도 변한다!!!!
# 그러므로 arr[:]를 써야한다

D = arr[:]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            D[i] = max(D[j]+arr[i], D[i])
    

print(max(D))