n = int(input())
arr = []
for i in range(n):
    arr.append([int(v) for v in input().split()])

'''
D[i][j] = i 번째에 j를 놨을 때 누적 최소값
D[i][j] = min(D[i-i][j]+)
'''


D = [[0 for i in range(3)] for j in range(n)]
D[0][0] = arr[0][0]
D[0][1] = arr[0][1]
D[0][2] = arr[0][2]

for i in range(1, n):
    for j in range(3):
        D[i][j] = min(D[i-1][(j+1)%3], D[i-1][(j+2)%3]) + arr[i][j]

print(min(D[n-1][0], D[n-1][1], D[n-1][2]))
