# что храним в dp - dp[i][j] - длина НОП A[0..i-1], B[0...j-1]
# база dp[0][0]
# переход dp[i][j] = dp[i-1][j-1] + 1, a[i-1]=b[j-1]
#                    max(dp[i-1][j], dp[i][j-1])
# порядок обхода по возрастанию i, по возрастанию j
# где ответ? dp[n][m]
def lcs(str1: str, str2: str) -> str:
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    p = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                p[i][j] = (i-1, j-1, s1[i-1])
            else:
                if dp[i][j-1] > dp[i - 1][j]:
                    dp[i][j] = dp[i][j-1]
                    p[i][j] = (i, j -1, '')
                else:
                    dp[i][j] = dp[i- 1][j]
                    p[i][j] = (i-1,j,'')
    cur = p[n][m]
    ans = ''
    while cur is not None:
        ans += cur[2]
        cur = p[cur[0]][cur[1]]
    return ans[::-1]

if __name__ == '__main__':
    s1 = 'abacaba'
    s2 = 'abcabc'
    print(lcs(s1, s2))
