import sys
sys.path.append('../graph')
from util import Stack, Queue
from graph import Graph


def ancestor(arr, k):
    assert len(arr[0]) == 2, 'input array must have 2 columns'
    g = Graph()  # child to parent
    for row in arr:
        g.add_vertex(row[0], True)
        g.add_vertex(row[1], True)
        g.add_edge(row[1], row[0])  # link child to parent

    can = []
    q = Queue()
    q.enqueue(k)

    while q.size() > 0:
        child_q = Queue()
        v = q.dequeue()
        for neighbor in g.vertices[v]:
            child_q.enqueue(neighbor)
            q.enqueue(neighbor)
        if child_q.size() == 0:
            can.append(v)

    can.sort()
    return can[-1]


print(ancestor(
    [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [11, 8],
        [10, 1]
    ], 6
))
