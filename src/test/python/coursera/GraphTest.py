import unittest

from coursera.graphs.acyclicity import solve_acyclic
from coursera.graphs.bipartite import solve_bipartite
from coursera.graphs.connected_components import solve_cc
from coursera.graphs.connecting_points import solve_minimum_distance
from coursera.graphs.negative_cycle import solve_negative_cycle
from coursera.graphs.reachability import solve_reach
from coursera.graphs.shortest_paths import solve_shortest
from coursera.graphs.toposort import solve_toposort
from coursera.graphs.strongly_connected import solve_number_of_scc
from coursera.graphs.bfs import solve_distance
from coursera.graphs.dijkstra import solve_dijkstra

from src.main.python.coursera.graphs.clustering import solve_clustering


class TestGraphMethods(unittest.TestCase):

    def test_graph_reachable(self):
        self.assertEqual(solve_reach("4 4 1 2 3 2 4 3 1 4 1 4"), 1)
        self.assertEqual(solve_reach("4 2 1 2 3 2 1 4"), 0)
        self.assertEqual(solve_reach("10 6 2 3 3 4 3 5 7 6 6 8 9 6 2 5"), 1)
        self.assertEqual(solve_reach("10 6 2 3 3 4 3 5 7 6 6 8 9 6 3 6"), 0)

    def test_graph_component(self):
        self.assertEqual(solve_cc("4 4 1 2 3 2 4 3 1 4 1 4"), 1)
        self.assertEqual(solve_cc("4 2 1 2 3 2"), 2)
        self.assertEqual(solve_cc("10 6 2 3 3 4 3 5 7 6 6 8 9 6"), 4)

    def test_acyclic(self):
        self.assertEqual(solve_acyclic("4 4 1 2 4 1 2 3 3 1"), 1)
        self.assertEqual(solve_acyclic("5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5"), 0)
        self.assertEqual(solve_acyclic("3 3 1 2 1 3 2 3"), 0)
        self.assertEqual(solve_acyclic("3 3 1 3 1 2 2 3"), 0)
        self.assertEqual(solve_acyclic("4 4 1 2 2 3 3 4 4 2"), 1)
        self.assertEqual(solve_acyclic("6 5 1 2 3 4 4 3 5 6 6 5"), 1)

    def test_toposort(self):
        self.assertEqual(solve_toposort("4 3 1 2 4 1 3 1"), [4, 3, 1, 2])
        sort = solve_toposort("4 1 3 1")
        self.assertTrue(sort.index(3) < sort.index(1))
        self.assertIn(solve_toposort("5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3"), [[5, 4, 3, 2, 1], [4, 5, 3, 2, 1]])

    def test_scc(self):
        self.assertEqual(solve_number_of_scc("4 4 1 2 4 1 2 3 3 1"), 2)
        self.assertEqual(solve_number_of_scc("5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3"), 5)

    def test_distance(self):
        self.assertEqual(solve_distance("4 4 1 2 4 1 2 3 3 1 2 4"), 2)
        self.assertEqual(solve_distance("5 4 5 2 1 3 3 4 1 4 3 5"), -1)

    def test_bipartite(self):
        self.assertEqual(solve_bipartite("4 4 1 2 4 1 2 3 3 1"), 0)
        self.assertEqual(solve_bipartite("5 4 5 2 4 2 3 4 1 4"), 1)
        self.assertEqual(solve_bipartite("5 5 5 2 4 2 3 4 1 4 4 5"), 0)
        self.assertEqual(solve_bipartite("7 6 5 2 4 2 3 4 1 4 3 6 1 7"), 1)
        self.assertEqual(solve_bipartite("7 6 5 2 4 2 3 4 3 6 1 4 1 7"), 1)
        self.assertEqual(solve_bipartite("8 6 5 2 4 2 3 4 3 6 1 4 1 7"), 0)
        self.assertEqual(solve_bipartite("7 7 5 2 4 2 3 4 3 6 1 4 1 7 6 7"), 0)

    def test_dijkstra(self):
        self.assertEqual(solve_dijkstra("4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3"), 3)
        self.assertEqual(solve_dijkstra("5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5"), 6)
        self.assertEqual(solve_dijkstra("5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 1 3 4 4 1 5"), 4)
        self.assertEqual(solve_dijkstra("5 9 1 2 2 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5"), 5)
        self.assertEqual(solve_dijkstra("3 3 1 2 7 1 3 5 2 3 2 3 2"), -1)

    def test_negative_cycle(self):
        self.assertEqual(solve_negative_cycle("4 4 1 2 -5 4 1 2 2 3 2 3 1 1"), 1)
        self.assertEqual(solve_negative_cycle("4 4 1 2 -3 4 1 2 2 3 2 3 1 1"), 0)
        self.assertEqual(solve_negative_cycle("5 7 1 2 4 2 4 4 2 3 -2 1 3 3 3 4 -3 4 5 2 3 5 1"), 0)
        self.assertEqual(solve_negative_cycle("5 7 1 2 4 2 4 4 2 3 -2 1 3 3 3 4 -4 4 5 2 3 5 1"), 0)
        self.assertEqual(solve_negative_cycle("5 7 1 2 4 2 4 4 2 3 -2 1 3 3 3 4 -4 4 5 2 5 3 1"), 1)
        self.assertEqual(solve_negative_cycle("5 7 1 2 4 4 2 4 2 3 -2 1 3 3 3 4 -3 4 5 2 3 5 1"), 1)

    def test_shortest_paths(self):
        self.assertEqual(solve_shortest("6 7 1 2 10 2 3 5 1 3 100 3 5 7 5 4 10 4 3 -18 6 1 -1 1"),
                         "0\n10\n-\n-\n-\n*\n")
        self.assertEqual(solve_shortest("5 4 1 2 1 4 1 2 2 3 2 3 1 -5 4"),
                         "-\n-\n-\n0\n*\n")

    def test_clustering(self):
        self.assertAlmostEqual(solve_clustering("12 7 6 4 3 5 1 1 7 2 7 5 7 3 3 7 8 2 8 4 4 6 7 2 6 3"), 2.828427124746)
        self.assertAlmostEqual(solve_clustering("8 3 1 1 2 4 6 9 8 9 9 8 9 3 11 4 12 4"), 5.000000000)

    def test_connecting_points(self):
        self.assertAlmostEqual(solve_minimum_distance("4 0 0 0 1 1 0 1 1"), 3.0)
        self.assertAlmostEqual(solve_minimum_distance("5 0 0 0 2 1 1 3 0 3 2"), 7.064495102)

if __name__ == '__main__':
    unittest.main()
