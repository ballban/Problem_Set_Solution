from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = defaultdict(int)
        for n in arr1:
            dic[n] += 1
        
        result = []
        for n in arr2:
            count = dic.pop(n)
            result +=  [n] * count
        
        sorted_lst = sorted([k for k, v in dic.items()])
        for n in sorted_lst:
            result += [n] * dic[n]

        return result