# 2437. Number of Valid Clock Times
class Solution:
    def countTime(self, time: str) -> int:
        hour, minute = time.split(":")
        totalHour, totalMin = 0, 0
        if hour=="??": totalHour = 24
        elif hour[0]=="?" and hour[1]!="?": totalHour = 2 if int(hour[1])>3 else 3
        elif hour[0]!="?" and hour[1]=="?": totalHour = 4 if int(hour[0])==2 else 10
        else: totalHour = 1
        if minute=="??": totalMin = 60
        elif minute[0]=="?" and minute[1]!="?": totalMin = 6
        elif minute[0]!="?" and minute[1]=="?": totalMin = 10
        else: totalMin = 1
        return totalHour*totalMin if (totalHour!=0 and totalMin!=0) else totalHour+totalMin