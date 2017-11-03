# -*- coding: utf-8 -*- 
def getSmallLargeNumbers(data, pivot):
    left = []
    right = []
    #O(n)
    for i in range(len(data)):
        #pivot보다 작은 수는 왼쪽에
        if data[i] <= pivot:
            left.append(data[i])
        else:
            right.append(data[i])
    return (left, right)

def quickSort(data):
    
    if len(data) <= 1:
        return data

    mid = len(data)//2
    pivot = data[mid]
    #피봇을 제외한 배열을 보내야 함
    temp = data[:mid] + data[mid+1:]
    left, right = getSmallLargeNumbers(temp, pivot)
    # right = getLargeNumbers(temp, pivot)

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

def main():
    arr = [5,3,1,2,7]
    print(arr, "\n=>")
    result = quickSort(arr)
    print(result)


if __name__ == "__main__":
    main()
