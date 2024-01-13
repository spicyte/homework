import threading


data = [4, 2, 8, 1, 6, 3, 7, 5]

def process_data(data):
    sorted_data = sorted(data)
    print(f"Sorted Data: {sorted_data}")

def process_data_multithreaded(data):
    mid = len(data) // 2
    first_half = data[:mid]
    second_half = data[mid:]

    thread1 = threading.Thread(target=process_data, args=(first_half,))
    thread2 = threading.Thread(target=process_data, args=(second_half,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

print("Single-threaded:")
process_data(data)

print("\nMulti-threaded:")
process_data_multithreaded(data)