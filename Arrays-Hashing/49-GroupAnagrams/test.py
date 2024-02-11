import unittest
from typing import List
from sol1 import Solution  # replace 'your_module' with the actual module name or file where the Solution class is defined

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_groupAnagrams_basic(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = self.solution.groupAnagrams(input_strs)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_groupAnagrams_empty_input(self):
        input_strs = []
        expected_output = []
        result = self.solution.groupAnagrams(input_strs)
        self.assertEqual(result, expected_output)

    def test_groupAnagrams_single_word(self):
        input_strs = ["hello"]
        expected_output = [["hello"]]
        result = self.solution.groupAnagrams(input_strs)
        self.assertEqual(result, expected_output)

    def test_groupAnagrams_duplicate_words(self):
        input_strs = ["listen", "silent", "enlist", "listen"]
        expected_output = [["listen", "silent", "enlist"]]
        result = self.solution.groupAnagrams(input_strs)
        self.assertEqual(result, expected_output)

    def test_groupAnagrams_mixed_case(self):
        input_strs = ["Tea", "eat", "TEA", "tan", "ATE", "bat"]
        expected_output = [["Tea", "eat", "TEA", "ATE"], ["tan"], ["bat"]]
        result = self.solution.groupAnagrams(input_strs)
        self.assertEqual(sorted(result), sorted(expected_output))

if __name__ == "__main__":
    unittest.main()