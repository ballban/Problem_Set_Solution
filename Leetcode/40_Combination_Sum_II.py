class Solution:
    def combinationSum2(self, candidates, target: int):
        dp = [[] for _ in range(target + 1)]
        candidates_count = dict()
        for candidate in candidates:
            if candidate < target:
                dp[candidate].append([candidate])
            # if there are many candidates equal to target
            # just add 1 candidate to dp list
            elif candidate == target and not dp[candidate]:
                dp[candidate].append([candidate])

            if candidate in candidates_count:
                candidates_count[candidate] += 1
            else:
                candidates_count[candidate] = 1
        print(dp)

        for i in range(1, len(dp)):
            if dp[i]:
                # from first element to element i
                for j in range(1, i + 1):
                    if i + j >= len(dp):
                        break
                    if dp[j]:
                        for x in dp[i]:
                            a = sorted(dp[j][0] + x)
                            if check(a, candidates_count) and a not in dp[i + j]:
                                dp[i + j].append(a)
                    print(dp)
        return dp[-1]


def check(candidate, candidates_count):
    for num in candidates_count:
        if candidate.count(num) > candidates_count[num]:
            return False
    return True



can = [10,1,2,7,6,1,5]
t = 8

can = [1,1]
t = 1

can = [10,1,2,7,6,1,5]
t= 8

s = Solution()
print(s.combinationSum2(can, t))
