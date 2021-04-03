# -*- coding: utf-8 -*-
import sys
input = raw_input

def cost(from, to, visited):
    
    
    
        

def main():
    a = input().split()
    n = int(a[0])
    way = int(a[1])
    
    inf = 10002
    
    
    
    # [0][0] 은 버린다.
    dist = [[inf for i in range(n+1)] for j in range(n+1)]
    
    for i in range(way):
        (v1, v2, cost) = [int(v) for v in input().split()]
        dist[v1][v2] = cost
    
    
    for i in range(1,n+1):
        for j in range(1, n+1):
            result = cost(i, j, visited)
            
    
    if result == 0:
        print(-1)
    else:
        print(result)
    
    # for i in range(len(dist)):
    #     print(dist[i])
    
if __name__ == "__main__":
    main()