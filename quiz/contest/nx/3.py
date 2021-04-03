
'''
D[i] i 번째를 잘랐을 때 최소 5의 배수 갯수
D[i] = getFivePieceNum(D[:1]) + getFivePieceNum(D[1:])
D[i] = getFivePieceNum(D[:2]) + getFivePieceNum(D[2:])
#최소값 갱신
'''


def getFivePieceNum(s):
    print("s!", s)
    total = 0
    nums = []
    origin = int(s, 2)
    if origin%5 != 0:
        return 98098098098
    
    for i in range(22):
        n = pow(5,i)
        nums.append(bin(n)[2:])
    
    minNum = 998098098
    #20개 돌아서 있으면 또 나머지 가지고 리컬시브 타기
    for num in nums:
        
        idx = s.find(num)
        if idx != -1:
            # print("find!", num)
            result = getFivePieceNum(s[:idx]+s[idx+len(num)+1:])
            print(result)
            minNum = min(result, minNum)
        
        #뻗어본 가지 중 가장 최소를 갱신한다
    if minNum == 998098098:
        minNum = 0
            
    # print("return min!", minNum)
    return minNum + 1

def main():
    result = getFivePieceNum('101101101')
    print(result)
    
    
#result = solution()
    #21까지 가능.
    # for i in range(23):
    #     n = pow(5,i)
    #     result= bin(n)[2:]
    #     # print(n, "=", result)
    #     print(i,"th length:", len(result))
    #     if len(result) > 50:
    #         print("stop:",i)
    # print(bin(5)[2:], bin(25)[2:], bin(125)[2:])
#print(result)


if __name__ == "__main__":
    main()
