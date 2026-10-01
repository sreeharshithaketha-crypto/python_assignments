# 1. Create a list of 10 integers and print all elements.
def q01_numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Create a list of 5 names and print the first and last element.
def q02_first_and_last(names):
    return names[0], names[-1]

# 3. Find the length of a list without using len().
def q03_length(items):
    count = 0
    for item in items:
        count += 1
    return count

# 4. Find the largest number in a list without using max().
def q04_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# 5. Find the smallest number in a list without using min().
def q05_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

# 6. Calculate the sum of all numbers without using sum().
def q06_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# 7. Count how many times a given number occurs in a list.
def q07_count_number(numbers, wanted):
    count = 0
    for number in numbers:
        if number == wanted:
            count += 1
    return count

# 8. Check whether a given element exists in a list.
def q08_contains(items, wanted):
    for item in items:
        if item == wanted:
            return True
    return False

# 9. Print all elements of a list using a for loop.
def q09_print_items(items):
    for item in items:
        print(item)

# 10. Print all elements of a list in reverse order.
def q10_print_backwards(items):
    for item in items[::-1]:
        print(item)

# 11. Print only even numbers from a list.
def q11_evens(numbers):
    return [number for number in numbers if number % 2 == 0]

# 12. Print only odd numbers from a list.
def q12_odds(numbers):
    return [number for number in numbers if number % 2 != 0]

# 13. Create a new list containing squares of all numbers.
def q13_squares(numbers):
    return [number * number for number in numbers]

# 14. Create a new list containing cubes of all numbers.
def q14_cubes(numbers):
    return [number * number * number for number in numbers]

# 15. Find the average of numbers in a list.
def q15_average(numbers):
    return q06_total(numbers) / q03_length(numbers)

# 16. Count positive, negative, and zero values.
def q16_count_signs(numbers):
    positive = negative = zero = 0
    for number in numbers:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1
    return positive, negative, zero

# 17. Find the second-largest different number in a list.
def q17_second_largest(numbers):
    ordered = sorted(numbers)
    different = []
    for number in ordered:
        if number not in different:
            different.append(number)
    return different[-2]

# 18. Find the second-smallest different number in a list.
def q18_second_smallest(numbers):
    ordered = sorted(numbers)
    different = []
    for number in ordered:
        if number not in different:
            different.append(number)
    return different[1]

# 19. Swap the first and last elements of a list.
def q19_swap_ends(items):
    result = items[:]
    result[0], result[-1] = result[-1], result[0]
    return result

# 20. Copy one list into another without using copy().
def q20_copy_list(items):
    result = []
    for item in items:
        result.append(item)
    return result

# 21. Add an element to the end of a list using append().
def q21_append(items, item):
    items.append(item)
    return items

# 22. Add multiple elements using extend().
def q22_extend(items, more_items):
    items.extend(more_items)
    return items

# 23. Insert an element at the 3rd position.
def q23_insert_third(items, item):
    items.insert(2, item)
    return items

# 24. Remove a specific element using remove().
def q24_remove(items, item):
    items.remove(item)
    return items

# 25. Remove the last element using pop().
def q25_pop_last(items):
    items.pop()
    return items

# 26. Remove an element at a specific index using pop().
def q26_pop_index(items, index):
    items.pop(index)
    return items

# 27. Delete an element using del.
def q27_delete_index(items, index):
    del items[index]
    return items

# 28. Empty a list using clear().
def q28_clear(items):
    items.clear()
    return items

# 29. Find the index of a given element.
def q29_find_index(items, wanted):
    return items.index(wanted)

# 30. Count occurrences of a particular element.
def q30_count(items, wanted):
    return items.count(wanted)

# 31. Sort a list in ascending order.
def q31_sort_ascending(items):
    items.sort()
    return items

# 32. Sort a list in descending order.
def q32_sort_descending(items):
    items.sort(reverse=True)
    return items

# 33. Reverse a list using reverse().
def q33_reverse(items):
    items.reverse()
    return items

# 34. Create a sorted copy without changing the original list.
def q34_sorted_copy(items):
    return sorted(items)

# 35. Add five user-entered values to an empty list.
def q35_five_values(values=None):
    if values is None:
        values = []
        for number in range(5):
            values.append(input("Enter a value: "))
    return values

# 36. Remove all occurrences of a particular number.
def q36_remove_all(numbers, wanted):
    return [number for number in numbers if number != wanted]

# 37. Replace all occurrences of one value with another.
def q37_replace_all(items, old_value, new_value):
    return [new_value if item == old_value else item for item in items]

# 38. Insert an element after every occurrence of a particular value.
def q38_insert_after(items, wanted, new_item):
    result = []
    for item in items:
        result.append(item)
        if item == wanted:
            result.append(new_item)
    return result

# 39. Find the frequency of every element in a list.
def q39_frequencies(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

# 40. Check whether two lists contain the same elements and counts.
def q40_same_elements(first, second):
    if len(first) != len(second):
        return False
    for item in first:
        if first.count(item) != second.count(item):
            return False
    return True

# 41. Print the first 5 elements using slicing.
def q41_first_five(items):
    return items[:5]

# 42. Print the last 5 elements using slicing.
def q42_last_five(items):
    return items[-5:]

# 43. Print elements from index 2 to 7.
def q43_indexes_two_to_seven(items):
    return items[2:8]

# 44. Print every second element.
def q44_every_second(items):
    return items[::2]

# 45. Print every third element.
def q45_every_third(items):
    return items[::3]

# 46. Reverse a list using slicing.
def q46_reverse_slice(items):
    return items[::-1]

# 47. Copy a list using slicing.
def q47_copy_slice(items):
    return items[:]

# 48. Remove the first three elements using slicing.
def q48_remove_first_three(items):
    return items[3:]

# 49. Remove the last three elements using slicing.
def q49_remove_last_three(items):
    return items[:-3]

# 50. Replace the middle element or elements using slicing.
def q50_replace_middle(items, replacements):
    middle = len(items) // 2
    if len(items) % 2 == 0:
        start = middle - 1
        end = middle + 1
    else:
        start = middle
        end = middle + 1
    return items[:start] + replacements + items[end:]

# 51. Extract all even-indexed elements.
def q51_even_indexes(items):
    return items[::2]

# 52. Extract all odd-indexed elements.
def q52_odd_indexes(items):
    return items[1::2]

# 53. Split a list into two nearly equal halves.
def q53_two_halves(items):
    middle = (len(items) + 1) // 2
    return items[:middle], items[middle:]

# 54. Rotate a list left by 2 positions using slicing.
def q54_rotate_left_two(items):
    if not items:
        return []
    steps = 2 % len(items)
    return items[steps:] + items[:steps]

# 55. Rotate a list right by 3 positions using slicing.
def q55_rotate_right_three(items):
    if not items:
        return []
    steps = 3 % len(items)
    return items[-steps:] + items[:-steps] if steps else items[:]

# 56. Generate numbers from 1 to 50 using list comprehension.
def q56_numbers_one_to_fifty():
    return [number for number in range(1, 51)]

# 57. Generate squares from 1 to 20.
def q57_squares_one_to_twenty():
    return [number * number for number in range(1, 21)]

# 58. Generate cubes from 1 to 20.
def q58_cubes_one_to_twenty():
    return [number ** 3 for number in range(1, 21)]

# 59. Generate only even numbers from 1 to 100.
def q59_evens_one_to_hundred():
    return [number for number in range(1, 101) if number % 2 == 0]

# 60. Generate only odd numbers from 1 to 100.
def q60_odds_one_to_hundred():
    return [number for number in range(1, 101) if number % 2 != 0]

# 61. Generate numbers from 1 to 100 divisible by both 3 and 5.
def q61_divisible_by_three_and_five():
    return [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]

# 62. Convert a list of strings to uppercase.
def q62_uppercase(words):
    return [word.upper() for word in words]

# 63. Convert a list of strings to lowercase.
def q63_lowercase(words):
    return [word.lower() for word in words]

# 64. Extract words having more than 5 characters.
def q64_long_words(words):
    return [word for word in words if len(word) > 5]

# 65. Extract numbers greater than 50.
def q65_greater_than_fifty(numbers):
    return [number for number in numbers if number > 50]

# 66. Replace negative numbers with 0.
def q66_replace_negatives(numbers):
    return [0 if number < 0 else number for number in numbers]

# 67. Create a list containing "Even" or "Odd" for each number.
def q67_even_or_odd(numbers):
    return ["Even" if number % 2 == 0 else "Odd" for number in numbers]

# 68. Create a list containing the length of every word.
def q68_word_lengths(words):
    return [len(word) for word in words]

# 69. Extract vowels from a string using list comprehension.
def q69_vowels(text):
    return [letter for letter in text if letter.lower() in "aeiou"]

# 70. Create a list of numbers whose square is greater than 100.
def q70_square_greater_than_hundred(numbers):
    return [number for number in numbers if number * number > 100]

# 71. Remove duplicate elements from a list without using set().
def q71_remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

# 72. Find all duplicate elements in a list.
def q72_duplicates(items):
    result = []
    for item in items:
        if items.count(item) > 1 and item not in result:
            result.append(item)
    return result

# 73. Find all elements that occur only once in a list.
def q73_unique_elements(items):
    return [item for item in items if items.count(item) == 1]

# 74. Find the common elements between two lists.
def q74_common(first, second):
    return [item for item in q71_remove_duplicates(first) if item in second]

# 75. Find elements present in the first list but not the second.
def q75_only_in_first(first, second):
    return [item for item in q71_remove_duplicates(first) if item not in second]

# 76. Merge two lists and remove duplicates.
def q76_merge_without_duplicates(first, second):
    return q71_remove_duplicates(first + second)

# 77. Find the intersection of three lists.
def q77_intersection_three(first, second, third):
    return [item for item in q71_remove_duplicates(first) if item in second and item in third]

# 78. Find the union of two lists without using set().
def q78_union(first, second):
    return q71_remove_duplicates(first + second)

# 79. Find the missing number from a list containing numbers from 1 to N.
def q79_missing_number(numbers):
    last_number = len(numbers) + 1
    for number in range(1, last_number + 1):
        if number not in numbers:
            return number
    return None

# 80. Find the first non-repeating element in a list.
def q80_first_non_repeating(items):
    for item in items:
        if items.count(item) == 1:
            return item
    return None

# 81. Find the first element that repeats while scanning the list.
def q81_first_repeating(items):
    seen = []
    for item in items:
        if item in seen:
            return item
        seen.append(item)
    return None

# 82. Find the element that occurs most frequently.
def q82_most_frequent(items):
    return max(items, key=items.count)


# 83. Find the element that occurs least frequently.
def q83_least_frequent(items):
    return min(items, key=items.count)


# 84. Find all pairs whose sum equals a given number.
def q84_pairs_with_sum(numbers, wanted):
    pairs = []
    for first_index in range(len(numbers)):
        for second_index in range(first_index + 1, len(numbers)):
            pair = (numbers[first_index], numbers[second_index])
            if sum(pair) == wanted:
                pairs.append(pair)
    return pairs


# 85. Find all triplets whose sum equals a given number.
def q85_triplets_with_sum(numbers, wanted):
    triplets = []
    for first_index in range(len(numbers)):
        for second_index in range(first_index + 1, len(numbers)):
            for third_index in range(second_index + 1, len(numbers)):
                triplet = (numbers[first_index], numbers[second_index], numbers[third_index])
                if sum(triplet) == wanted:
                    triplets.append(triplet)
    return triplets


# 86. Find the maximum sum of any two elements in a list.
def q86_maximum_pair_sum(numbers):
    ordered = sorted(numbers)
    return ordered[-1] + ordered[-2]


# 87. Find the minimum sum of any two elements.
def q87_minimum_pair_sum(numbers):
    ordered = sorted(numbers)
    return ordered[0] + ordered[1]


# 88. Find the maximum difference between two elements.
def q88_maximum_difference(numbers):
    return q04_largest(numbers) - q05_smallest(numbers)


# 89. Move all zeros to the end and keep the other numbers in order.
def q89_zeros_to_end(numbers):
    return [number for number in numbers if number != 0] + [0 for number in numbers if number == 0]


# 90. Move all negative numbers to the beginning of a list.
def q90_negatives_first(numbers):
    return [number for number in numbers if number < 0] + [number for number in numbers if number >= 0]


# 91. Separate even and odd numbers while keeping their order.
def q91_evens_then_odds(numbers):
    evens = [number for number in numbers if number % 2 == 0]
    odds = [number for number in numbers if number % 2 != 0]
    return evens, odds


# 92. Rotate a list right by K positions.
def q92_rotate_right(numbers, steps):
    if not numbers:
        return []
    steps = steps % len(numbers)
    if steps == 0:
        return numbers[:]
    return numbers[-steps:] + numbers[:-steps]


# 93. Find the longest consecutive sequence of integers.
def q93_longest_consecutive(numbers):
    ordered = sorted(set(numbers))
    longest = []
    current = []
    for number in ordered:
        if not current or number == current[-1] + 1:
            current.append(number)
        else:
            if len(current) > len(longest):
                longest = current
            current = [number]
    if len(current) > len(longest):
        longest = current
    return longest


# 94. Find one longest increasing subsequence in a list.
def q94_longest_increasing_subsequence(numbers):
    if not numbers:
        return []
    lengths = [1] * len(numbers)
    previous = [-1] * len(numbers)
    for end in range(len(numbers)):
        for before in range(end):
            if numbers[before] < numbers[end] and lengths[before] + 1 > lengths[end]:
                lengths[end] = lengths[before] + 1
                previous[end] = before
    end = lengths.index(max(lengths))
    result = []
    while end != -1:
        result.append(numbers[end])
        end = previous[end]
    return result[::-1]


# 95. Find the maximum sum of a continuous part of a list.
def q95_maximum_subarray_sum(numbers):
    best = current = numbers[0]
    for number in numbers[1:]:
        current = max(number, current + number)
        best = max(best, current)
    return best


# 96. Find all subarrays whose sum equals a given number.
def q96_subarrays_with_sum(numbers, wanted):
    result = []
    for start in range(len(numbers)):
        total = 0
        for end in range(start, len(numbers)):
            total += numbers[end]
            if total == wanted:
                result.append(numbers[start:end + 1])
    return result


# 97. Find the subarray with the largest sum.
def q97_largest_sum_subarray(numbers):
    best_start = start = 0
    best_end = 1
    current_sum = best_sum = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] > current_sum + numbers[index]:
            current_sum = numbers[index]
            start = index
        else:
            current_sum += numbers[index]
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = start
            best_end = index + 1
    return numbers[best_start:best_end]


# 98. Find each product without the current element and without division.
def q98_product_except_self(numbers):
    result = [1] * len(numbers)
    left_product = 1
    for index in range(len(numbers)):
        result[index] = left_product
        left_product *= numbers[index]
    right_product = 1
    for index in range(len(numbers) - 1, -1, -1):
        result[index] *= right_product
        right_product *= numbers[index]
    return result


# 99. Flatten a nested list into one simple list.
def q99_flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(q99_flatten(item))
        else:
            result.append(item)
    return result


