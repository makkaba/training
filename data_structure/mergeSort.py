# -*- coding: utf-8 -*- 
import sys
import math

def merge(left, right):
    #left, right 두 그룹으로부터 작은 원소부터 줄세우기.
    result = []
    leftPtr = 0
    rightPtr = 0

    #left, right 중 한 그룹이라도 아직 끝까지 못한 스캔이 있다면
    while leftPtr < len(left) or rightPtr < len(right):
        '''
        범위의 마지막 요소를 스캔한 후에 +1을 더하니까 
        포인터가 배열의 길이보다 크면(leftPtr < len(left)) 실제론 가리키는 값이 없는 것.
        따라서 비교에 영향을 끼치지 않도록 최대값을 넣어준다.
        '''
        leftValue = left[leftPtr] if leftPtr < len(left) else float('inf')
        rightValue =  right[rightPtr] if rightPtr < len(right) else float('inf')
        
        if leftValue <= rightValue:
            result.append(left[leftPtr])
            leftPtr = leftPtr + 1
        else:
            result.append(right[rightPtr])
            rightPtr = rightPtr + 1
    return result

def mergeSort(data):

    #기저조건
    if len(data) <= 1:
        # 한조각이 될때까지 쪼갠다.
        return data
    
    mid = len(data)//2
    # 0 ~ mid-1까지.
    left = mergeSort(data[:mid])
    #mid ~ 끝까지
    right = mergeSort(data[mid:])

    result = merge(left, right)
    return result

def main():
    n = [5,1,3,2,8]
    '''
    포인트)
    리컬시브: 기저조건 설정, 리컬시브 로직
    '''
    result = mergeSort(n)

    for line in result:
        print(line)

if __name__ == "__main__":
    main()