class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[x * -1 for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            t1=heapq.heappop(maxHeap)
            t2=heapq.heappop(maxHeap)
            if t1==t2:
                continue
            else:
                heapq.heappush(maxHeap,t1-t2)
        if len(maxHeap)==1:
            return -1*heapq.heappop(maxHeap)
        else:
            return 0

            
            


        