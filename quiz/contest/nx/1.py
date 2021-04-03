import sys

def solution(words):
    result = []
    
    for word in words:
        total = 0
        temp = 1
        for i in range(1, len(word)):
            #ㅇ이전글자와 같으면
            if word[i-1] == word[i]:
                temp += 1
                if i == len(word) -1:
                    total += temp//2
            else:
                #같지 않으면
                total += temp//2
                temp = 1
            print(word[i], temp)
        result.append(total)
    return result

def main():
    result = solution(["rplpqbzsnpotqwmcrdyckzfyghzz"])
    # result = solution(["aab"])
    print(result)

if __name__ == "__main__":
    main()