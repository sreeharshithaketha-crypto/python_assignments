# 1. Install NumPy and import it using the alias np.
import numpy as np

print("1. NumPy is ready:", np.__version__)

# 2. Create a NumPy array from the list [10, 20, 30, 40, 50].
numbers = np.array([10, 20, 30, 40, 50])
print("2.", numbers)

# 3. Print the type of a NumPy array.
print("3.", type(numbers))

# 4. Print the data type (dtype) of an array.
print("4.", numbers.dtype)

# 5. Find the number of dimensions of an array using ndim.
print("5.", numbers.ndim)

# 6. Find the shape of a 1D array.
print("6.", numbers.shape)

# 7. Find the total number of elements using size.
print("7.", numbers.size)

# 8. Create an array containing numbers from 1 to 10.
print("8.", np.arange(1, 11))

# 9. Create an array of ten zeros.
print("9.", np.zeros(10))

# 10. Create an array of ten ones.
print("10.", np.ones(10))

# 11. Create an array containing five 7s.
print("11.", np.full(5, 7))

# 12. Create an array containing numbers from 0 to 20 using arange().
print("12.", np.arange(0, 21))

# 13. Create an array of even numbers from 2 to 20.
print("13.", np.arange(2, 21, 2))

# 14. Create an array of odd numbers from 1 to 19.
print("14.", np.arange(1, 20, 2))

# 15. Create five equally spaced numbers between 0 and 1 using linspace().
print("15.", np.linspace(0, 1, 5))

# 16. Create a 3×3 matrix containing zeros.
print("16.\n", np.zeros((3, 3)))

# 17. Create a 3×3 matrix containing ones.
print("17.\n", np.ones((3, 3)))

# 18. Create a 4×4 identity matrix.
print("18.\n", np.eye(4))

# 19. Create a 2D array from a nested Python list.
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("19.\n", matrix)

# 20. Access the first element of a NumPy array.
print("20.", numbers[0])

# 21. Access the last element using negative indexing.
print("21.", numbers[-1])

# 22. Access the second row of a 2D array.
print("22.", matrix[1])

# 23. Access the third column of a 2D array.
print("23.", matrix[:, 2])

# 24. Use slicing to extract the first three elements.
print("24.", numbers[:3])

# 25. Reverse a NumPy array using slicing.
print("25.", numbers[::-1])

# 26. Add two NumPy arrays element by element.
left = np.array([2, 4, 6])
right = np.array([1, 3, 5])
print("26.", left + right)

# 27. Subtract two NumPy arrays element by element.
print("27.", left - right)

# 28. Multiply two NumPy arrays element by element.
print("28.", left * right)

# 29. Divide two NumPy arrays element by element.
print("29.", left / right)

# 30. Calculate the square of every array element.
print("30.", left**2)

# 31. Calculate the cube of every array element.
print("31.", left**3)

# 32. Find the sum of all elements.
print("32.", numbers.sum())

# 33. Find the mean of an array.
print("33.", numbers.mean())

# 34. Find the median of an array.
print("34.", np.median(numbers))

# 35. Find the minimum value.
print("35.", numbers.min())

# 36. Find the maximum value.
print("36.", numbers.max())

# 37. Find the standard deviation.
print("37.", numbers.std())

# 38. Find the variance.
print("38.", numbers.var())

# 39. Find the cumulative sum.
print("39.", np.cumsum(numbers))

# 40. Find the cumulative product.
print("40.", np.cumprod(np.array([1, 2, 3, 4])))

# 41. Calculate the absolute value of negative numbers.
print("41.", np.abs(np.array([-5, -2, 0, 3])))

# 42. Round floating-point values to two decimal places.
print("42.", np.round(np.array([1.234, 5.678, 9.876]), 2))

# 43. Find the index of the maximum value using argmax().
print("43.", numbers.argmax())

# 44. Find the index of the minimum value using argmin().
print("44.", numbers.argmin())

# 45. Count values greater than 50.
more_numbers = np.array([10, 60, 30, 80, 50, 100])
print("45.", np.count_nonzero(more_numbers > 50))

# 46. Count even numbers in an array.
print("46.", np.count_nonzero(numbers % 2 == 0))

# 47. Find all numbers divisible by 5.
print("47.", numbers[numbers % 5 == 0])

# 48. Replace all negative values with 0.
some_numbers = np.array([-4, 3, -2, 8])
print("48.", np.where(some_numbers < 0, 0, some_numbers))

# 49. Replace all values greater than 100 with 100.
big_numbers = np.array([50, 120, 90, 150])
print("49.", np.minimum(big_numbers, 100))

# 50. Calculate the percentage contribution of each value to the total.
percent_numbers = np.array([10, 20, 30])
print("50.", percent_numbers / percent_numbers.sum() * 100)

# 51. Reshape an array of 12 elements into a 3×4 matrix.
print("51.\n", np.arange(1, 13).reshape(3, 4))

# 52. Reshape an array of 16 elements into a 4×4 matrix.
print("52.\n", np.arange(1, 17).reshape(4, 4))

# 53. Convert a 2D array into a 1D array using flatten().
small_matrix = np.array([[1, 2], [3, 4]])
print("53.", small_matrix.flatten())

# 54. Convert a 2D array into a 1D array using ravel().
print("54.", small_matrix.ravel())

# 55. Transpose a 2D matrix.
print("55.\n", small_matrix.T)

# 56. Swap the first and last rows of a matrix.
row_swap = np.arange(1, 10).reshape(3, 3)
row_swap[[0, -1]] = row_swap[[-1, 0]]
print("56.\n", row_swap)

# 57. Swap the first and last columns of a matrix.
column_swap = np.arange(1, 10).reshape(3, 3)
column_swap[:, [0, -1]] = column_swap[:, [-1, 0]]
print("57.\n", column_swap)

# 58. Extract a 2×2 sub-matrix from a 4×4 matrix.
four_matrix = np.arange(1, 17).reshape(4, 4)
print("58.\n", four_matrix[1:3, 1:3])

# 59. Extract all elements from the second row onward.
print("59.\n", four_matrix[1:, :])

# 60. Extract all elements from the third column onward.
print("60.\n", four_matrix[:, 2:])

# 61. Use boolean indexing to find values greater than 50.
filter_numbers = np.array([10, 55, 70, 30, 90])
print("61.", filter_numbers[filter_numbers > 50])

# 62. Use boolean indexing to find values between 20 and 80.
print("62.", filter_numbers[(filter_numbers >= 20) & (filter_numbers <= 80)])

# 63. Find all even values using boolean indexing.
print("63.", filter_numbers[filter_numbers % 2 == 0])

# 64. Find all odd values using boolean indexing.
print("64.", filter_numbers[filter_numbers % 2 != 0])

# 65. Replace even values with 0 using boolean indexing.
even_replaced = filter_numbers.copy()
even_replaced[even_replaced % 2 == 0] = 0
print("65.", even_replaced)

# 66. Replace values below the mean with the mean.
mean_replaced = filter_numbers.copy()
mean_replaced[mean_replaced < mean_replaced.mean()] = mean_replaced.mean()
print("66.", mean_replaced)

# 67. Sort a NumPy array.
print("67.", np.sort(np.array([5, 2, 8, 1, 3])))

# 68. Sort each row of a 2D array.
unsorted_matrix = np.array([[3, 1, 2], [9, 7, 8]])
print("68.\n", np.sort(unsorted_matrix, axis=1))

# 69. Sort each column of a 2D array.
print("69.\n", np.sort(unsorted_matrix, axis=0))

# 70. Find unique values in an array.
print("70.", np.unique(np.array([1, 2, 2, 3, 3, 3])))

# 71. Concatenate two NumPy arrays using concatenate().
print("71.", np.concatenate((np.array([1, 2]), np.array([3, 4]))))

# 72. Stack two arrays vertically using vstack().
print("72.\n", np.vstack((np.array([1, 2]), np.array([3, 4]))))

# 73. Stack two arrays horizontally using hstack().
print("73.", np.hstack((np.array([1, 2]), np.array([3, 4]))))

# 74. Split an array into three equal parts.
print("74.", np.split(np.arange(1, 10), 3))

# 75. Split a 2D matrix into two vertical sections (left and right).
print("75.", np.hsplit(np.arange(1, 17).reshape(4, 4), 2))

# 76. Split a 2D matrix into two horizontal sections (top and bottom).
print("76.", np.vsplit(np.arange(1, 17).reshape(4, 4), 2))

# 77. Perform matrix addition on two 3×3 matrices.
first_matrix = np.ones((3, 3), dtype=int)
second_matrix = np.full((3, 3), 2)
print("77.\n", first_matrix + second_matrix)

# 78. Perform matrix multiplication on two matrices.
print("78.\n", np.array([[1, 2], [3, 4]]) @ np.array([[5, 6], [7, 8]]))

# 79. Calculate the transpose of a matrix and verify its shape.
transposed = matrix.T
print("79.\n", transposed)
print("   Shape:", transposed.shape)

# 80. Calculate the determinant of a 2×2 matrix using np.linalg.det().
print("80.", np.linalg.det(np.array([[1, 2], [3, 4]])))

# 81. Calculate the inverse of a matrix using np.linalg.inv().
print("81.\n", np.linalg.inv(np.array([[1, 2], [3, 4]])))

# 82. Solve a system of linear equations using np.linalg.solve().
# These equations are x + y = 5 and 2x + y = 8.
answer_xy = np.linalg.solve(np.array([[1, 1], [2, 1]]), np.array([5, 8]))
print("82. x and y:", answer_xy)

# 83. Calculate dot product of two vectors.
print("83.", np.dot(np.array([1, 2, 3]), np.array([4, 5, 6])))

# 84. Calculate the Euclidean norm of a vector.
print("84.", np.linalg.norm(np.array([3, 4])))

# 85. Normalize an array so its values range from 0 to 1.
normalize_me = np.array([10, 20, 30, 40])
normalized = (normalize_me - normalize_me.min()) / (
    normalize_me.max() - normalize_me.min()
)
print("85.", normalized)

# 86. Find the second-largest unique value in a NumPy array.
unique_numbers = np.unique(np.array([8, 2, 8, 5, 3]))
print("86.", np.sort(unique_numbers)[-2])

# 87. Find the third-largest value without sorting the entire array.
rank_numbers = np.array([8, 2, 10, 5, 3, 7])
print("87.", np.partition(rank_numbers, -3)[-3])

# 88. Find duplicate values in a NumPy array.
duplicate_numbers, duplicate_counts = np.unique(
    np.array([1, 2, 2, 3, 4, 4, 4]), return_counts=True
)
print("88.", duplicate_numbers[duplicate_counts > 1])

# 89. Find values that occur exactly once.
print("89.", duplicate_numbers[duplicate_counts == 1])

# 90. Find the frequency of every unique value.
print("90. Values:", duplicate_numbers)
print("    Counts:", duplicate_counts)

# 91. Find the row with the highest sum in a 2D array.
score_matrix = np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])
best_row = score_matrix.sum(axis=1).argmax()
print("91. Row index:", best_row, "Row:", score_matrix[best_row])

# 92. Find the column with the lowest average in a 2D array.
lowest_column = score_matrix.mean(axis=0).argmin()
print("92. Column index:", lowest_column, "Average:", score_matrix.mean(axis=0)[lowest_column])

# 93. Find the top 3 values and their indexes.
top_array = np.array([12, 50, 7, 40, 30])
top_indexes = np.argpartition(top_array, -3)[-3:]
top_indexes = top_indexes[np.argsort(top_array[top_indexes])[::-1]]
print("93. Values:", top_array[top_indexes], "Indexes:", top_indexes)

# 94. Find all values that are above the array's mean.
print("94.", top_array[top_array > top_array.mean()])

# 95. Find the percentage of missing values represented by NaN.
nan_array = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
nan_percent = np.isnan(nan_array).sum() / nan_array.size * 100
print("95.", nan_percent, "%")

# 96. Replace NaN values with the mean of the array.
nan_mean = np.nanmean(nan_array)
filled_array = np.where(np.isnan(nan_array), nan_mean, nan_array)
print("96.", filled_array)

# 97. Remove rows containing NaN values from a 2D array.
nan_matrix = np.array([[1.0, 2.0], [np.nan, 4.0], [5.0, 6.0]])
print("97.\n", nan_matrix[~np.isnan(nan_matrix).any(axis=1)])

# 98. Calculate row-wise and column-wise mean for a matrix.
mean_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("98. Row means:", mean_matrix.mean(axis=1))
print("    Column means:", mean_matrix.mean(axis=0))

# 99. Create a 10×10 random matrix and find its minimum, maximum, mean, and standard deviation.
random_matrix = np.random.default_rng(1).random((10, 10))
print("99. Minimum:", random_matrix.min())
print("    Maximum:", random_matrix.max())
print("    Mean:", random_matrix.mean())
print("    Standard deviation:", random_matrix.std())

# 100. Final Challenge: Build a NumPy Student Marks Analyzer.
# Pass rule: a student's average is at least 40. Grades use average marks:
# A is 90+, B is 80+, C is 70+, D is 40+, and F is below 40.
student_names = np.array(["Asha", "Ben", "Cleo", "Dev", "Eli"])
student_marks = np.array(
    [
        [90, 85, 95],
        [70, 75, 80],
        [35, 40, 45],
        [60, 55, 65],
        [20, 25, 30],
    ]
)
student_totals = student_marks.sum(axis=1)
student_averages = student_marks.mean(axis=1)
subject_averages = student_marks.mean(axis=0)
highest_student = student_averages.argmax()
lowest_student = student_averages.argmin()
passed = student_averages >= 40
student_grades = np.select(
    [
        student_averages >= 90,
        student_averages >= 80,
        student_averages >= 70,
        student_averages >= 40,
    ],
    ["A", "B", "C", "D"],
    default="F",
)
student_ranks = (student_averages[:, None] < student_averages).sum(axis=1) + 1
above_class_average = student_averages > student_averages.mean()

print("100. Total marks:", student_totals)
print("     Average marks:", student_averages)
print("     Highest scorer:", student_names[highest_student])
print("     Lowest scorer:", student_names[lowest_student])
print("     Subject averages:", subject_averages)
print("     Pass count:", np.count_nonzero(passed))
print("     Fail count:", np.count_nonzero(~passed))
print("     Grades:", student_grades)
print("     Ranks:", student_ranks)
print("     Above class average:", student_names[above_class_average])
