class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # from discuss
        dct = dict() 
        mx = 0 # maximum of destroyed targets
        
        for num in nums:
            x = num % space # if the numbers have the same remainder after division by space, 
                            # then they can be presented in the form : nums[i] + c * space
            if x not in dct:
                dct[x] = (1, num)
            else:
                dct[x] = (dct[x][0] + 1, min(dct[x][1], num)) # we always keep the minimum nums[i] for all remainders 
                
            mx = max(mx, dct[x][0])
        print(dct)
        res = float("inf")
        for key, val in dct.items(): #we just go through all the keys and find the result
            if val[0] == mx:
                res = min(res, val[1])
        
        return res
        records = Counter(nums)
        print(records)
        ma = 0
        res = -1
        for num in nums:
            while num > space:
                num -= space
                if num in records:
                    records[num] += 1
        print(records)
        for k in records:
            v = records[k]
            if v > ma:
                ma = v
                res = k
            if v == ma:
                res = min(res, k)
        return res
        
        
        
        
        
        #
        records = Counter(nums)
        ma = 0
        res = -1
        
        for seed in nums:
            cnt = 0
            for num in nums:
                if num >= seed and (num - seed) % space == 0:
                    cnt += 1
            if cnt > ma:
                ma = cnt
                res = seed
            if cnt == ma:
                res = min(res, seed)
        return res