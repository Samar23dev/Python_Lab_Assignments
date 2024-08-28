
def selectionsort(arr,n):
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        arr[min],arr[i]=arr[i],arr[min]

def insertionsort(arr,n):      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  

def bubblesort (list,n):
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if list[j]>list[j+1]:
                list[j+1],list[j]=list[j],list[j+1]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0
    j = 0 
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
 
def mergesort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)



def sort_list(arr):
    ch=int(input("Enter 1->Bubble Sort\n2->Selection Sort\n3->Merge Sort\n4->Insertion Sort\n"))
    match ch:
        case 1:
            bubblesort(arr,len(arr))
        case 2:
            selectionsort(arr,len(arr))
        case 3:
            mergesort(arr,0,len(arr)-1)
        case 4:
            insertionsort(arr,len(arr))
        case _:
            print("Wrong Entry || exit")

a=[int(ch) for ch in input("Enter list : ") if (ch!=" ")]
print("Initial Array : ",a)
# a.sort(reverse=True)
sort_list(a)
print("Sorted Array",a)