# -*- coding: utf-8 -*- 
def getSmallNumbers(data, pivot):
    result = []
    #O(n)
    for i in range(len(data)):
        if data[i] <= pivot:
            result.append(data[i])
    return result 
def getLargeNumbers(data, pivot):
    result = []
    #O(n)
    for i in range(len(data)):
        if data[i] > pivot:
            result.append(data[i])
    return result
def quickSort(data):
    
    if len(data) <= 1:
        return data

    mid = len(data)//2
    pivot = data[mid]
    #피봇을 제외한 배열을 보내야 함
    temp = data[:mid] + data[mid+1:]
    left = getSmallNumbers(temp, pivot)
    right = getLargeNumbers(temp, pivot)

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

def main():
    n = [5,3,1,2,7]
    result = quickSort(n)
    for line in result:
        print(line)


if __name__ == "__main__":
    main()
