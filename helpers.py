import csv

from faker import Faker
import random
from files import CSV_FILE_PATH, ADMIN_CREDENTIALS


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


def get_emails():
    with open(CSV_FILE_PATH, mode='r') as csv_file:
        next(csv_file)
        line = csv_file.readline().strip()
        emails = [email.strip() for email in line.split(',') if email.strip()]
    return emails

def get_random_user():
    email_list = get_emails()
    return random.choice(email_list), "test"


def get_credentials():
    with open(ADMIN_CREDENTIALS, mode="r", newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            return row
