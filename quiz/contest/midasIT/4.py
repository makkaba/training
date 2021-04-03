# -*- coding: utf-8 -*-
import sys
input = raw_input

def main():
    n = int(input())
    minGap = 100000000
    arr = []
    ans = 0
    
    for i in range(n):
        arr.append(int(input()))
    
    if len(arr) == 0:
        print(0)
        return
    
    for i in range(len(arr)-1):
        diff = abs(arr[i+1]-arr[i])
        minGap = min(diff, minGap)
    
    maxDistance = max(arr)
    firstDistance = arr[0]
    
    for v in range(firstDistance, maxDistance - minGap+1, minGap):
        if not v in arr:
            ans += 1
            
    print(ans)
    
if __name__ == "__main__":
    main()