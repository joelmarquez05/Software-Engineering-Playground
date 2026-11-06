# [a, b] a <- b, so we should calculate the degree that comes to a, inc_degree, to check if it
# starts

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj_list = [[] for _ in range(numCourses)]

        for course, required_course in prerequisites:
            adj_list[required_course].append(course) # required_course -> course
        
        indegree = [0] * numCourses

        for course, required_course in prerequisites:
            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            order.append(course)

            for postrequisite_course in adj_list[course]:
                indegree[postrequisite_course] -= 1
                if indegree[postrequisite_course] == 0:
                    queue.append(postrequisite_course)

        if len(order) == numCourses:
            return order
            
        return []



        