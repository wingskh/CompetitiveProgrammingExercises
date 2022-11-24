graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"],
}

def dfs(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)

    while len(stack) > 0:
        vertex = stack.pop(-1)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

dfs(graph, "A")
