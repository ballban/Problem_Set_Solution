from typing import List

class Solution:
    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[0])
        print(courses)

        result = []
        sum = 0
        difference = 0
        for course in courses:
            duration_i, lastDay_i = course
            if duration_i > lastDay_i:
                continue

            if len(result) > 1:
                last_course = result[-1]

                left_time_i = lastDay_i - duration_i

                if left_time_i > sum:
                    result.append(course + [left_time_i])
                    sum += duration_i
                else:
                    result.sort(key=lambda course: course[0], reverse=True)
                    for j in range(len(result)):
                        duration_j, lastDay_j, left_time_j = result[j]
                        if left_time_i > left_time_j:
                            result[j] = course + [left_time_i]
                            sum += duration_i - duration_j
                            break

            else:
                result.append(course + [lastDay_i - duration_i])
                sum += duration_i
            print(result, sum)

        return len(result)

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: (course[1], course[0]))
        print(courses)
        dp = [[0, 0] for _ in range(max(courses, key=lambda course: course[1])[1] + 1)]

        for course in courses:
            print(course)
            duration, lastDay = course
            difference = lastDay - duration
            if difference > 0:
                target = difference
                count = 0
                while dp[target][0] == 0 and target > 0:
                    target -= 1
                    count += 1

                # for x in range(1, count + 1):
                #   dp[difference + x] = dp[difference]

                if target == 0:
                    for x in range(lastDay - duration + 1):
                       dp[duration + x] = [1, duration]
                else:
                    new_value = dp[target][0] + 1
                    for x in range(count, -1, -1):
                        dp[lastDay - x] = [new_value, lastDay - count] if new_value > dp[lastDay][0] else dp[lastDay]

                    for x in range(difference + 1):
                        dp[duration + x] = [1, duration] if dp[duration + x][0] == 0 else dp[duration + x]

                # if count > 0:
                #   dp[lastDay - count] = new_value

                # for x in range(1, count + 1):
                #   dp[lastDay - x] = new_value if new_value > dp[lastDay - x] else dp[lastDay - x]
                print(dp)
        return max(dp)

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3

courses = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
# Output: 4

#courses = [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
# Output: 5

#courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
# Output: 4

s = Solution()
print(s.scheduleCourse(courses))