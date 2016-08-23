inversion_count = 0
def merge_sort(input):
  global inversion_count
  if len(input) == 1:
    return input

  c = []
  mid = len(input)/2

  left = merge_sort(input[:mid])
  right = merge_sort(input[mid:])
  i = 0
  j = 0
  while i <  len(left) and j < len(right):
    if left[i] < right[j]:
      c.append(left[i])
      i = i + 1
    else:
      inversion_count = inversion_count + (len(left) - i)
      c.append(right[j])
      j = j + 1
  # Append the items which are left out
  if i < len(left):
    c.extend(left[i:])

  if j < len(right):
    c.extend(right[j:])
  return c


input = [6, 5, 4, 3]
print merge_sort(input)
print inversion_count