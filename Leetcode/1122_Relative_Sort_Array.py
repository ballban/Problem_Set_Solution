from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frequency_map = defaultdict(int)
        for n in arr1:
            frequency_map[n] += 1
        
        result = []
        for n in arr2:
            result.extend([n] * frequency_map.pop(n))
        
        remaining_elements = sorted(frequency_map.items())
        for n, c in remaining_elements:
            result.extend([n] * c)

        return result