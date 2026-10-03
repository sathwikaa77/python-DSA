#SELECTION SORTING
a=[23,12,22,45,7,8]
def selectionsort(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    print(a)
selectionsort(a)

