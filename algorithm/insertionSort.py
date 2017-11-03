# -*- coding: utf-8 -*- 
def insertionSort(data):

    #1번 인덱스 원소부터
    for i in range(1, len(data)):
        j = i-1
        #마지막에 남는 자리에 넣어주기 위해서 담아놓는다
        temp = data[i]

        #왼쪽에 있는 값들 중 기준보다 큰 값이 있으면, 땡긴다.
        while data[j] > temp and j>=0:
            #한칸씩 땡긴다. 덮어씌워도 되는 이유는 data[i]값이 temp에 들어있기 때문.
            data[j+1] = data[j]
            #기준을 왼쪽으로 옮긴다
            j = j-1
        #while문이 끝나면 최종 기준값 자리에 자리 잡는다.
        #while문을 한번 더 돌아서 -1이 더 되었으므로 +1을 보정해준다
        data[j+1] = temp
    return data


def main():
    arr = [1,5,3,2,8]
    result = insertionSort(arr)
    
    for line in result :
        print(line)

if __name__ == "__main__":
    main()