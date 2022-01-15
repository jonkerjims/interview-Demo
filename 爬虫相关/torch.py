class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" or s == None:
            return 0
        elif s == " " or s == None:
            return 1
        BigList = []
        List = []
        s = list(s)
        print(s)
        for i in range(0,len(s)):
            List.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] != s[i]:
                    List.append(s[j])
                else:
                    BigList.append(List)
                    print(List)
                    List = []
                    continue

        maxLength = 0
        for li in BigList:

            if len(li) > maxLength:
                maxLength = len(li)
        return maxLength
S = Solution()
res = S.lengthOfLongestSubstring('dvdf')
print(res)