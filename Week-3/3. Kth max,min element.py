import heapq
def kth_min(arr,k):
    #Python has only Min-heap, so if we are trying to find min element so we will create a max_heap with -ve value
    max_heap=[]
    for num in arr:
        heapq.heappush(max_heap, -num)
        if len(max_heap) >k:
            heapq.heappop(max_heap)
    return -max_heap[0]

def kth_max(arr,k):
    max_heap=[]
    for num in arr:
        heapq.heappush(max_heap,num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return max_heap[0]

arr=[1,21,3,14,5,90]
k=3
res1= kth_min(arr,k)
res2= kth_max(arr,k)
print(f"Minimum element at position {k} is:",res1)
print(f"Maximum element at position {k} is:",res2)

