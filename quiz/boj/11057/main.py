'''
D[i][j] = i번째에 j를 세웠을 때 오름수의 i자리의 경우의 수
0번째는 스킵한다.
n=100
D[100][6] = D[99][0] + ...D[99][6]
'''

n = input()
for i in range(10):
    D[1][i]= 1

for i in range(1, n+1):
    for j in range(10):
        D[i][j] = 
    
print(sum(D[i])%10007)