class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        indegree = [0]*numCourses

        for crs,pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs] += 1
        # add all the course that can be finished i.e. indegree = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            finished = q.popleft()
            order.append(finished)
            for nei in preMap[finished]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return order if len(order) == numCourses else []