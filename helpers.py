from faker import Faker
import random

def get_fake_product():
    fake = Faker()
    max_length = random.randint(1, 7)  # Случайное число от 1 до 7
    text = fake.text(max_nb_chars=max_length * 10)  # Генерация текста
    text = text[:max_length]  # Обрезка текста до нужного количества символов
    return text
