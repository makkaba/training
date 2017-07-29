# -*- coding: utf-8 -*- 
'''
나누기2
나누기3
빼기1

이 세가지의 연산만 가능할 때 n을 1로 만드는 최소경우의 수를 리턴하라.
ex) 10인 경우 1을 먼저 빼는 것이 최소경우임.
'''

d = [0]*100
def shortestNum(n):
    temp = 0
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    
    d[n] = shortestNum(n-1) + 1
    if n%3 == 0:
        temp = shortestNum(n/3) + 1
        if temp < d[n]:
            d[n] = temp
    elif n%2 == 0:
        temp = shortestNum(n/2) + 1
        if temp < d[n]:
            d[n] = temp
    
    return d[n]
    
def main():
    print("dd")
    n = input()
    result = shortestNum(n)
    print(result)
    
if __name__ == "__main__":
    main()