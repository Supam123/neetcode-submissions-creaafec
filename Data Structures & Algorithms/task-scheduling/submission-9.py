class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      count = {}
      for t in tasks:
        count[t] = count.get(t,0) + 1
      h = [-v for v in count.values()]
      heapq.heapify(h) # we created a max heap by negating it
      time = 0
      q = deque()
      while h or q:
        time += 1
        if h:
          task = heapq.heappop(h)
          task += 1
          unlock_time = time + n
          if task != 0:
            q.append((task,unlock_time))
        if q and q[0][1] == time:
          item = q.popleft()
          heapq.heappush(h,item[0])
      return time
     
  