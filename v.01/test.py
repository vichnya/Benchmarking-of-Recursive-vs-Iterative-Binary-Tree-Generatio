from math import factorial
from main import (
  my_factorial, 
  my_factorial2, 
  gen_bin_tree
)


def test_factorial_recursive():
  """Тест факториала - рекурсивная версия"""
  assert factorial(5) == my_factorial(5), "тест факториала со значением 5"

def test_factorial_non_recursive():
  """Тест факториала - нерекурсивная версия"""
  assert factorial(10) == my_factorial2(10), "тест нерекурсивной версии факториала"

def test_binary_tree_1():
  """Тест построения бинарного дерева - 1"""
  assert gen_bin_tree(height=1, root=18) == {18: []}, 'для высоты 1'

def test_binary_tree_2():
  """Тест построения бинарного дерева - 2"""
  assert gen_bin_tree(height=2, root=18) == {
    18: [{
      30: []
    }, {
      52: []
    }]
  }, 'для высоты 2'
def test_binary_tree_5():
  """Тест построения бинарного дерева - 3"""
  tree_5 = {
    18: [{
      30: [{
        66: [{
          174: [{
            498: []
          }, {
            364: []
          }]
        }, {
          148: [{
            420: []
          }, {
            312: []
          }]
        }]
      }, {
        76: [{
          204: [{
            588: []}, {
            424: []
          }]
        }, {
          168: [{
            480: []
          }, {
            352: []
          }]
        }]
      }]
    }, {
      52: [{
        132: [{
          372: [{
            1092: []
          }, {
            760: []
          }]
        }, {
          280: [{
            816: []
          }, {
            576: []
          }]
        }]
      }, {
        120: [{
          336: [{
            984: []
          }, {
            688: []
          }]
        }, {
          256: [{
            744: []
          }, {
            528: []
          }]
        }]
      }]
    }]
  }
  assert gen_bin_tree(height=5, root=18) == tree_5, 'для высоты 5'

def all_tests():
  test_factorial_recursive()
  test_factorial_non_recursive()

  test_binary_tree_1()
  test_binary_tree_2()
  test_binary_tree_5()


  