class Solution:
    DAY_MINUTE = 60 * 24
    
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        print(loginTime, logoutTime)
        loginMin = self.convertToMin(loginTime)
        print(loginMin)
        startMin = self.checkNextRound(loginMin)
        print(startMin)
        logoutMin = self.convertToMin(logoutTime)
        if logoutMin < loginMin:
            totalMin = self.DAY_MINUTE - startMin + logoutMin
            totalRound = totalMin // 15
            return totalRound
        elif loginMin < logoutMin:
            totalMin = logoutMin - startMin
            totalRound = totalMin // 15
            if totalRound < 0:
                return 0
            return totalRound
        
    def checkNextRound(self, loginTime: int) -> int:
        dis = loginTime % 15
        print(loginTime, dis)
        if dis == 0:
            return loginTime
        return loginTime + 15 - dis
    
    
    def convertToMin(self, time: str) -> int:
        hour, minute = time.split(":")
        hour = int(hour)
        minute = int(minute)
        print(hour, minute)
        totalMin = hour * 60 + minute
        if totalMin == self.DAY_MINUTE:
            totalMin = 0
        return totalMin