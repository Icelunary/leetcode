class Solution:
    HALF_SCALE = 30
    def angleClock(self, hour: int, minutes: int) -> float:
        # x = 7.123971293
        # round(x, 5)
        # print(x)
        
        
        hourScale = self.convertHourToScale(hour)
        hourScale += self.addMinuteScale(minutes)
        # print(hour, minutes, hourScale)
        dis = abs(hourScale - minutes)
        if dis > self.HALF_SCALE:
            dis = self.HALF_SCALE * 2 - dis
        return dis * 6
    
    def convertHourToScale(self, hour) -> int:
        if hour == 12:
            return 0
        return hour * 5
    
    def addMinuteScale(self, minute) -> float:
        return 5/60 *minute
    