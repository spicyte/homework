import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    start_time = time.time()
    insertionSort(arr)
    end_time = time.time()

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    print("\nTime taken:", end_time - start_time, "seconds")
