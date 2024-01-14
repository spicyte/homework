import threading
import time
shared_resource = 0

lock = threading.Lock()

def modify_resource(thread_id):
    global shared_resource

    lock.acquire()

    try:
        print(f"Thread {thread_id} отримав блокування.")
        
        shared_resource += 1
        print(f"Thread {thread_id} змінив ресурс: {shared_resource}")
        
        time.sleep(1)

        print(f"Thread {thread_id} завершив роботу.")
    finally:
        lock.release()

threads = []
for i in range(5):
    thread = threading.Thread(target=modify_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Всі потоки завершили роботу. Значення спільного ресурсу:", shared_resource)
