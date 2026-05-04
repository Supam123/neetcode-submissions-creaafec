class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {n:[] for n in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []: #if this course has no preq
                return True
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True
        for crs in preMap:
            if not dfs(crs):
                return False
        return True
        