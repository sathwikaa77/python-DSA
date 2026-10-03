#sorting
def linearsearch(ar,target):
  for i in range(len(ar)):
    if ar[i]==target:
      print(f'{target} is found at index {i}')
      return
  print('not found')
  return -1
a=[23,12,22,45,7,8]
print(linearsearch(a,10))