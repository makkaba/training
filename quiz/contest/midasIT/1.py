# -*- coding: utf-8 -*-
import sys
input = raw_input

def main():
    arr = []
    answer = 0
    info = input().split()
    
    y = int(info[0])
    x = int(info[1])
    k = int(info[2])
    
    
    if k == 0:
        print(y*x)
        return
    
    
    
    
    visited = [[False for i in range(x)] for j in range(y)]
    
    # 0,0부터 - y-1,x-1까지
    
    
    
    
    # print(k)
    
    for i in range(k):
        arr.append([int(v) for v in input().split(' ')])
            
    
    
    # 
    # arr[i][0] = 몇번째 열인지
    # arr[i][1] = 몇번부터
    # arr[i][2] = 몇번째까지인지
    # 
    
    
    for i in range(len(arr)):
        for j in range(arr[i][1]-1, arr[i][2]+1-1):
            row = arr[i][0]-1
            visited[row][j] = True
    
    for i in range(y):
        for j in range(x):
            if visited[i][j] == False:
                answer += 1
    
    print(answer)
    

if __name__ == "__main__":
    main()
    

