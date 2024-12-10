import threading
import time
from datetime import datetime

# Flaga do zatrzymywania wątków
stop_event = threading.Event()

# Wątek 1: Podaje aktualny czas co 3 minuty
def print_time():
    while not stop_event.is_set():
        print(f"Aktualny czas: {datetime.now()}")
        time.sleep(180)  # 3 minuty

# Wątek 2: Wypisuje kolejne elementy ciągu Fibonacciego co 5 minut
def print_fibonacci():
    a, b = 0, 1
    while not stop_event.is_set():
        print(f"Fibonacci: {a}")
        a, b = b, a + b
        time.sleep(300)  # 5 minut

# Wątek 3: Przyjmuje prompty od użytkownika
def user_prompt():
    while not stop_event.is_set():
        command = input("Wpisz polecenie (end aby zakończyć): ").strip().lower()
        if command == "end":
            stop_event.set()

# Tworzenie wątków
thread1 = threading.Thread(target=print_time, daemon=True)
thread2 = threading.Thread(target=print_fibonacci, daemon=True)
thread3 = threading.Thread(target=user_prompt)

# Uruchamianie wątków
thread1.start()
thread2.start()
thread3.start()

# Czekanie na zakończenie wątku przyjmującego prompty
thread3.join()

print("Program zakończony.")
