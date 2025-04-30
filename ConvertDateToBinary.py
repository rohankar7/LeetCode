# 3280. Convert Date to Binary
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")
        return f"{bin(int(year))[2:]}-{bin(int(month))[2:]}-{bin(int(day))[2:]}"