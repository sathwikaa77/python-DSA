def two_sum_sorted(arr, target):
  left = 0
  right = len(arr) - 1
  
  while left < right:
      current_sum = arr[left] + arr[right]
      if current_sum == target:
          return [left, right]
      elif current_sum < target:
          left += 1
      else:
          right -= 1
  
  return [-1, -1]

# Example usage
numbers = [2, 7, 11, 15, 19, 23]
print(two_sum_sorted(numbers, 26))  # Output: [1, 4] (7 + 19 = 26)
