graph = {'A': set(['B','C']),
'B' : set(['A','D','E']),
'C' : set(['A','F']),
'D' : set(['B']),
'E' : set(['B','F']),
'F' : set(['C','E'])}

def bfs(graph,start):
  visited, queue =[],[start]
  while queue:
    vertex = queue.pop()
    if vertex not in visited:
      visited.append(vertex)
      queue.extend(graph[vertex] - set(visited))
  return visited

bfs(graph,'A')
