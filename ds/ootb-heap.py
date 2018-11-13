# OOTB python heap
# Main functions
# L heapify
# L heappush
# L heappop
# L heapreplace

# creation
import heapq

h = [21,2,45,78,3,5]
heapq.heapify(h)


# insert
heapq.heappush(h,1)

# remove
min_item = h[0]
heapq.heappop(h)
