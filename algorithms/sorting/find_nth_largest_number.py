# Find the nth order statistic of a list of integers.
# Eg: Find 5th largest element in the array
# One technique is to sort the integers using nlogn algorithms and find the nth largest element
# The better way of doing it is using RANDOMIZED SELECTION which is kind of extension of
# quick_sort
# Step 1: Choose a pivot randomly and push the elements smaller than the pivot to the left side
#         and elements larger than the pivot to the right side
# Step 2: Find where n falls from the pivot(left side or right side) and change the nth order accordingly
#         Eg: If you are trying to find 5th largest element and say first pivot is the 3rd largest element.
#         Now we to find the 2nd largest element on the right side of the pivot
# Step 3: Do step 1 and step 2 until you find the nth element
# --------------------------------------------------------------------------------------------------------
import random

def random_number(first, last):
    return random.randint(first, last)

def partition(input, l, h):
    pivot_index = random_number(l, h)
    input[l], input[pivot_index] = input[pivot_index], input[l]
    
    i = l + 1
    for j in range(l + 1, h + 1):
        if input[j] < input[l]:
            input[i], input[j] = input[j], input[i]
            i = i + 1
    input[l], input[i-1] = input[i-1], input[l]
    return i - 1

def find_nth_element(input, l, h, order):
    if l <= h:
        pivot = partition(input, l, h)
        if pivot == order:
            return input[pivot]
        elif pivot > order: 
            return find_nth_element(input, l, pivot-1, order)
        else:
            return find_nth_element(input, pivot+1, h, order)

input = [10, 20, 6, 5, 4, 11, 13, 17, 25, 3, 2, 1]
print find_nth_element(input, 0, len(input)-1, 3)
