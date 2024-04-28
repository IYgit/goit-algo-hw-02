from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо у нижній регістр
    s = s.lower().replace(" ", "")
    
    # Створюємо двосторонню чергу
    queue = deque()
    
    # Додаємо символи рядка до черги
    for char in s:
        queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    
    return True

# Приклади використання функції
print(is_palindrome("level"))    # True
print(is_palindrome("Level"))    # True (нечутливість до регістру)
print(is_palindrome("A man a plan a canal Panama"))    # True (ігнорує пробіли)
print(is_palindrome("hello"))    # False
