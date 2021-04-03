#난이도 중
import sys

def solution(matrix, r):
    
    n = r%4
    result = matrix
    for i in range(n):
        result = rotate(result)
        print(i, result)
    return result
        
def rotate(matrix):
    answer = 0
    
    size = len(matrix)
    print("size",size)
    temp = [[0 for i in range(size)] for j in range(size)]
    print("first temp", temp)
    
    for i in range(size):
        for j in range(size):
            temp[i][j] = matrix[size -1 -j][i]
        # print("temp:", temp[i])
        
    return temp

def main():
    result = solution([[4,1,2],[7,3,4],[3,5,6]], 3)
    print(result)

if __name__ == "__main__":
    main()
    
    