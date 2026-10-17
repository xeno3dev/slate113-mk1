"""Vertices on any simple path between terminal sets in an undirected graph."""
from collections import deque


def path_vertices(graph, sources, destinations):
    discovered, low, parent = {}, {}, {}
    edges, blocks = [], []
    clock = 0
    for root in graph:
        if root in discovered:
            continue
        clock += 1
        discovered[root] = low[root] = clock
        parent[root] = None
        stack = [(root, iter(graph[root]))]
        while stack:
            node, neighbours = stack[-1]
            other = next(neighbours, None)
            if other is None:
                stack.pop()
                ancestor = parent[node]
                if ancestor is not None:
                    low[ancestor] = min(low[ancestor], low[node])
                    if low[node] >= discovered[ancestor]:
                        block = set()
                        while edges:
                            edge = edges.pop()
                            block.update(edge)
                            if edge == (ancestor, node):
                                break
                        blocks.append(block)
                continue
            if other not in discovered:
                parent[other] = node
                clock += 1
                discovered[other] = low[other] = clock
                edges.append((node, other))
                stack.append((other, iter(graph[other])))
            elif other != parent[node] and discovered[other] < discovered[node]:
                low[node] = min(low[node], discovered[other])
                edges.append((node, other))
    # The block/vertex incidence forest excludes side branches and dangling loops.
    tree = {node: set() for node in graph}
    for index, block in enumerate(blocks):
        block_id = ("block", index)
        tree[block_id] = set(block)
        for node in block:
            tree[node].add(block_id)
    result = set()
    for source in sources:
        if source not in tree:
            continue
        previous = {source: None}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            for other in tree[node]:
                if other not in previous:
                    previous[other] = node
                    queue.append(other)
        for destination in destinations:
            if destination not in previous or destination == source:
                continue
            node = destination
            while node is not None:
                if isinstance(node, tuple):
                    result.update(blocks[node[1]])
                else:
                    result.add(node)
                node = previous[node]
    return result
