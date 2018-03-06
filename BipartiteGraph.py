import fileinput
import collections

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

class Graph:
    def __init__(self, verticesCount, edgesCount):
        self.items = collections.OrderedDict()
        self.verticesCount = verticesCount
        self.edgesCount = edgesCount
        self.length = len(self.items)
    
    def addEdge(self, vertexA, vertexB):
        if vertexA in self.items.keys():
            self.items[vertexA].append(vertexB)
        else:
            self.items[vertexA] = [vertexB]

        # update length
        self.length = len(self.items)
        return True
        
    # friendly string representation of graph
    def toString(self):
        for key in self.items.keys():
            values = []
            for value in self.items[key]:
                values.append(value)
            print key, " ---> ", values
        return
    
    def isBipartite(self):
        if self.edgesCount <= 1:
            return True
        graph_depth = collections.OrderedDict()
        visited = collections.OrderedDict()
        queue = Queue()

        # Initialize source node data
        parentNode = self.items.keys()[0]
        graph_depth[parentNode] = 0
        queue.enqueue(parentNode)
        while(queue.isEmpty() == False):
            parentNode = queue.dequeue()
            # Check if key exists, will throw error attempting to search for nonexistent key
            if parentNode in self.items.keys():
                # BFS: search all neighbors/edges for currentNode
                for currentNode in self.items[parentNode]:
                    if currentNode not in visited.keys():
                        visited[currentNode] = True
                        queue.enqueue(currentNode)
                        graph_depth[currentNode] = graph_depth[parentNode] + 1
                    
                    # if a child of current node has already been 
                    # visited & are both within same graph depth 
                    # an odd cycle length exists
                    elif graph_depth[currentNode] == graph_depth[parentNode]:
                        return False
        
        # graph is bipartite if uninterrupted
        return True


def main():
    graph = None
    line_count, vertexCount, edgeCount = 0, 0, 0
    intro = "Waiting for graph input"
    tutorial = """
        Please only two integers per line. I'm not that advanced.
        Try this format:
        `3 3
        1 2
        2 3
        1 3`

        Where the first line represents the number of vertices and edges in a graph respectively
        And the trailing integers per line (u,v) represent edges in the graph.
        """
    
    print(intro)
    for line in fileinput.input():
        # first line is edge/vertex count
        # initialize graph with these values
        if line_count == 0:
            vertexEdgePair = line.split('\t')
            print vertexEdgePair
            if len(vertexEdgePair) >= 2:
                graph = Graph(int(vertexEdgePair[0]), int(vertexEdgePair[1]))
        
        elif graph is not None:
            verticesEdgesArray = line.split("\t")
            if (len(verticesEdgesArray) != 2):
                print(tutorial)
            
            # convert every string to int
            count = 0 
            while count < len(verticesEdgesArray):
                verticesEdgesArray[count] = int(verticesEdgesArray[count])
                count += 1

            graph.addEdge(*verticesEdgesArray)

            if graph.edgesCount == line_count:
                break

        line_count += 1
    
    if graph is not None:
        if graph.isBipartite():
            print('Yes')
        else:
            print('No')

main()