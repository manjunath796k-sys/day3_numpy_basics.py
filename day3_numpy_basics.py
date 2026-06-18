# DAY 3 - NUMPY BASICS

import numpy as np

# 1. ARRAYS VS PYTHON LISTS

print("\n===== ARRAYS VS PYTHON LISTS =====")

python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print("Python List :", python_list)
print("NumPy Array :", numpy_array)


# 2. CREATE 1D ARRAY

print("\n===== 1D ARRAY =====")

arr1 = np.arange(1, 21)

print("Array:", arr1)


# 3. EVEN INDEXED ELEMENTS

print("\n===== EVEN INDEXED ELEMENTS =====")

even_index = arr1[::2]

print(even_index)


# 4. CREATE 3x3 ARRAY

print("\n===== 3x3 ARRAY =====")

arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr2)

print("Sum:", np.sum(arr2))
print("Mean:", np.mean(arr2))
print("Std:", np.std(arr2))


# 5. RESHAPE ARRAY

print("\n===== RESHAPE =====")

arr3 = np.arange(1,13)

reshape_array = arr3.reshape(3,4)

print(reshape_array)


# 6. CREATE RANDOM 5x5 ARRAY

print("\n===== RANDOM 5x5 ARRAY =====")

random_array = np.random.randn(5,5)

print(random_array)


# 7. ROW-WISE & COLUMN-WISE MEAN

print("\n===== ROW MEAN =====")

row_mean = np.mean(random_array, axis=1)
print(row_mean)

print("\n===== COLUMN MEAN =====")

column_mean = np.mean(random_array, axis=0)
print(column_mean)


# 8. NORMALIZATION (0 TO 1)

print("\n===== NORMALIZED ARRAY =====")

normalized = (
    (random_array - random_array.min())
    /
    (random_array.max() - random_array.min())
)

print(normalized)


# 9. REPLACE NEGATIVE VALUES WITH 0

print("\n===== NEGATIVE VALUES REPLACED =====")

positive_array = np.where(random_array < 0, 0, random_array)

print(positive_array)


# 10. BROADCASTING

print("\n===== BROADCASTING =====")

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Original Matrix")
print(matrix)

print("\nAdd Scalar 10")

print(matrix + 10)

vector = np.array([10,20,30])

print("\nAdd 1D Array")

print(matrix + vector)


# 11. ELEMENT-WISE OPERATIONS

print("\n===== ELEMENT WISE OPERATIONS =====")

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print("Addition")
print(a + b)

print("Subtraction")
print(a - b)

print("Multiplication")
print(a * b)


# 12. NP.WHERE() THRESHOLD

print("\n===== NP.WHERE THRESHOLD =====")

scores = np.array([45,60,75,30,90])

result = np.where(scores > 50,
                  "Pass",
                  "Fail")

print(result)


# 13. MAX, MIN & POSITIONS

print("\n===== MAX MIN POSITION =====")

sample = np.array([
    [15,45,12],
    [78,22,10],
    [5,90,33]
])

print(sample)

print("Maximum Value:", np.max(sample))
print("Minimum Value:", np.min(sample))

print("Max Position:",
      np.unravel_index(
          np.argmax(sample),
          sample.shape
      ))

print("Min Position:",
      np.unravel_index(
          np.argmin(sample),
          sample.shape
      ))


print("\n===== TASK COMPLETED =====")