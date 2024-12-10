import threading
import time

# Funkcja, która będzie wykonywana w wątku
def print_numbers(name, start, end, delay):
    for number in range(start, end + 1):
        print(f"Thread {name}: {number}")
        time.sleep(delay)  # Symulacja opóźnienia, np. przetwarzania

# Tworzenie wątków
thread1 = threading.Thread(target=print_numbers, args=("A", 1, 5, 1))
thread2 = threading.Thread(target=print_numbers, args=("B", 6, 10, 0.5))

# Uruchamianie wątków
thread1.start()
thread2.start()

# Czekanie na zakończenie wątków
thread1.join()
thread2.join()

print("Wszystkie wątki zakończyły pracę.")
