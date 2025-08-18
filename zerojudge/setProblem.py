# 在班上，總是會有那麼一兩個同學特別愛說別人閒話。有一天，愛八卦的同學想要知道班上的小團體到底有幾個，他知道班上誰跟誰是朋友，但是因為愛八卦的同學很懶，所以他委託你寫一個程式幫他把小團體的數目計算出來。
#
# 輸入說明
# 多筆測資
#
# 每筆測資第一行會有二個正整數
# n, k(int)
#
# n代表班上的人數(編號為0~n - 1)，k是接下來有幾筆關係
#
# 再來有k行，每行有二個整數
# a, b
# 代表編號
# a
# 跟
# b
# 的人是朋友
#
# 輸出說明
# 輸出總共有幾個小團體
#
# 小團體的定義是你的朋友或者是朋友的朋友跟你屬於同一個小團體
# 範例輸入 #1
# 5 6
# 1 0
# 0 1
# 1 2
# 2 3
# 2 4
# 4 1
# 5 4
# 1 0
# 0 1
# 2 3
# 2 4
# 範例輸出 #1
# 1
# 2

#disjoint set

while True:
    try:
        n,k = map(int, input().split())
        tmpSet = set()
        circle = []
        ans = []
        for i in range(k):
            p1,p2 = map(int, input().split())
            tmpSet.add(p1)
            tmpSet.add(p2)
            circle.append(tmpSet.copy())
            tmpSet.clear()
        for g in range(len(circle)):
            for h in range(len(circle)):
                if circle[g] & circle[h]:
                    circle[h].update(circle[g])

        for s in circle:
            if s not in ans:
                ans.append(s.copy())
        print(len(ans))
    except:
        break

