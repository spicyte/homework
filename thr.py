import threading
import time

def func(car):
    print("Начало нашей ф-и..." + car)
    time.sleep(3)
    print("...конец ф-и")


def main():
    threads = []
    for i in range(1):
        car = 'Impala' + str(i)
        thread = threading.Thread(target=func, args=(car,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join

if __name__ == "__main__":
    main()