def traverse(mMap, y, x, dp):
    #변수 초기화
    dydx=[(0,1),(1,0),(0,-1),(-1,0)]
    ySize = len(mMap)
    xSize = len(mMap[ySize-1])


    
    #현재 위치가 종점이면 길 한개 찾았다고 리턴해준다
    if (y,x) == (ySize - 1, xSize - 1):
        return 1
    #한번 방문한 적이 있다면? => 이미 계산이 되었으니 가져가시오. 메모이제이션
    if dp[y][x] != -1:
        return dp[y][x]
    
    # 위의 경우가 모두 아니라면, 현재 위치를 방문표시로 0을 할당해준다 
    # (색깔 칠하기)여기서부터 dfs랑 비슷한낌느낌
    dp[y][x]=0

    # 현재 지점에서 4방향을 모두 탐사시킨다.
    for dy, dx in dydx:
        yy,xx = y+dy,x+dx
        if 0 <= yy < ySize and 0 <= xx < xSize and mMap[yy][xx] < mMap[y][x]:
            dp[y][x] += traverse(mMap, yy, xx, dp)

    # 4방향을 다 탐사하고 돌아와서 결과를 보고한다. 누적시켜야 dp가 결정되기 때!문!에! 
    # 비로소 리턴해준다.
    return dp[y][x]

def main():
    #m이 세로 개수, n이 개수
    firstLine = [int(x) for x in input().split(' ')]
    m = firstLine[0]
    n = firstLine[1]
    
    mMap = []
    for i in range(m):
        mMap.append([int(x) for x in input().split()])
    

    dp = [[-1 for i in range(n)] for j in range(m)]
    print(traverse(mMap, 0, 0, dp))

if __name__ == '__main__':
    main()


#한가지 알게된 것
#1. 방문했는지, 그리고 어떤 값이 필요할때 테이블 한개로 해결할 수도 있다. -1을 사용해서
#2. 그래프 문제는 탐사시킨다. backtrack 보다 각 점에서 탐사시켜서 dp를 완성시켜나가는게 훨씬 빠르다.