class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pt = []
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.pt.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        '''
        find a valid diagonal and then if  any other poinst forma  sqaure  count it
        '''
        qx,qy = point
        for x,y in self.pt:
            if (abs(qx-x) == abs(qy-y)) and  x != qx and y != qy:
            # then that means x and y is good diagonal
                res += self.points.get((x, qy), 0) * self.points.get((qx, y), 0)        
        return res








        
