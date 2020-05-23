class Graph:
    def __init__(self, vertices):
        self.graph = {x:set() for x in vertices}

    def add_edge(self, x, y):
        self.graph[x].add(y)
        self.graph[y].add(x)

    def BFS(self, x):
        visited = set()
        queue = [x]

        while queue != []:
            current = queue.pop(0)
            for vertex in self.graph[current]:
                if vertex not in visited and vertex not in queue:
                    queue.append(vertex)
                    print(vertex)
            visited.add(current)


    def DFS(self, x):
        visited = set()
        discovered = set()

        def traverse(current):
            for vertex in self.graph[current]:
                if vertex not in discovered:
                    discovered.add(vertex)
                    traverse(vertex)
            visited.add(current)

        traverse(x)

    def topological_sort():
        pass


    def shortest_path(self, x, y):
        visited = set()
        paths = []

        def traverse(path):
            current = path[-1]
            for vertex in self.graph[current]:
                if current == y:
                    paths.append(path)
                    return
                if vertex not in path:
                    traverse(path + [vertex])
            visited.add(current)

        traverse([x])

        return list(map(lambda path: min(path) min())








graph = Graph(['A','B','C','D','E'])
graph.add_edge('A','C')
graph.add_edge('A','D')
graph.add_edge('B','C')
graph.add_edge('B','E')
graph.add_edge('C','D')
graph.add_edge('D','E')

graph.shortest_path('A', 'E')



# get rid of self as first parameter of class functions
# change [ lambda x: x * x ] to [ x => x * x ] replace lambda functions with one line arrow functions
# make dictionaries like JS objects where keys need not be strings [JSON]
# make arrays that can handle only one type
# make variables type specific
