from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_hour_rate = right

        while left <= right:
            hour_rate = (left + right) // 2

            curr_hours_spent = 0
            for pile in piles:
                curr_hours_spent += ceil(pile / hour_rate)

            if curr_hours_spent <= h:
                right = hour_rate - 1
                min_hour_rate = hour_rate
            else:
                left = hour_rate + 1

        return min_hour_rate
            
            