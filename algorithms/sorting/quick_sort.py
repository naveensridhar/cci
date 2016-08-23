# Quick Sort Pseudo Code
# Step 1: Choose a pivot element. The pivot element can be first element. But the problem will be that the input may not be divided into two equal partitions
# sometimes. So choose a random pivot and replace it with first element(constant operation)
# Step 2: Move all the elements less than the pivot to the left side and greater than the pivot to the right side
# Create two variables, one(i) to track the unseen input and one two mark the boundary(j) pointing the smaller and bigger elements than the pivot
# Step 3: Once all the elements are seen, swap the pivot with the biggest element left side of the variable marking the boundary(j)
# Step 4: Do the same recursively for elements left of the pivot and right of the pivot
# ------------------------------------------------------------------------------------------------------------------------------------
import random
def random_number(first, last):
    return random.randint(first,last)

def quick_sort(input, l, h):
    if l <  h:
        p = partition(input, l, h)
        quick_sort(input, l, p-1)
        quick_sort(input, p+1, h)


def partition(input, l, h):
    pivot = random_number(l, h)
    input[l], input[pivot] = input[pivot], input[l]
    j = l+1
    for i in range(l+1, h+1):
        if input[i] < input[l]:
            input[i], input[j] = input[j], input[i]
            j = j+1
    input[l], input[j-1] = input[j-1], input[l]
    return j-1 
        
input = [10, 20, 30, 8, 5, 4, 15]
quick_sort(input, 0, len(input)-1)        
print input   
