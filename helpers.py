from faker import Faker
import random
from csv import DictReader
from files import CSV_FILE_PATH

def get_fake_product():
    fake = Faker()
    max_length = random.randint(1, 7)  # Случайное число от 1 до 7
    text = fake.text(max_nb_chars=max_length * 10)  # Генерация текста
    text = text[:max_length]  # Обрезка текста до нужного количества символов
    return text

def get_user_data():
    fake = Faker()
    firstname = fake.first_name()
    lastname = fake.last_name()
    email = fake.email()
    password = "test"
    return firstname, lastname, email, password


import csv


def get_emails():
    with open(CSV_FILE_PATH, mode='r') as csv_file:
        next(csv_file)
        line = csv_file.readline().strip()
        emails = [email.strip() for email in line.split(',') if email.strip()]
    return emails

