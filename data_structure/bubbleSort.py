# -*- coding: utf-8 -*- 
def bubbleSort(data):
    #사이즈가 반복 사용되기 때문에 미리 할당한다.
    size = len(data) - 1
    
    #반복해서 0번째 아이템부터 훑는다
    for i in range(size):
        #한번 루프를 돌때 마다 가장 오른쪽 아이템 한개의 위치가 정해진다.
        for j in range(size-i):
            #두개를 비교해서 대소관계에 맞게 스왑한다.
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def main():
    n = [5,1,3,2,8]
    '''
    포인트)
    값한번 루프를 돌때 마다 가장 오른쪽(가장 큰 값) 아이템 한개의 위치가 정해진다.
    우측부터 쌓여가는 정렬이다.
    '''
    result = bubbleSort(n)

    for line in result:
        print(line)

if __name__ == "__main__":
    main()