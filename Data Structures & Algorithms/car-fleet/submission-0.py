class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            [(pos, spe) for pos, spe in zip(position, speed)], 
            key=lambda el: -el[0]
        )
        groups = 0
        stack = []
        for pos, spe in cars:
            if not stack or stack[-1] < (target - pos) / spe:
                stack.append((target - pos) / spe)
                groups += 1
        return groups



