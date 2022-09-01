class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = {}
        self.countWords(cnt, words)
        picked, mid = self.pickWords(cnt)
        return (sum(picked.values()) * 2 + len(mid)) * 2
    # You can get the string from here
        res = ""
        for i in picked:
            for times in range(picked[i]):
                res += i
        res += mid
        res += res[::-1]
        return len(res)
    
    def countWords(self, cnt, words):
        for i in words:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
    
    def pickWords(self, cnt):
        mid = ""
        picked = {}
        for word in cnt:
            reverse = word[1] + word[0]
            if cnt[word] != 0:
                if word[0] != word[1] and reverse in cnt:
                    pickNum = min(cnt[word], cnt[reverse])
                    picked[word] = pickNum
                    cnt[reverse] = 0
                if word[0] == word[1]:
                    pickNum = cnt[word] // 2
                    picked[word] = pickNum
                    if mid == "" and cnt[word] % 2 == 1:
                        mid += word[0]
            cnt[word] = 0
        return picked, mid
                