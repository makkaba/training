# https://www.youtube.com/watch?v=CE2b_-XfVDk
import sys

def main():
    n = input()
    arr = [int(v) for v in input().split()]
    
    D = [1 for v in range(len(arr))]
    
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                D[i] = max(D[i], D[j]+1)
    print(max(D))

if __name__ == "__main__":
    main()