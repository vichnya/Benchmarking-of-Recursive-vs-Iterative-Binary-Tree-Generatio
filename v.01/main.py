"""
Вариант 18: Root = 18; height = 5, 
left_leaf = (root-8)*3, 
right_leaf = (root+8)*2
"""

def my_factorial(n: int) -> int:
  """Функция по нахождению факториала - рекурсивная версия"""
  if n == 0:
      return 1
  return n * my_factorial(n - 1)


def my_factorial2(n: int) -> int:
  """Функция по нахождению факториала - нерекурсивная версия"""
  res = 1
  for i in range(1, n + 1):
      res *= i  
  return res


def gen_bin_tree(height: int, root: int) -> dict:
  """ Функция по построению бинарного дерева - рекурсивная версия"""
  if height == 1:
    return {root:[]}
  else:
    left_leaf = (root-8)*3
    right_leaf = (root+8)*2
    left = gen_bin_tree(height-1, left_leaf)
    right = gen_bin_tree(height-1, right_leaf)
    return {root: [left, right]}
    


def main():
  if __name__ == '__main__':
    from test import all_tests
    all_tests()
    print(gen_bin_tree(2,18))

main()



