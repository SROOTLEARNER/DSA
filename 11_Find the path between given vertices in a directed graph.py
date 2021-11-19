# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the directed graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
# Function to perform DFS traversal on the graph on a graph
def DFS(graph,s,d, visited,path):
 
    # mark current node as visited
    visited[s] = True
    path.append(s)
    if (s == d):
      print(path)
    else:  
    # do for every edge (s, d)
      for u in graph.adjList[s]:
        # `u` is not visited
        if not visited[u]:
            DFS(graph, u,d, visited,path)
    path.pop()
    visited[s]= False
 
# Check if the graph is strongly connected or not
def path1(graph,n,s,d):
 
    # to keep track of whether a vertex is visited or not
    visited = [False] * n
    path=[]
    
        # start DFS from the first vertex
    DFS(graph,s, d,visited,path)
 
        # If DFS traversal doesn't visit all vertices,
        # then the graph is not strongly connected
        
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
 
    # total number of nodes in the graph
    n = 5
 
    # construct graph
    graph = Graph(edges, n)
    path1(graph,n,2,4)