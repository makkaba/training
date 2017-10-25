# 맵 순환 문제. 기본.
import sys

def isValid(y,x,size):
    if y<0 or y>=size or x<0 or x>=size:
        return False
    else:
        return True

#탐색한 갯수를 리턴한다
def findPath(mMap, height, visited, y, x):
    count = 0
    dydx = [(-1,0), (1,0), (0,1), (0,-1)]
    size = len(mMap)
    if visited[y][x] == True or mMap[y][x] <= height:
        return 0
    
    visited[y][x] = True
    # print(y,x)
    count +=1

    for dy,dx in dydx:
        yy = y +dy
        xx = x +dx
        if isValid(yy,xx,size) == True and mMap[y][x] >height:
            count += findPath(mMap, height, visited, yy, xx)
        
    
    #리턴하기 전에 원래대로 돌려놓기. 다음 함수가 탐색할 수 있도록.
    #visited[y][x] = False
    
    return count

def getNumSafe(mMap, size, height, visited):
    #모든 점마다 고립될때까지 탐색 후 돌아와.
    count = 0
    for i in range(size):
        for j in range(size):
            #탐색하면서 밟은 땅이 한개 이상이면 '영역' 이다. 증가시켜준다.
            if findPath(mMap, height, visited, i, j) > 0:
                count += 1
            # print("-----------\n")
    return count
    

def main():
    # 백준 알고리즘 전용
    # input = lambda : sys.stdin.readLine()
    n = int(input())
    arr = []
    temp = []
    answer = []
    # visited = [[False for j in range(n)] for i in range(n)]
    maxHeight = 0
    
    for i in range(n):
        temp = [int(v) for v in input().split()]
        arr.append(temp)
        maxHeight = max (max(temp), maxHeight)
    
    for h in range(maxHeight):
        visited = [[False for j in range(n)] for i in range(n)]
        answer.append(getNumSafe(arr,n,h,visited))
    # print(answer)
    print(max(answer))
    
    
if __name__ == "__main__":
    main()