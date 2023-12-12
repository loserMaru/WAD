import threading


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.RLock()

    def print_lock_info(self, action):
        print(f"{action} - Захвачено: {self.lock._is_owned()}, "
              f"Идентификатор потока: {threading.current_thread().ident}")

    def increment(self):
        with self.lock:
            self.print_lock_info("Инкремент")
            self.value += 1
            self.increment_recursive(2)

    def increment_recursive(self, n):
        with self.lock:
            if n > 0:
                self.print_lock_info("Рекурсивный инкремент")
                self.value += 1
                self.increment_recursive(n - 1)

    def decrement(self):
        with self.lock:
            self.print_lock_info("Декремент")
            self.value -= 1
            self.decrement_recursive(2)

    def decrement_recursive(self, n):
        with self.lock:
            if n > 0:
                self.print_lock_info("Рекурсивный декремент")
                self.value -= 1
                self.decrement_recursive(n - 1)


def main():
    n = int(input("Введите количество потоков для инкремента: "))
    m = int(input("Введите количество потоков для декремента: "))

    counter = Counter()

    threads = []

    for _ in range(n):
        threads.append(threading.Thread(target=counter.increment))

    for _ in range(m):
        threads.append(threading.Thread(target=counter.decrement))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Значение счетчика: {counter.value}")


if __name__ == "__main__":
    main()
