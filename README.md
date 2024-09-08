# Проектная работа по курсу Python QA Engineer Otus.
## Автоматизация тестирования OpenCart

### Подготовка для запуска:

1. Склонировать репозиторий:
   ```bash
   git clone git@github.com:mishacap/Project.git
   ```

2. Установить зависимости из `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Запуск тестов:
Для запуска тестов необходимо выполнить команду:
```bash
pytest -n 2 --executor="local"
```

### Дополнительные атрибуты:
- `--headless` — запуск в безоконном режиме (по умолчанию: `False`)
- `--browser` — браузер для запуска (по умолчанию: `chrome`, также доступен `firefox`)
- `--url` — IP-адрес для развернутого OpenCart
- `--executor` — режим исполнения тестов (`local` или через `selenoid`)
