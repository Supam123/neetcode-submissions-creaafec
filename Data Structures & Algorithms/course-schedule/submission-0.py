class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        prqMap = { i : [] for i in range(numCourses)}


        for crs,pre in prerequisites:
            prqMap[crs].append(pre)
        
        def dfs(crs):

            if(crs in visit):
                return False
            if(prqMap[crs] == []):
                return True
            
            visit.add(crs)
            for pre in prqMap[crs]:
                if not dfs(pre) : return False
            visit.remove(crs)
            prqMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
        


        


        