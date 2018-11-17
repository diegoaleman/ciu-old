# Graph - using adjacency matrix

# TODO
# Graph - vertList, numVertices
# x addVertex(vert) -> adds new vertex to graph
# x addEdge(fromVert, toVert) -> adds directed edge
# x addEdge(fromVert, toVert, weight) -> adds weighted directed edge
# x getVertices() -> get list of vertices in graph

class Graph:
    def __init__(self,directed=False):
        self.vertices = {}
        self.matrix = []
        if not directed:
            self.directed = False
        else:
            self.directed = True

    def addVertex(self,vertex):
        if self.vertices.get(vertex) is None:
            self.vertices[vertex] = len(self.vertices)

        for row in self.matrix:
            row.append(0)

        new_row = [0] * len(self.vertices)
        self.matrix.append(new_row)

    def addEdge(self,from_vertex,to_vertex,weight=0):
        row = self.vertices.get(from_vertex)
        col = self.vertices.get(to_vertex)

        if weight == 0:
            self.matrix[row][col]=1
            if not self.directed:
                self.matrix[col][row]=1

        else:
            self.matrix[row][col]=weight
            if not self.directed:
                self.matrix[col][row]=weight

    def getVertices(self):
        return list(self.vertices.keys())

    def print(self):
        for i in self.matrix:
            for j in i:
                print(j,end=' ')
            print()



