# -*- coding: utf-8 -*-
import sys
input = raw_input

def getCostPelin(s, size):
    sum = 0 
    for i in range(0, size//2):
        left = ord(s[i])
        right = ord(s[size-1-i])
        
        if(left > right):
            sum += left-right
        else:
            sum += right -left
            
    return sum

def main():
    
    ans = []
    T = int(input())
    
    for i in range(T):
        str = input()
        s = list(str)
        size = len(s)
        ans.append( getCostPelin(s, size) )
        
        
    print(ans)

if __name__ == "__main__":
    main()