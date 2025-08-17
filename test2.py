# def check_parentheses(s) :
#     stack = []
#     for ch in s :
#         if ch == "(" :
#             stack.append(ch)
#         elif ch ==")" :
#             if not stack :
#                 return false
#                 stack.poop()
#     return not stack

# from collections import deque

# q = deque()

# q.append(10)
# q.append(20)
# x = q.popleft()
# print(len(q))
# print(not q)

# from collections import deque

# q = deque()

# q.append(10)
# q.append(20)
# x = q.popleft()
# print(x)

import heapq
hq = []
heapq.heappush(hq, (2, "B"))
heapq.heappush(hq, (1, "A"))
print(heapq.heappop(hq))