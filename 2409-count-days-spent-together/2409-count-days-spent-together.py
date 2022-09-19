class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a1_m, a1_d = arriveAlice.split("-")[0], arriveAlice.split("-")[1]
        a2_m, a2_d = arriveBob.split("-")[0], arriveBob.split("-")[1]
        
        l1_m, l1_d = leaveAlice.split("-")[0], leaveAlice.split("-")[1]
        l2_m, l2_d = leaveBob.split("-")[0], leaveBob.split("-")[1]
        # print(a1_m, a1_d, l1_m, l1_d, a2_m, a2_d, l2_m, l2_d)
        return self.shareDays(a1_m, a1_d, l1_m, l1_d, a2_m, a2_d, l2_m, l2_d)
    
    def shareDays(self, a1_m, a1_d, l1_m, l1_d, a2_m, a2_d, l2_m, l2_d):
        aliceAD = self.getTotalDays(self.atoi(a1_m)) + self.atoi(a1_d)
        bobAD = self.getTotalDays(self.atoi(a2_m)) + self.atoi(a2_d)
        aliceLD = self.getTotalDays(self.atoi(l1_m)) + self.atoi(l1_d)
        bobLD = self.getTotalDays(self.atoi(l2_m)) + self.atoi(l2_d)
        # print(aliceAD, aliceLD, bobAD, bobLD)
        if aliceAD <= bobLD and aliceAD >= bobAD:
            # print("alice")
            l = aliceAD
            r = min(aliceLD, bobLD)
            return r - l + 1
        elif bobAD <= aliceLD and bobAD >= aliceAD:
            # print("bob")
            l = bobAD
            r = min(aliceLD, bobLD)
            # print(l, r)
            return r - l + 1
        else:
            return 0
    
    def atoi(self, s):
        if s[0] == "0":
            return int(s[1])
        else:
            return int(s)
    
    def getTotalDays(self, month):
        #        1  2    3   4   5  6   7   8   9   10  11   12
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days[:month-1])