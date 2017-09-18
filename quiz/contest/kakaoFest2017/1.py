# -*- coding: utf-8 -*- 
def probe(picture,y,x,visited,v):
    print("(",y,x,")",v)
    m = len(picture)
    n = len(picture[0])
    dydx = [(0,1),(0,-1),(1,0),(-1,0)]
    #만약 dp가 필요한 경우라면 단지 로컬변수 sum 이 아니라 dp를 써서 저장해야하지만
    sum = 0
    #이미 방문한 적이 있다면 카운트 되지 않도록 0을 리턴
    if visited[y][x] == True or picture[y][x] != v or picture[y][x] == 0:
        return 0
    elif picture[y][x] == v:
        visited[y][x] = True
        sum += 1
    
    
    for dy, dx in dydx:
        yy,xx = y+dy,x+dx
        if 0<= yy < m and 0<= xx< n and visited[yy][xx] == False:
            sum += probe(picture,yy,xx,visited, v)
    
    
        
    return sum
    
def solution(m,n,picture):
    maxSize = 0
    numArea = 0
    
    visited = [[False for i in range(n)] for j in range(m)]
    
    for y in range(m):
        for x in range(n):
            temp = probe(picture,y,x,visited, picture[y][x])
            if temp > 0:
                numArea += 1
            maxSize = max(maxSize, temp)
            
            
    return [numArea, maxSize]
def main():
    
    m = 6
    n = 4
    picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
    
    result = solution(m,n,picture)
    
    print(result[0], result[1])
    
    
if __name__ == "__main__":
    main()
    
