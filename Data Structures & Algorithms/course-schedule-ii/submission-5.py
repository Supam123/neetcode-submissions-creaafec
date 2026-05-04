class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {n:[] for n in range(numCourses)}
        in_degree = {n:0 for n in range(numCourses)}
        q = deque()
        for crs,pre in prerequisites:
            preMap[pre].append(crs)
            in_degree[crs] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        order = []
        while q:
            taken_course = q.popleft()
            order.append(taken_course)
            for course in preMap[taken_course]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)
        
        return order if len(order) == numCourses else []

        