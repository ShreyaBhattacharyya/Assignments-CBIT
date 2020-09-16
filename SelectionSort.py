def SelectionSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if(a[min]>a[j]):
                min = j
        t = a[i]
        a[i] = a[min]
        a[min]=t

    print("Sorted Array")
    for i in range(len(a)):
        print(a[i],"\t", end = '')

b = [27,10,13,2,104]
SelectionSort(b)