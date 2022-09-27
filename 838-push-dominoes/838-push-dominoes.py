class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = []
        marker = 0
        for i in range(n):
            dominoe = dominoes[i]
            if dominoe != ".":
                marker = i
            left.append(marker)
        # print(left)
        right = []
        marker = n - 1
        for i in range(n-1, -1, -1):
            if dominoes[i] != ".":
                marker = i
            right.append(marker)
        right.reverse()
        if not right:
            return dominoes
        res = ""
        # print(right)
        for i in range(n):
            dominoe = dominoes[i]
            if dominoe != ".":
                res += dominoe
            else:
                l = left[i]
                r = right[i]
                # if left is R
                if dominoes[l] == "R":
                    # if right is not L
                    if dominoes[r]  != "L":
                        res += "R"
                    # if right is L
                    else:
                        mid = (l + r) // 2
                        print(l, r, dominoes[mid])
                        if i < mid:
                            res += "R"
                        elif i > mid:
                            res += "L"
                        else:
                            if not (r - l) % 2:
                                # print("case1")
                                res += "."
                            else:
                                # print("case2")
                                res += "R"
                # if left is L or "." and right is L
                elif dominoes[r] == "L":
                    res += "L"
                else:
                    res += "."
        return res
