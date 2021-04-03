# -*- coding: utf-8 -*-
import sys
input = raw_input

def main():
    n = int(input())
    setPrice = [int(v) for v in input().split()]
    
    D  = [0 for i in range(n+1)]
    
    '''
    D[i] = i개가 있을 때  i개를 팔았을 때 얻을 수 있는 최대 수익
    D[i] = max(D[i-1]+ max(setPrice), D[i])
    D[n] = n개를 팔 때 얻을 수 있는 최대 수익
    
    D[3] = D[2] + 1개 세트가격
    D[3] = D[1] + 2개 수익
    '''
    D[1] = setPrice[0]
    
    # j:0~n-1. n개
    
    for i in range(2, n+1):
        for j in range(i):
            D[i] = max(D[i],D[i-1-j]+ setPrice[j])
            
    print(D[n])

if __name__ == "__main__":
    main()