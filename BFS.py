graph = {'A': set(['B', 'C']),
'B': set(['A', 'D', 'E']),
'C': set(['A', 'F']),
'D': set(['B']),
'E': set(['B', 'F']),
'F': set(['C', 'E'])}
print("Graph : ",graph);
def bfs(graph,start):
  visited, queue =[],[start]
  while queue:
    vertex = queue.pop()
    if vertex not in visited:
      visited.append(vertex)
      queue.extend(graph[vertex] - set(visited))
  return visited
print("BFS : ",bfs(graph, 'A'))

def bfs_paths(graph, start, goal):
  queue = [(start, [start])]
  while queue:
    (vertex, path) = queue.pop(0)
    for next in graph[vertex] - set(path):
      if next == goal:
        yield path + [next]
      else:
        queue.append((next, path + [next]))

print("Paths (A,F): ",list(bfs_paths(graph, 'A', 'F')))
def shortest_path(graph, start, goal):
  try:
    return next(bfs_paths(graph, start, goal))
  except StopIteration:
    return None

print("Shortest Path: ",shortest_path(graph, 'A', 'F'))
