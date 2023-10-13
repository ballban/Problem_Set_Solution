import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pile_max = max(piles)
        # if h equal to length of piles, k must equal to max value of piles
        if len(piles) == h:
            return pile_max

        pile_sum = sum(piles)
        # result must larger than pile_sum / h, so let i start from here
        start_i = math.ceil(pile_sum / h)
        for i in range(start_i, pile_max + 1):
            sum_divide_by_i = pile_sum / i
            if sum_divide_by_i <= h:
                break

        left = i
        right = math.ceil(pile_sum / (h - len(piles) + 1))
        while right > left:
            middle = (right + left) // 2
            temp_h = 0
            for pile in piles:
                temp_h += math.ceil(pile / middle)
                if temp_h > h:
                    if left == middle:
                        left += 1
                    else:
                        left = middle
                    break
            if temp_h <= h:
                right = middle
        return left