from collections import defaultdict

def canFinish(numCourses, prerequisites):
  graph = defaultdict(list)
  indegree = [0] * numCourses
  
  # Build the graph
  for dest, src in prerequisites:
    graph[src].append(dest)
    indegree[dest] += 1
    
  # Start with courses having 0 indegree
  zero_indegree = [i for i in range(numCourses) if indegree[i] == 0]
  
  completed_courses = 0
  while zero_indegree:
    node = zero_indegree.pop()
    completed_courses += 1
    
    # Reduce indegree for nodes pointed from this node
    for neigh in graph[node]:
      indegree[neigh] -= 1
      if indegree[neigh] == 0:
        zero_indegree.append(neigh)
        
  return completed_courses == numCourses

numCourses = 2 
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites)) # True

numCourses = 2
prerequisites = [[1,0],[0,1]]  
print(canFinish(numCourses, prerequisites)) # False
