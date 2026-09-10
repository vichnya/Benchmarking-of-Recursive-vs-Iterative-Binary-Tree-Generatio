"""
Вариант 18: Root = 18; height = 5, 
left_leaf = (root-8)*3, 
right_leaf = (root+8)*2 
"""

def gen_bin_tree_recursive(height: int, root: int, left_leaf, right_leaf) -> dict:
  """ Функция по построению бинарного дерева - рекурсивная версия"""
  if height == 1:
    return {root: []}
  else:
    left = gen_bin_tree_recursive(height-1, left_leaf(root), left_leaf, right_leaf)
    right = gen_bin_tree_recursive(height-1, right_leaf(root), left_leaf, right_leaf)
    return {root: [left, right]}



def gen_bin_tree(height: int, root: int, left_leaf, right_leaf) -> dict:
  """Функция по построению бинарного дерева - нерекурсивная версия"""
  
  roots = [[root]] 

  for leaf in range(height - 1): 
      if (len(roots) == 1):
          r = roots[0]  
      else: 
          r = [item for s in roots[-1] for item in s] 

      leaves = list( 
          map(
              lambda root_value: [
                left_leaf(root_value),
                right_leaf(root_value)], r)) 

      roots.append(leaves)
  roots.reverse()

  if height == 1:
    tree = {root: []}
  else:
    roots[-1] = [roots[-1]]
    roots[0] = list(map(lambda x: [{
        x[0]: []
    }, {
        x[1]: []
    }], roots[0]))
  
    for i in range(height - 1):
        roots[i].reverse()
        sublist = roots[i]
        for j in range(len(sublist)):
            x = sublist.pop()
            roots[i + 1][j // 2][j % 2] = {roots[i + 1][j // 2][j % 2]: x}
    tree = roots[-1][0][0]

  return tree

def Run_func(args: str, number: int):
  """Функция по измерению времени выполнения функций gen_bin_tree_recursive и gen_bin_tree"""
  import timeit
  
  test1 = timeit.timeit(f'gen_bin_tree_recursive({args})', setup="from __main__ import gen_bin_tree_recursive", number = number)
  test2 = timeit.timeit(f'gen_bin_tree({args})', setup="from __main__ import gen_bin_tree", number = number)
  write_log(args, number, result1 = test1, result2 = test2)
  

def write_log(args, number, result1, result2, file = 'record.txt'):
  """Запись истории в лог-файл"""

  f = open(file, mode='a', errors='ignore')
  
  f.write(f'Аргументы: {args}\n')
  f.write(f'Количество итераций: {number}\n')
  f.write(f'Рукурсивная версия. Время выполнения: {result1}\n')
  f.write(f'Нерукурсивная версия. Время выполнения:  {result2}\n\n')
  
  f.close()
  
if __name__ == '__main__':
  print('Построение бинарного дерева\n')
  print(f'Рекурсивная версия:\n{gen_bin_tree_recursive(5, 18, lambda x: (x-8)*3, lambda x: (x+8)*2)}')
  print()
  print(f'Нерекурсивная версия:\n{gen_bin_tree(5, 18, lambda x: (x-8)*3, lambda x: (x+8)*2)}')

  step = 0
  stop = 10000
  while step <= stop:
    Run_func(args = 'height = 5, root = 18, left_leaf = lambda x: (x-8)*3, right_leaf = lambda x: (x+8)*2', number = step)
    step += 500