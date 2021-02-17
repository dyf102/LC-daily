import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """LC 1235. Maximum Profit in Job Scheduling

        Args:
            startTime (List[int]): [description]
            endTime (List[int]): [description]
            profit (List[int]): [description]

        Returns:
            int: [description]
        """
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(jobs)
        dp = [[0,0]]
        # print(jobs)
        for i in range(n):
            # find right-most less or equal position
            idx = bisect.bisect_right(dp, [jobs[i][1], float('inf')]) - 1
            if dp[idx][1] + jobs[i][2] > dp[-1][1]:
                dp.append([jobs[i][0], dp[idx][1] + jobs[i][2]])
        return max([x[1] for x in dp ])
        
        