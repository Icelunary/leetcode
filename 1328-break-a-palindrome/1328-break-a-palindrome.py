class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        cnt = {}
        if len(palindrome) == 1:
            return ""
        for c in palindrome:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        if len(cnt) == 1 and palindrome[0] == "a":
            return palindrome[:-1] + "b"
        else:
            res = palindrome
            for i in range(len(palindrome) // 2):
                if palindrome[i] > "a":
                    if not (len(palindrome) % 2 and i == len(palindrome) // 2):
                        res = res[:i] + "a" + res[i+1:]
                        return res
            for i in range(len(palindrome) - 1, -1, -1):
                if palindrome[i] < "z":
                    return palindrome[:i] + chr(ord(palindrome[i])+1) + palindrome[i+1:]
                
