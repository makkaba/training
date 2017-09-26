import sys

def stair(data) :
    '''
    각 계단에 쓰여있는 점수가 list로 주어질 때, 이 게임에서 얻을 수 있는 총 점수의 최댓값을 반환하는 함수를 작성하세요.
    '''

    n = len(data)

    if n == 1 :
        return data[0]
    if n == 2 : 
        return data[0] + data[1]
    if n == 3 :
        return max(data[0]+data[2], data[1]+data[2])

    Table = [0 for i in range(n)]

    Table[0] = data[0]
    Table[1] = data[0] + data[1]
    Table[2] = max(data[0]+data[2], data[1]+data[2])

    for i in range(3, n) :
        Table[i] = max(Table[i-2] + data[i], Table[i-3] + data[i] + data[i-1])

    return Table[n-1]

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(stair(data))

if __name__ == "__main__":
    main()
