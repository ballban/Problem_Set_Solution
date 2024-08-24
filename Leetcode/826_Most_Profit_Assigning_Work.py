from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit_dict = dict(zip(difficulty, profit))
        difficulty.sort()

        i = 0
        while i < len(difficulty) - 1:
            if difficulty_profit_dict[difficulty[i + 1]] <= difficulty_profit_dict[difficulty[i]]:
                difficulty.pop(i + 1)
            else:
                i += 1

        print(difficulty)
        print(difficulty_profit_dict)
        worker.sort()
        
        diff_index = 0
        totalProfit = 0
        for w in worker:
            while True:
                if diff_index == len(difficulty) - 1:
                    break

                if w >= difficulty[diff_index]:
                    diff_index += 1
                else:
                    break
            
            if difficulty[diff_index] <= w:
                totalProfit += difficulty_profit_dict[difficulty[diff_index]]
        
        return totalProfit


s = Solution()
print(s.maxProfitAssignment([66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63], [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77], [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]))