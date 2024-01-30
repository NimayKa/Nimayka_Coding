class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vert):
        if vert not in self.graph:
            self.graph[vert] = []

    def addEdge(self, fromVert, toVert):
        if fromVert in self.graph and toVert in self.graph:
            self.graph[fromVert].append(toVert)
        
        else:
            print('Vertex does not exist in graph')

    def search(self, vert):
        
        if vert in self.graph:
            return True
        else:
            return False

    
    def getEdges(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            print(f'This vertex "{vertex}" is not found in current graph')

    def size(self):
        return len(self.graph)


    def isPath(self, start, end, visited=None):

        visited = []
        visited.append(start)

        if start not in self.graph or end not in self.graph :
            return False
        else:
            if start == end:
                return True
            
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    if self.isPath(neighbor, end, visited):
                        return True
            
    
    def Show_Graph(self):
         for vertex in self.graph:
            print(f'Edge of vertex {vertex}: {self.graph[vertex]}')
            
               

# Create an instance of DirectedGraph
graph = DirectedGraph()

# Add vertices
graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('C')
graph.addVertex('D')
graph.addVertex('E')

# Add directed edges
graph.addEdge('A','B')
graph.addEdge('D','E')
graph.addEdge('D','C')
graph.addEdge('A','D')


# Check if a vertex is in the graph
print("Is 'A' in the graph?", graph.search('A'))
print("Is 'Z' in the graph?", graph.search('Z'))

# Get the edges of a vertex
print("Edges of 'A':", graph.getEdges('A'))
print("Edges of 'E':", graph.getEdges('E'))

# Get the number of nodes in the graph
print("Number of nodes in the graph:", graph.size())

# Check if there is a path between two nodes
print("Is there a path from 'A' to 'D'?", graph.isPath('A', 'E'))
print("Is there a path from 'Z' to 'N'?", graph.isPath('D', 'B'))

# Display all vertices with respective edges
print('\nDisplay Graph : ')
graph.Show_Graph()
