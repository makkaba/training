# -*- coding: utf-8 -*- 

def partition(LIST, start, end):
    pivot = LIST[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and LIST[left] <= pivot:
            left += 1
        while left <= right and pivot <= LIST[right]:
            right -= 1
        if left > right:
            #다 훑었으면 끝낸다
            done = True
        else:
            #swap
            LIST[left], LIST[right] = LIST[right], LIST[left]
    
    LIST[start], LIST[right] = LIST[right], LIST[start]
    return right

def quick_sort(LIST, start, end):
    if start < end:
        pivot = partition(LIST, start, end)
        quick_sort(LIST, start, pivot - 1)
        quick_sort(LIST, pivot + 1, end)
    return LIST
    
def main():
    arr = [5,1,4,2,9]
    arr = quick_sort(arr, 0, 4)
    print(arr)
    
    
if __name__ == "__main__":
    main()