def getFivePieceNum(s, dp):
    
    #모든 원소에 대하여
    for 
        s_left = ?
        dp[s_left] = getFivePieceNum(s_left)
    
    return dp[s]


def main():
    result = getFivePieceNum('101101101', [])
    print(result)
    

if __name__ == "__main__":
    main()
