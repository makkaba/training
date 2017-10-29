size = int(input())

D = [[0 for j in range(3)] for i in range(size)]
D[0][0] = 1
D[0][1] = 1
D[0][2] = 1
for i in range(1, size):
    D[i][0] = D[i-1][0] + D[i-1][1] + D[i-1][2]
    D[i][1] = D[i-1][0] + D[i-1][2]
    D[i][2] = D[i-1][0] + D[i-1][1]
    D[i][0] = D[i][0]%9901
    D[i][1] = D[i][1]%9901
    D[i][2] = D[i][2]%9901

print(sum(D[size-1])%9901)