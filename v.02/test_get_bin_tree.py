#запуск: python3 -m unittest -v test_get_bin_tree.py

import unittest
from main import gen_bin_tree, gen_bin_tree_recursive


class TestBinTreeGeneration(unittest.TestCase):
  def test_simple_case_recursive(self):
    """Тест на рекурсивную функцию - предложенный"""
    self.assertEqual(gen_bin_tree_recursive(2, 5, lambda x: x + 3, lambda x: x * 2), {5: [{8: []}, {10: []}]})
  def test_simple_case_non_recursive(self):
    """Тест на нерекурсивную функцию - предложенный"""
    self.assertEqual(gen_bin_tree(2, 5, lambda x: x + 3, lambda x: x * 2), {5: [{8: []}, {10: []}]})

  def test_limit_values_recursive(self):
    """Тест на граничные значения - рекурсивная функция"""
    self.assertEqual(gen_bin_tree_recursive(1, 5, lambda x: x + 3, lambda x: x * 2), {5: []})
  def test_limit_values_non_recursive(self):
    """Тест на граничные значения - нерекурсивная версия"""
    self.assertEqual(gen_bin_tree(1, 5, lambda x: x + 3, lambda x: x * 2), {5: []})

  def test_error_recursive(self):
    """Тест на неподходящие значения - рекурсивная версия"""
    with self.assertRaisesRegex(RecursionError, 'maximum recursion depth exceeded in comparison'):
      gen_bin_tree_recursive(0, 5, lambda x: x + 3, lambda x: x * 2)
  def test_error_non_recursive(self):
    """Тест на неподходящие значения - нерекурсивная версия"""
    with self.assertRaisesRegex(IndexError, 'list index out of range'):
      gen_bin_tree(0, 5, lambda x: x + 3, lambda x: x * 2)