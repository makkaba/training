n, m = [int(v) for v in input().split()]

arr = []
for i in range(n):
    arr.append([int(v) for v in input().split()])

'''
D[i][j] = (i,j)를 거쳐서 갈 수 있는 최대값
'''
D = [ [0 for x in range(m)] for y in range(n) ]
D[0][0] = arr[0][0]
for i in range(1, m):
    D[0][i] = arr[0][i] + D[0][i-1]
for i in range(1, n):
    D[i][0] = arr[i][0] + D[i-1][0]
    
for i in range(1, n):
    for j in range(1, m):
        D[i][j] = max(D[i-1][j], D[i][j-1], D[i-1][j-1]) + arr[i][j]
        # print(i,j,":",D[i][j])
print(D[n-1][m-1])