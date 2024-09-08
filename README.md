# Проектная работа по курсу Python QA Engineer Otus.
Автоматизация тестирования OpenCart
Подготовка для запуска:

Склоннировать репозиторий
git clone git@github.com:mishacap/Project.git
Установить содержимое requirements.txt
pip install -r requirements.txt

Для запуска тестов необходимо выполнить команду:
pytest -n 2 --executor="local"
Дополнительные атрибуты: 
--headless - запуск в безоконном режиме, по умолчанию - False
--browser (сhrome по умолчанию, так же есть firefox) 
--url - ip адрес и порт для развернутого OpenCart
--executor - local или через selenoid
