# 1
# class FileReader:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.file_name, 'r')
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()
#
# with FileReader('data.txt') as f:
#     for line in f:
#         print(line.strip())

# ---------------------------------------------------------------
# 1
import multiprocessing
#
# def sum_list(numbers):
#     result = 0
#     i = 0
#     while i < len(numbers):
#         result += numbers[i]
#         i += 1
#     return result
#
#
# if __name__ == '__main__':
#     numbers = [1, 2, 3, 4, 5]
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(sum_list, (numbers,))
#     print("Yig'indisi:", result)

# ----------------------------------------------------------------------------------
# 2
# def rotate_list(lst):
#     return lst[1:] + lst[:1]
#
#
# if __name__ == '__main__':
#     lst = [1, 2, 3, 4]
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(rotate_list, (lst,))
#     print("Aylantirilgan ro'yxat:", result)

# --------------------------------------------------------------------------
# 3
# def find_min_max(numbers):
#     return min(numbers), max(numbers)
#
#
# if __name__ == '__main__':
#     numbers = [1, 2, 3, 4, 5]
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_min_max, (numbers,))
#     print("Minimal va maksimal qiymatlar:", result)

# -------------------------------------------------------------------------
# 4
# def find_element(lst, element):
#     return element in lst
#
#
# if __name__ == '__main__':
#     lst = [1, 2, 3, 4, 5]
#     element = 3
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_element, (lst, element))
#     print(f"Element {element} mavjud:", result)

# ----------------------------------------------------------------
# 5
# def remove_duplicates(lst):
#     return list(set(lst))
#
#
# if __name__ == '__main__':
#     lst = [1, 2, 2, 3, 4, 4, 5]
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(remove_duplicates, (lst,))
#     print("Unikal elementlar:", result)

# --------------------------------------------------------
# 6
# def reverse_words(words):
#     return [word[::-1] for word in words]
#
#
# if __name__ == '__main__':
#     words = ['salom', 'dunyo', 'python']
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(reverse_words, (words,))
#     print("Teskari so'zlar:", result)

# ------------------------------------------------------------
# 7
# def find_longest_word(words):
#     return max(words, key=len)
#
#
# if __name__ == '__main__':
#     words = ['salom', 'dunyodagi', 'python']
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_longest_word, (words,))
#     print("Eng uzun so'z:", result)

# ------------------------------------------------------------------
# 8
# def find_duplicates(d):
#     values = list(d.values())
#     return {v for v in values if values.count(v) > 1}
#
#
# if __name__ == '__main__':
#     d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_duplicates, (d,))
#     print("Takrorlangan qiymatlar:", result)

# -----------------------------------------------------------------------
# 9
# def find_sort_numbers(d):
#     numbers = [v for v in d.values() if isinstance(v, (int, float))]
#     return sorted(numbers)
#
#
# if __name__ == '__main__':
#     d = {'a': 10, 'b': 'hello', 'c': 15, 'd': 5}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_sort_numbers, (d,))
#     print("Saralangan raqamlar:", result)

# --------------------------------------------------------------------------
# 10
# def multiply_numbers(d):
#     return {k: (v * 2 if isinstance(v, (int, float)) else v) for k, v in d.items()}
#
#
# if __name__ == '__main__':
#     d = {'a': 10, 'b': 'world', 'c': 15, 'd': 5}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(multiply_numbers, (d,))
#     print("Yangilangan lug‘at:", result)

# ----------------------------------------------------------------
# 11
# def find_key_with_max_value(d):
#     return max(d, key=d.get)
#
#
# if __name__ == '__main__':
#     d = {'a': 10, 'b': 25, 'c': 15}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_key_with_max_value, (d,))
#     print("Eng katta qiymatga ega kalit:", result)

# -----------------------------------------------------------
# 12
# def calculate_average(d):
#     values = [v for v in d.values() if isinstance(v, (int, float))]
#     return sum(values) / len(values) if values else None
#
#
# if __name__ == '__main__':
#     d = {'a': 10, 'b': 20, 'c': 30}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(calculate_average, (d,))
#     print("O‘rta arifmetik:", result)

# ---------------------------------------------------------------
# 13
# def merge_dicts(d1, d2):
#     result = d1.copy()
#     for key, value in d2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value
#     return result
#
#
# if __name__ == '__main__':
#     d1 = {'a': 10, 'b': 20}
#     d2 = {'b': 30, 'c': 40}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(merge_dicts, (d1, d2))
#     print("Birlashtirilgan lug‘at:", result)

# ----------------------------------------------------------------
# 14
# def find_shortest_longest_keys(d):
#     keys = d.keys()
#     shortest = min(keys, key=len)
#     longest = max(keys, key=len)
#     return shortest, longest
#
#
# if __name__ == '__main__':
#     d = {'a': 10, 'bb': 20, 'ccc': 30, 'dddd': 40}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(find_shortest_longest_keys, (d,))
#     print("Eng qisqa kalit:", result[0], "| Eng uzun kalit:", result[1])

# ---------------------------------------------
# 15
# def convert_numeric_strings(d):
#     return {k: (int(v) if str(v).isdigit() else v) for k, v in d.items()}
#
#
# if __name__ == '__main__':
#     d = {'a': '123', 'b': 'hello', 'c': 456}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(convert_numeric_strings, (d,))
#     print("Yangilangan lug‘at:", result)

# ----------------------------------------------
# 16
# def double_values(d):
#     return {k: (v * 2 if isinstance(v, (int, float)) else v) for k, v in d.items()}
#
#
# if __name__ == '__main__':
#     d = {'a': 5, 'b': 10, 'c': 'hello'}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(double_values, (d,))
#     print("2 ga ko‘paytirilgan yangi lug‘at:", result)

# ----------------------------------------------------
# 17
# def reverse_string_values(d):
#     return {k: (v[::-1] if isinstance(v, str) else v) for k, v in d.items()}
#
#
# if __name__ == '__main__':
#     d = {'a': 'hello', 'b': 123, 'c': 'world'}
#     with multiprocessing.Pool() as pool:
#         result = pool.apply(reverse_string_values, (d,))
#     print("Teskari string qiymatlar:", result)
