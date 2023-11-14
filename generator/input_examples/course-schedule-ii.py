from collections import defaultdict

def findOrder(numCourses, prerequisites):

    graph = defaultdict(list)
    indegree = [0] * numCourses
    result = []
    
    # Build the graph
    for dst, src in prerequisites:
        graph[src].append(dst)
        indegree[dst] += 1
    
    # Find all nodes with 0 indegree
    queue = [i for i in range(numCourses) if indegree[i] == 0]
    
    # BFS Topological sort
    while queue:
        
        node = queue.pop(0)
        result.append(node)
        
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)
    
    if len(result) == numCourses:
        return result
    else:
        return []

