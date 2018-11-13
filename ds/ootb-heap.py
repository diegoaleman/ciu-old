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



# now, with objects
h2 = []
heapq.heapify(h2)
heapq.heappush(h2,(24,'Diego'))
heapq.heappush(h2,(21,'Paula'))
heapq.heappush(h2,(15,'Fer'))

# retuns tuple with lowest value
min_elem2= h2[0]

