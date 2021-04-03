# -*- coding: utf-8 -*-
import sys
input = raw_input

def numDigit(n):
    digit = 0
    while n != 0:
        n = n//10
        digit += 1
    return digit


def numNoMatch(a,b):
    result = 0 
    while a != 0:
        if a%10 != b%10:
            result += 1
        a = a//10
        b = b//10
        
    return result


    
    
def main():
    dd = input().split()
    a = int(dd[0])
    b = int(dd[1])
    
    
    a_len = numDigit(a)
    b_len = numDigit(b)
    while a_len != b_len:
        if numNoMatch(pow(10,a_len) + a, b) > numNoMatch(10*a + 1, b):
            #뒤에 붙이기
            a = 10*a + b%10
        else:
            #앞에 붙이기
            a = pow(10,a_len)*(b%b_len) + a
        a_len = numDigit(a)
        b_len = numDigit(b)
    
    print(numNoMatch(a,b))
    
    

if __name__ == "__main__":
    main()