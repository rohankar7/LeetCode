# 3248. Snake in Matrix
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        currentCell = 0
        for i in commands:
            match i:
                case "UP": currentCell -= n
                case "DOWN": currentCell += n
                case "LEFT": currentCell -= 1
                case _: currentCell += 1
        return currentCell