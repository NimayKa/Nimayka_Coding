class undirectedgrpah:
    def __init__(self):
        self.graph = {}

    def addvorterx(self,vert):
        if vert not in self.graph:
            self.graph[vert] = []
        else:
            print("vertex already exists")

        print(self.graph)
    
    def addedge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def getvertex(self,vertkey):
        if vertkey in self.graph:
            return print(True)
        else:
            return print(False)
        
    def getvertices(self):
        for vertex in self.graph:
            print (vertex,end='')
    
    def getalledge(self):
        for vertex in self.graph:
            print ('Connected vertices of', vertex,'are',self.graph[vertex])

    def getEdge(self,vertkey):
        for vertex in self.graph[vertkey]:
            print (vertex,end='|')
    

    
            
graph = undirectedgrpah()
graph.addvorterx('a')
graph.addvorterx('b')
graph.addvorterx('c')
graph.addvorterx('d')
graph.addvorterx('e')

graph.addedge('a','b')
graph.addedge('a','c')
graph.addedge('b','c')
graph.addedge('b','d')
graph.addedge('c','e')

graph.getalledge()

graph.getEdge('b')
