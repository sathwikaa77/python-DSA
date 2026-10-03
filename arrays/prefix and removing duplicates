def prefixsum(a):
  ar=[0 for _ in range(len(a))]
  sum=0
  for i in range(len(a)):
    sum=sum+a[i]
    ar[i]=sum
  return ar
def rangesum(a,st,en):
  if st==0:
    return a[en]
  return a[en]-a[st-1]
a=[3,1,4,1,5,9,2,6]
res=prefixsum(a)
print(rangesum(res,0,5))



def remove_duplicates(arr):
  write = 1
  for read in range(1, len(arr)):
    if arr[read] != arr[read -1]:
      arr[write] = arr[read]
      write += 1
  return write
numbers = [1,1,2,2,3,3,4,5,5]
new_length = remove_duplicates(numbers)
print(numbers[:new_length])
