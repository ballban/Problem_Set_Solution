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
            if difference >= 0:
                count = 0
                while dp[difference][0] == 0 and difference > 0:
                    difference -= 1
                    count += 1

                if difference == 0:
                    dp[duration] = [1, 0]
                else:
                    count = dp[difference][1]
                    new_value = dp[difference][0] + 1
                    for x in range(1, count + 1):
                        if dp[difference + x][0] == 0 or dp[difference][0] > dp[difference + x][0]:
                            dp[difference + x] = [dp[difference][0], x]

                    for x in range(0, count + 1):
                        if dp[lastDay - x][0] == 0 or new_value > dp[lastDay - x][0]:
                            dp[lastDay - x] = [new_value, count - x + dp[difference][1]]

                # for x in range(count, -1, -1):
                #   dp[lastDay - count] = [new_value,x] if new_value > dp[lastDay][0] else dp[lastDay]
                #   dp[duration] = [1, 0] if dp[duration][0] == 0  else dp[duration]

                # if count > 0:
                #   dp[lastDay - count] = new_value

                # for x in range(1, count + 1):
                #   dp[lastDay - x] = new_value if new_value > dp[lastDay - x] else dp[lastDay - x]
            print(dp)
        return max(dp)

    def scheduleCoursee(self, courses: List[List[int]]) -> int:
        """
        it works. 5%
        """
        courses.sort(key = lambda course: (course[1]))
        #print(courses)

        sum = 0
        result = []
        for course in courses:
            duration, lastDay = course
            if lastDay - duration >= 0:
                if sum + duration <= lastDay:
                    sum += duration
                    result.append(duration)
            else:
                max_value = max(result)
                if duration <= max_value:
                    result.remove(max_value)
                    result.append(duration)
                    sum += duration - max_value
            #print(result)
        return len(result)

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