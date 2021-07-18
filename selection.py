#python program on selction sort
a=[23,78,11,89,5]
for i in range(len(a)):
    min=i
    for j in range (i+1,len(a)):
        if a [min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]
print("sorted array")
for i in range (len(a)):
    print("%d" %a[i]),
            
