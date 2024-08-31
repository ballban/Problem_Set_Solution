from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_map = {
            'a': 3,
            'b': 5,
            'c': 7,
            'd': 11,
            'e': 13,
            'f': 17,
            'g': 19,
            'h': 23,
            'i': 29,
            'j': 31,
            'k': 37,
            'l': 41,
            'm': 43,
            'n': 47,
            'o': 53,
            'p': 59,
            'q': 61,
            'r': 67,
            's': 71,
            't': 73,
            'u': 79,
            'v': 83,
            'w': 89,
            'x': 97,
            'y': 101,
            'z': 103
            }
        result = {}

        for s in strs:
            product = 1
            for c in s:
                product *= alphabet_map[c]

            if product in result:
                result[product].append(s)
            else:
                result[product] = [s]
        
        return list(result.values())