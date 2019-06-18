import unittest
from graph import Graph

class GraphTest(unittest.TestCase):

    # def __init__(self):
    #     super().__init__(self)
    #     self.log = logging.getLogger("graph.day1")

    @classmethod
    def setUpClass(self):
        self.graph = Graph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_vertex(4)
        self.graph.add_vertex(5)
        self.graph.add_vertex(6)
        self.graph.add_vertex(7)
        self.graph.add_edge(5, 3)
        self.graph.add_edge(6, 3)
        self.graph.add_edge(7, 1)
        self.graph.add_edge(4, 7)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(7, 6)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(4, 6)

    def test_load_vertices(self):
        self.assertEqual(self.graph.vertices,
                         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}})

    def test_dft(self):
            # Valid DFT paths:
        paths = [
            [1, 2, 3, 5, 4, 6, 7],
            [1, 2, 3, 5, 4, 7, 6],
            [1, 2, 4, 7, 6, 3, 5],
            [1, 2, 4, 6, 3, 5, 7]
        ]
        t = []
        def cb(x): return t.append(x)
        self.graph.dft(1, cb)
        self.assertIn(t, paths)
        t = []
        self.graph.dft_recursive(1, None, cb)
        self.assertIn(t, paths)

    def test_bft(self):
        # Valid BFT paths:
        paths = [
            [1, 2, 3, 4, 5, 6, 7],
            [1, 2, 3, 4, 5, 7, 6],
            [1, 2, 3, 4, 6, 7, 5],
            [1, 2, 3, 4, 6, 5, 7],
            [1, 2, 3, 4, 7, 6, 5],
            [1, 2, 3, 4, 7, 5, 6],
            [1, 2, 4, 3, 5, 6, 7],
            [1, 2, 4, 3, 5, 7, 6],
            [1, 2, 4, 3, 6, 7, 5],
            [1, 2, 4, 3, 6, 5, 7],
            [1, 2, 4, 3, 7, 6, 5],
            [1, 2, 4, 3, 7, 5, 6],
        ]
        t = []
        def cb(x): return t.append(x)
        self.graph.bft(1, cb)
        self.assertIn(t, paths)
        t = []
        self.graph.bft_recursive(1, cb)
        self.assertIn(t, paths)

    def test_bfs(self):
        # Valid BFS path:
        t = [1, 2, 4, 6]
        self.assertRaises(IndexError, self.graph.bfs, *[6, 7])
        self.assertEqual(self.graph.bfs(1, 6), t)

    def test_tfs(self):
        # Valid DFS path:
        t = [
            [1, 2, 4, 6],
            [1, 2, 4, 7, 6]
        ]
        self.assertRaises(IndexError, self.graph.dfs, *[6, 7])
        self.assertIn(self.graph.dfs(1, 6), t)


if __name__ == '__main__':
    unittest.main()
