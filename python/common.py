import heapq
q = []
heapq.heappush(q,(1,2))
heapq.heappop(q)
nums =[2,1,3]
nums.sort()
s = ["a","b","c"]
#print(set(zip(nums, s)))
z = list(zip(nums, s))
uz, us = zip(*z)
print(uz) 
