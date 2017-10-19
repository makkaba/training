

n = input()
arr = []
for i in range(n):
    arr[i].append([int(v) for v in input().split()])

'''
D[i][j] = i번째에 j를 놨을 때 최소 비용
D[i][0] = max (D[i-1][1], D[i-1][2])
D[i][1] = max (D[i-1][0], D[i-1][2])
D[i][2] = max (D[i-1][0], D[i-1][1])

return max(D[n][0],D[n][1],D[n][2])

'''

D = [[0 for i in range(3)] for j in range(n)]
D[0][0] = arr[0][0]
D[0][1] = arr[0][1]
D[0][2] = arr[0][2]

for i in range(1, n+1):
    for j in range(3):
        D[i][j] = D[i][j]

