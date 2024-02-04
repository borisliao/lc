import pytest
import inspect
import solution_133


# @pytest.mark.timeout(3)
# @pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_133, predicate=inspect.isfunction)])
# def test_example_1(f):
#     """
#     ![https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)
#     Explanation: There are 4 nodes in the graph.

#     1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).

#     2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

#     3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).

#     4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
#     """
#     adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
#     output = [[2, 4], [1, 3], [2, 4], [1, 3]]

#     assert f(adjList) == output


# @pytest.mark.timeout(3)
# @pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_133, predicate=inspect.isfunction)])
# def test_example_2(f):
#     """
#     ![https://assets.leetcode.com/uploads/2020/01/07/graph.png](https://assets.leetcode.com/uploads/2020/01/07/graph.png)
#     Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

#     """
#     adjList = [[]]
#     output = [[]]

#     assert f(adjList) == output


# @pytest.mark.timeout(3)
# @pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_133, predicate=inspect.isfunction)])
# def test_example_3(f):
#     """
#     Explanation: This an empty graph, it does not have any nodes.
#     """
#     adjList = []
#     output = []

#     assert f(adjList) == output
