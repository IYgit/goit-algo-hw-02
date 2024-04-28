import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

# Функція генерації заявок
def generate_request():
    request_id = random.randint(1, 1000)  # Унікальний номер заявки
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

# Функція обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} обробляється.")
        # Тут можна реалізувати логіку обробки заявки
    else:
        print("Черга порожня. Немає заявок для обробки.")

# Головний цикл програми
def main():
    while True:
        generate_request()
        process_request()
        time.sleep(1)  # Затримка у 1 секунду між ітераціями циклу

if __name__ == "__main__":
    main()
