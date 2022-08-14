class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = 0
        vertical = 0
        for direction in moves:
            if direction == "U":
                vertical += 1
            elif direction == "D":
                vertical -= 1
            elif direction == "L":
                horizontal -= 1
            elif direction == "R":
                horizontal += 1
            else:
                print("wrong direction: ", direction)
        if horizontal == 0 and vertical == 0:
            return True
        else:
            return False