import re

# Add Function which takes string of numbers
def add(numbers: str):
  if numbers == '': # if string is empty
    return 0

  del_ = None # delimeter
  if numbers[:2] == '//':
    numbers = numbers[2:]
    del_, numbers = re.split('\n', numbers, 1)

  pattern = ',|\n' # to find patterns
  if del_ is not None:
    pattern = f',|\n|\{del_}'

  nums = [ int(_) for _ in re.split(pattern, numbers) ]

  # check for negatives
  for num in nums:
    if num < 0:
      raise ValueError(f'negatives not allowed. found {num}')
  return sum(nums) 
