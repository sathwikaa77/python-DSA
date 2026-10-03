def linearsearch(a,el):
  res=[]
  for i in range(len(a)):
    if a[i]==el:
     res.append(i)
  return res

a=[1,2,3,2,4,5,3]
el=2
print(linearsearch(a,el))