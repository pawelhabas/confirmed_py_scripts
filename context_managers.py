# Context Managers

def example1():
    with open('example.txt', 'w') as file:
        file.write("Hello World")


def example2():
    import threading

    lock = threading.Lock()

    with lock:
        # critical section, only one thread at a time
        print("Tread-safe code block")


def example3():
    """No exception is raised, program continues smoothly"""
    from contextlib import suppress

    with suppress(FileNotFoundError):
        open("non_existent_file.txt")


def example4():
    import tempfile

    with tempfile.TemporaryFile(mode='w+t') as tmp:
        tmp.write("Temporary data")
        tmp.seek(0) # Go back to start of file to read
        data = tmp.read()
        print(data)


def example5():
    import time

    class Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            print("Start timer...")

        def __exit__(self, exc_type, exc_val, exc_tb):
            print(exc_type, exc_val, exc_tb)
            self.end = time.perf_counter()
            self.elapsed = self.end - self.start
            print(f"Timer stopped. Elapsed time: {self.elapsed:.4f} seconds")

    with Timer():
        0 / 0
        total = sum(range(10000000))
        print("Sum calculated:", total)


if __name__ == '__main__':
    pass
