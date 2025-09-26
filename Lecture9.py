import threading
import time

def countdown_thread(thread_name, start_number):
    print(f" Поток '{thread_name}' начал выполнение")
    for i in range(start_number, 0, -1):
        print(f"[{thread_name}]: {i}")
        time.sleep(1)
    print(f" Поток '{thread_name}' завершил выполнение")


first = threading.Thread(
    target=countdown_thread,
    args=("Поток-1", 10),
    name="first"
)

second = threading.Thread(
    target=countdown_thread,
    args=("Поток-2", 10),
    name="second"
)

first.start()
second.start()

first.join()
second.join()