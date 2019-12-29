'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3
ABCDEFGHIJKMLNOPQRSTUVWXYZ

'''

def how_many_ways(digitarray):
    # implement here
    
    s = digitarray.lstrip('0')
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1, n):
        #判断10或20的组成可能是BA/K或CA/U,两种变化
        if s[i] == "0":
            if (s[i - 1] == "1" or s[i - 1] == "2"):
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                return 0
        else:
            if s[i - 1] == "1" or (s[i - 1] == "2" and 0 <= int(s[i]) <= 5):
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]
    return dp[-1]
