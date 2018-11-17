# Graph

# vertex -> node in a graph
# edge -> connects two vertices
# weight -> cost of going from one vertex to another
# path -> sequence of vertices connected by edges
# cycle -> a path that starts and ends in the same vertex

# TODO
# Graph - vertList, numVertices
# x addVertex(vert) -> adds new vertex to graph
# x addEdge(fromVert, toVert) -> adds directed edge
# x addEdge(fromVert, toVert, weight) -> adds weighted directed edge
# x getVertex(vertKey) -> finds vertex with key name
# x getVertices() -> get list of vertices in graph
class Graph:
    def __init__(self,directed=False):
        self.vertList = {}
        if not directed:
            self.is_directed = False
        else:
            self.is_directed = True

    def addVertex(self,vertex):
        if self.vertList.get(vertex) is None:
            self.vertList[vertex] = Vertex(vertex)
        else:
            return 0

    def addEdge(self,from_vertex,to_vertex,weight=0):
        if self.vertList.get(from_vertex) and self.vertList.get(to_vertex):
            temp_vert = self.vertList.get(from_vertex).addNeighbor(to_vertex,weight)
            if not self.is_directed:
                self.vertList.get(to_vertex).addNeighbor(from_vertex,weight)

    def getVertex(self,id):
        return self.vertList.get(id)

    def getVertices(self):
        return list(self.vertList.keys())



# Vertex - id, connectedTo
# x addNeighbor
# x getConnections
# x getID, getWeight
class Vertex:
    def __init__(self,id=None):
        self.id = id
        self.connectedTo = {}

    def addNeighbor(self,to_vertex,weight=0):
        if self.connectedTo.get(to_vertex) is None:
            self.connectedTo[to_vertex] = weight

    def getConnections(self):
        return list(self.connectedTo.keys())

    def getId(self):
        return self.id

    def getWeight(self,to_vertex):
        return self.connectedTo.get(to_vertex)



