# -*- coding: utf-8 -*-
import sys
input = raw_input

def findPath(arr, visited,n, y, x):
    sum = 0
    if visited[y][x] == True or arr[y][x] == 0:
        visited[y][x] = True
        print("aa")
        return 0
    
    if visited[y][x] == False and arr[y][x] ==1:
        print("bb")
        sum +=1
        visited[y][x] = True
        
    
    
    
    ddyx = [(0,1), (0,-1), (1,0), (-1,0)]
    for dy,dx in ddyx:
        yy = y+dy
        xx = x+dx
        
        if yy >=0 and yy< n and xx >=0 and xx <n:
            sum += findPath(arr, visited,n, yy, xx)
    
    print("return ", sum)
    return sum

def main():
    n= int(input())
    arr = []
    ans =0
    for i in range(n):
        arr.append([int(v) for v in input().split()])
        
    visited = [[False for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            result = findPath(arr, visited,n, i, j)
            print(result)
            if result != 0:
                ans +=1
    
    print(ans)
    
if __name__ == "__main__":
    main()