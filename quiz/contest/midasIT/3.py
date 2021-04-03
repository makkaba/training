# -*- coding: utf-8 -*-
import sys
input = raw_input
    
            
            

def main():
    arr = []
    n = int(input())
    
    #i그램 단위로 쪼갰을때 다 살수 있는 최소 값
    #
    ans = [0 for i in range(n)]
    
    arr = [int(v) for v in input().split()]
    
    largeNum = max(arr)
    
    for i in range(1, largeNum+1):
        for j in range(n):
            if arr[j] <= i+4:
                continue
            else:
                ans[i] += arr[j]
    
    
    print(max(ans))

if __name__ == "__main__":
    main()