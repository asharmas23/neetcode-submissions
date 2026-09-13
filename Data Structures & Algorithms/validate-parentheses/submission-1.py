class Solution:
    def isValid(self, s: str) -> bool:
        stackList = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in closeToOpen:
                if stackList and stackList[-1] == closeToOpen[c]:
                    stackList.pop()
                else:
                    return False
            else:
                stackList.append(c)
        return True if not stackList else False
