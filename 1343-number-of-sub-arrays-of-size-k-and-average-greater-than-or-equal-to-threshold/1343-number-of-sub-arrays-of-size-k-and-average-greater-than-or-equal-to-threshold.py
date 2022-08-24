class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current = sum(arr[0:k])
        print(current)
        cnt = 0
        # print(current / k)
        if current / k >= threshold:
            cnt += 1
        for i in range(k, len(arr)):
            current = current - arr[i - k] + arr[i]
            # print(i, current, arr[k])
            if current / k >= threshold:
                cnt += 1
                
        return cnt