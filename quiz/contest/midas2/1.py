# -*- coding: utf-8 -*-
import sys
input = raw_input

def main():
    s = [int(v) for v in input().split()]
    a = s[0]
    b = s[1]
    c = s[2]
    
    '''
    tft를 먼저 뺀다
    수가 부족할때는 대리를 뺀다a[1]
    '''
    #어차피 팀 못만드는 과분수 대리는 뺀다
    print(b, a//2)
    b_overflow = b - a//2
    
    b -= b_overflow
    if c > b_overflow:
        c -= b_overflow
    print(a,b,c)
    
    c_left = c//3
    a -= c_left*2
    b -= c_left
    c -= c_left*3
    
    print(a,b,c)
    
    
    while c != 0:
        if a//2 >= b:
            a -= 1
        else:
            b -= 1
        c -= 1
    
    
    sum = 0
    
    
    
    
    
    print(b)

main()        
# if __name__ == "__main__":
#     main()