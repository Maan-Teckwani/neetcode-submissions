class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=[-1*num for num in nums]
        heapq.heapify(maxHeap)

        for _ in range(k-1):
            heapq.heappop(maxHeap)
        return -1*heapq.heappop(maxHeap)
        

        