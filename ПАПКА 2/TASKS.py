import numpy as np
import random


print("=============================ЗАДАЧА 1=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

sum_cols = np.sum(np.absolute(A), axis=0)

max_sum = np.max(sum_cols)
max_sum_col = np.argmax(sum_cols)
col = A[:, max_sum_col]
max_el = np.max(col)
print("Наибольший элемент: {}".format(max_el))

print("=============================ЗАДАЧА 2=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

average = np.average(A, axis=1)
max_average = np.max(average)

print("Наибольшее среднее значение: {}".format(max_average))

print("=============================ЗАДАЧА 3=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

sum_cols = np.sum(np.absolute(A), axis=0)
max_sum = np.max(sum_cols)
max_sum_col = np.argmax(sum_cols)
col = A[:, max_sum_col]
min_el = np.min(col)

print("Наименьший элемент: {}".format(min_el))

print("=============================ЗАДАЧА 4=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

average = np.average(A, axis=1)
min_average = np.min(average)

print("Наименьшее среднее значение: {}".format(min_average))

print("=============================ЗАДАЧА 5=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

average_rows = np.average(A, axis=1)
average_cols = np.average(A, axis=0)
A = np.vstack((A, [average_cols]))
A = np.column_stack((A, np.append(average_rows, 0)))

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 6=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

sum_elements = np.sum(A)
sum_cols = np.sum(A, axis=0)
A = np.vstack((A, [sum_cols/sum_elements]))

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 7=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

sum_elements = np.sum(A)
sum_cols = np.sum(A, axis=1)
A = np.column_stack((A, sum_cols/sum_elements))

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 8=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A < 0
num_cols = np.sum(A_bool, axis=0)
num_rows = np.sum(A_bool, axis=1)
A = np.vstack((A, [num_cols]))
A = np.column_stack((A, np.append(num_rows, 0)))

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 9=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A_slice = A[:L, :K]
slice_bool = A_slice == 0
count_zero_elements = slice_bool.sum()

print("Количество нулевых элементов в срезе: {}".format(count_zero_elements))

print("=============================ЗАДАЧА 10=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

col = A[:, K]
col = col.reshape(len(col), 1)
A = A * col

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 11=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A = A + A[L]
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 12=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

row_max = np.max(A, axis=1)
A = A / row_max.reshape(len(row_max), 1)

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 13=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

col_max = np.max(A, axis=0)
A = A / col_max

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 14=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

max_el = np.max(A)
A = A / max_el

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 15=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
H = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A == H
row_sum = np.sum(A_bool, axis=0)

print("Столбцы в которых встречается значение {}:".format(H))
print(np.argwhere(row_sum).flatten())

print("Столбцы в которых нет значения {}:".format(H))
print(np.argwhere(row_sum == 0).flatten())

print("=============================ЗАДАЧА 16=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A = np.delete(A, L, axis=0)
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 17=============================")


N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

row = np.random.randint(-9, 10, M)
A = np.insert(A, L, row, axis=0)
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 18=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

diagonal_main = np.diagonal(A)
sum_diagonal_main = np.sum(diagonal_main)
print("Cумма элементов главной диагонали:\r\n{}".format(sum_diagonal_main))

diagonal_side = np.diagonal(A[::-1])
sum_diagonal_side = np.sum(diagonal_side)
print("сумму элементов побочной диагонали:\r\n{}".format(sum_diagonal_side))

print("=============================ЗАДАЧА 19=============================")

N = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, N))
print("Матрица:\r\n{}".format(A))

diagonal_elements = np.array([np.diagonal(A, i) for i in [1, -1]]).flatten()
print("Элементы, расположенные параллельно главной диагонали:")
print(diagonal_elements)

print("Сумма элементов, расположенные параллельно главной диагонали:")
print(np.sum(diagonal_elements))

print("=============================ЗАДАЧА 20=============================")

N = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, N))
print("Матрица:\r\n{}".format(A))

diagonal_elements = np.array([np.diagonal(A[::-1], i) for i in [1, -1]]).flatten()

print("Сумма элементов, расположенные параллельно побочной диагонали:")
print(np.prod(diagonal_elements))

print("=============================ЗАДАЧА 21=============================")

N = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, N))
print("Матрица:\r\n{}".format(A))

diagonal_elements = [np.diagonal(A, i) for i in [1, -1]]
values = (diagonal_elements[0] + diagonal_elements[1])/2
rng = np.arange(N-1)
A[rng, rng+1] = values[rng]
A[rng+1, rng] = values[rng]

print("Полученная матрица:\r\n{}".format(A))

print("=============================ЗАДАЧА 22=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(0, 2, (N, M))
print("Матрица:\r\n{}".format(A))

col = [i % 2 for i in np.sum(A, axis=1)]

A = np.insert(A, M, col, axis=1)
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 23=============================")

N = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, N))
print("Матрица:\r\n{}".format(A))

elements = np.diagonal(A, 1)
print("Сумма элементов, расположенных выше главной диагонали:")
print(np.sum(elements))

elements = np.diagonal(A[::-1], -1)
print("Произведение элементов, расположенных выше побочной диагонали:")
print(np.prod(elements))

print("=============================ЗАДАЧА 24=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],
]

for i in range(len(parts)):
    print("Cумма элементов {} части: {}".format(i+1, np.sum(parts[i])))

print("=============================ЗАДАЧА 25=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A == 0
col = np.sum(A_bool, axis=1)
A = np.insert(A, M, col, axis=1)
row = np.append(np.sum(A_bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)

print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 26=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
L = random.randint(1, 5)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],
]

for i in range(len(parts)):
    print("Cреднее арифметическое {} части: {}".format(i+1, np.average(parts[i])))

print("=============================ЗАДАЧА 27=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
H = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A == H
col_sum = np.sum(A_bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())

print("=============================ЗАДАЧА 28=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A = np.delete(A, K, axis=1)
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 29=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)
K = random.randint(1, 5)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

col = np.random.randint(-9, 10, N)
print("Столбец для вставки: {}".format(col))

A = np.insert(A, K, col, axis=1)
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 30=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

row = np.sum(A, axis=0) * -1

A = np.insert(A, N, row, axis=0)
print("Полученная матрица:\r\n {}".format(A))

print("=============================ЗАДАЧА 31=============================")

N = random.randint(5, 10)
M = random.randint(5, 10)

A = np.random.randint(-10, 10, (N, M))
print("Матрица:\r\n{}".format(A))

col = np.sum(A, axis=1) * -1

A = np.insert(A, M, col, axis=1)
print("Полученная матрица:\r\n {}".format(A))