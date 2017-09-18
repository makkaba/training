# -*- coding: utf-8 -*- 
import sys
if sys.version_info < (3,):
    input = raw_input

'''
위에서 밑으로 지나가는 길목 경우의 수 더하는 식으로 
순차적으로 채우려다가 

사방으로 이동이 가능해서 꼬임.
"내 오른쪽에서 오는 경우의 수를 알려면 
그 오른쪽칸의 입장에서는 왼쪽인 칸에서 오는 경우의 수를 알아야 본인이 정해지므로 
무한루프를 도는게 아닌가??"

'''

def getPath(arr, row, column):

    #memoization
    T = [ [0 for j in range(column)] for i in range(row) ]
    
    '''
    오른쪽 위에서부터 밑으로 내려가자
    기저조건으로 윗줄과 왼쪽줄을 채워주자
    '''
    T[0][0] = 1
    for i in range(1, column):
        #from 왼쪽이 더 크면 길이 되는거니까
        #print(i)
        if arr[0][i-1] > arr[0][i]:
            T[0][i] = 1
    for i in range(1, row):
        if arr[i][0] < arr[i-1][0]:
            T[i][0] = 1


    for i in range(1, row):
        for j in range(1, column):
            # print(i,j)
            #위
            if i > 0 and arr[i][j] < arr[i-1][j]:
                T[i][j] += T[i-1][j]
                print("위")
            #왼쪽
            if j> 0 and arr[i][j] < arr[i][j-1]:
                T[i][j] += T[i][j-1]
                print("왼쪽")
            #아래
            if i < row-1 and arr[i][j] < arr[i+1][j]:
                T[i][j] += T[i+1][j]
                print("아래")
            #오른쪽
            if j < column-1 and arr[i][j] < arr[i][j+1]:
                T[i][j] += T[i][j+1]
                print("오른쪽")
    for i in range(row):
        print(T[i])
    return T[row-1][column-1]
    
firstLine = [int(x) for x in input().strip().split(' ')]
m = firstLine[0]
n = firstLine[1]

# m = int(input())
# n = int(input())


matrix = []
for i in range(m) :
    matrix.append([int(v) for v in input().split()])
getPath(matrix, m, n)