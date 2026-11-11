import itertools
import unittest

from solutions import (
    coin_change, course_schedule, edit_distance, n_queens, randomized_set,
    rotated_search, rotting_oranges, sliding_window_maximum, subarray_sum,
    three_sum, trapping_rain_water, tree_max_path,
)


class AlgorithmExamples(unittest.TestCase):
    def test_three_sum_deduplicates(self):
        self.assertEqual(three_sum.Solution().threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

    def test_rotated_search_hit_and_miss(self):
        search = rotated_search.Solution().search
        self.assertEqual(search([9, 13, 2, 5, 7], 5), 3)
        self.assertEqual(search([9, 13, 2, 5, 7], 8), -1)

    def test_randomized_set_repairs_swapped_index(self):
        values = randomized_set.RandomizedSet()
        for value in (11, 17, 23):
            self.assertTrue(values.insert(value))
        self.assertFalse(values.insert(23))
        self.assertTrue(values.remove(11))
        self.assertTrue(values.remove(23))
        self.assertEqual(values.getRandom(), 17)
        self.assertFalse(values.remove(11))

    def test_prefix_sum_with_negative_values(self):
        self.assertEqual(subarray_sum.Solution().subarraySum([2, -2, 2, -2], 0), 4)

    def test_rain_water_implementations(self):
        stack = trapping_rain_water.StackSolution().trap
        pointers = trapping_rain_water.TwoPointerSolution().trap
        for heights in itertools.product(range(3), repeat=5):
            expected = sum(min(max(heights[:i + 1]), max(heights[i:])) - h for i, h in enumerate(heights))
            self.assertEqual(stack(heights), expected)
            self.assertEqual(pointers(heights), expected)

    def test_window_implementations(self):
        heap = sliding_window_maximum.HeapSolution().maxSlidingWindow
        deque = sliding_window_maximum.max_sliding_window_deque
        for values in itertools.product(range(3), repeat=5):
            for width in range(1, len(values) + 1):
                expected = [max(values[i:i + width]) for i in range(len(values) - width + 1)]
                self.assertEqual(heap(values, width), expected)
                self.assertEqual(deque(values, width), expected)

    def test_tree_state_resets_between_calls(self):
        solve = tree_max_path.Solution().maxPathSum
        node = tree_max_path.TreeNode
        self.assertEqual(solve(node(4, node(7), node(3))), 14)
        self.assertEqual(solve(node(-6, node(-2), node(-8))), -2)

    def test_course_schedule_detects_cycles(self):
        can_finish = course_schedule.Solution().canFinish
        self.assertTrue(can_finish(4, [[2, 1], [3, 2]]))
        self.assertFalse(can_finish(4, [[2, 1], [3, 2], [1, 3]]))

    def test_multi_source_bfs_and_unreachable_cell(self):
        solve = rotting_oranges.Solution().orangesRotting
        self.assertEqual(solve([[2, 1, 1, 1, 2]]), 2)
        self.assertEqual(solve([[2, 0, 1]]), -1)

    def test_queens_results_do_not_mutate_on_next_call(self):
        solve = n_queens.Solution().solveNQueens
        boards = solve(4)
        self.assertEqual(len(boards), 2)
        self.assertEqual(solve(1), [["Q"]])
        self.assertEqual(len(boards), 2)
        for board in boards:
            columns = [row.index("Q") for row in board]
            self.assertEqual(len(set(columns)), 4)
            self.assertEqual(len({row - col for row, col in enumerate(columns)}), 4)
            self.assertEqual(len({row + col for row, col in enumerate(columns)}), 4)

    def test_coin_change_reuse_and_unreachable_amount(self):
        solve = coin_change.Solution().coinChange
        self.assertEqual(solve([4, 7], 12), 3)
        self.assertEqual(solve([4, 7], 6), -1)

    def test_edit_distance_and_empty_prefix(self):
        solve = edit_distance.Solution().minDistance
        self.assertEqual(solve("park", "spark"), 1)
        self.assertEqual(solve("pale", "bake"), 2)
        self.assertEqual(solve("", "tea"), 3)


if __name__ == "__main__":
    unittest.main()
