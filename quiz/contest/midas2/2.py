# -*- coding: utf-8 -*-
import sys
input = raw_input


def main():
    
    print(678//50)
    
    ans = 0
    dd = input().split()
    
    a = int(dd[0])
    b = int(dd[1])
    arr = []
    
    for i in range(a):
        arr.append(int(input()))
    
    dist = arr[1] - arr[0]
    
    n = a//b
    
    print(a//b, a%b)
    
    if a%b ==0:
        ans = n*dist + dist
    else:
        ans = n*dist + dist*(a%b)
    
    
    print(ans)
        
    


main()