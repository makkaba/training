# -*- coding: utf-8 -*- 
import sys
# if sys.version_info < (3,):
#     input = raw_input
'''
(y,x)를 지나는 길의 개수

1. 본인을 방문하고 색칠한다(visited를 처리한다)
2. 이웃을 보고 방문하지 않았던 곳이면 방문한다

답은 맞는데, 메모이제이션이 없어서 
인풋이 많아지면 타임아웃 걸린다.
'''

def isValid(arr, y, x):
    lenY = len(arr)
    lenX = len(arr[lenY-1])

    if y >= 0 and y < lenY and x >= 0 and x < lenX:
        return True
    else:
        return False

def backTrack(arr, y, x, visited):
    visited[y][x] = True
    result = 0
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    lenY = len(arr)
    lenX = len(arr[lenY-1])


    #도착지점에 다다랐으면 길 하나 찾은것으로 간주.
    if y == lenY-1 and x == lenX -1:
        result = 1

    
    #네 방향을 다 방문
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        
        if isValid(arr, yy, xx):
            if arr[y][x] > arr[yy][xx]:
                if visited[yy][xx] == False:
                    result += backTrack(arr, yy, xx, visited)

            
    
    visited[y][x] = False
    return result

def main():
    firstLine = [int(x) for x in input().strip().split(' ')]
    ySize = firstLine[0]
    xSize = firstLine[1]

    matrix = []
    for i in range(ySize) :
        matrix.append([int(v) for v in input().split()])
    
    
    visited = [[False for i in range(xSize)] for j in range(ySize)]
    numPath = backTrack(matrix, 0, 0, visited)
    print(numPath)

if __name__ == '__main__':
    main()



