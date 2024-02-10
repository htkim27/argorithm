"""Graph : Node, Link, (Weight)
"""

graph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D", "E"},
    "D": {"B", "C", "F"},
    "E": {"C", "G", "H"},
    "F": {"D"},
    "G": {"E", "H"},
    "H": {"E", "G"}
}

def depth_first_search(graph:dict, start:str, visited:set):#DFS
    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = graph[start] - visited
        for v in nbr:
            depth_first_search(graph, v, visited)

depth_first_search(graph, start="A", visited=set())


from queue import Queue
def breadth_first_search(graph, start):#BFS
    visited = {start}

    queue = Queue()
    queue.put(start)

    while queue.empty() == False:
        node = queue.get()
        print(node, end = " ")

        nbr = graph[node] - visited

        for v in nbr:
            visited.add(v)
            queue.put(v)


breadth_first_search(graph, start="A")