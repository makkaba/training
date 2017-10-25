import sys


def main():
    answer = 0
    n = input()
    data = [int(v) for v in input().split()]
    dp = [0 for i in range(len(data))]
    dp[0] = data[0]
    for i in range(1, len(data)):
        dp[i] = max(dp[i-1]+data[i], data[i])
        
    answer = max(dp)
    print(answer)

if __name__ == "__main__":
    main()