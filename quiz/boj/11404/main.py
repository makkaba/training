import sys
import math

# !!!!미완성
INF = 987654321

def main():
    mapSize = int(input())
    busSize = int(input())
    
    
    dist = [[INF for j in range(mapSize)] for i in range(mapSize)]
    
    
    #문제에서 주어진 기본 정보 정리해서 넣기
    for i in range(busSize):
        from_i, to_i, distance = map(int, input().split())
        if dist[from_i-1][to_i-1] > distance:
            dist[from_i-1][to_i-1] = distance
    
    for i in range(mapSize):
        dist[i][i] = 0
        
    for i in range(mapSize):
        for j in range(mapSize):
            for k in range(mapSize):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    #지금까지 알려진 거리보다 더 짧으면 업데이트
                    dist[i][j] = dist[i][k] + dist[k][j]
    # 기본 정보 출력
    # for i in range(mapSize):
    #     print(dist[i])
    
    for i in range(mapSize):
        s = " "
        temp = s.join([str(el) for el in dist[i]])
        print(temp)
        #print s.join([str(el) for el in dist[i]])s
        # for j in range(1, mapSize+1):
        #     if
        #     print(dist[i][j])

if __name__ == "__main__":
    main()
    