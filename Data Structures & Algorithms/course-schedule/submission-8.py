class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {n:[] for n in range(numCourses)}
        in_degree = {n:0 for n in range(numCourses)}
        q = deque()
        for crs,pre in prerequisites:
            preMap[pre].append(crs)
            in_degree[crs] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        taken = 0
        while q:
            finished_course = q.popleft()
            taken += 1
            for c in preMap[finished_course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        return taken == numCourses
        