def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[15,87,90,45,3,78,90,11]
bubbleSort(arr)
print("sorted array is :")
for i in range(len(arr)):
    print("%d" %arr[i]),
