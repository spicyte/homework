import time

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    start_time = time.time()
    bubbleSort(arr)
    end_time = time.time()

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    print("\nTime taken:", end_time - start_time, "seconds")
