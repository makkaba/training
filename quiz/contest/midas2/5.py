# -*- coding: utf-8 -*-
import sys
input = raw_input

def genStr(n):
    s = ''
    for i in range(0, n):
        s= s+ chr(i+65)
    
    return s

def findIdx(arr, a):
    for i in range(len(arr)):
        if arr[i] == a:
            return i
        
    return -1

def main():
    # print(ord('A'))
    
    n = int(input())
    size = int(input())
    
    s = genStr(n)
    
    
    for i in range(size):
        a,b = input().split()
        if a > b:
            
            #b 바로 뒤에 a를 집어넣어야함
            s = s.replace(b,"")
            idx = findIdx(s, a)
            if idx == -1:
                print("no")
            s = s[0:idx+1] + b + s[idx+1:]
        
    print(s)
    
if __name__ == "__main__":
    main()