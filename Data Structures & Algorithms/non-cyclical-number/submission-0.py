class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            summa = 0
            for symbol in str(n):
                summa += int(symbol)**2
            if summa == 1:
                break
            if summa in visited:
                return False
            visited.add(summa)
            n = summa
        return True