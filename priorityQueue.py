import heapq 

pq = []
heapq.heappush(pq,(-2,50))
heapq.heappush(pq,(-3,60))
heapq.heappush(pq,(-4,20))
heapq.heappush(pq,(-5,10))
heapq.heappush(pq,(-1,40))
heapq.heappush(pq,(-6,50)) 
print(pq)

while pq:
    priority, ele = heapq.heappop(pq)
    print(priority, ele)