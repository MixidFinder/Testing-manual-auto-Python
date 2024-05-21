# Тестовое задание для SafeBoard
Написать тесты для тестирования API https://jsonplaceholder.typicode.com/ используя python и pytest.
- GET   /posts
- POST   /posts
- PUT   /posts/1
- PATCH   /posts/1
- DELETE   /posts/1

# Установка
Клонировать репозиторий:  
```bash
git clone https://github.com/MixidFinder/Testing-manual-auto-Python_test-task_Danila-Muravyov.git
```

Создать `.venv` и активировать его:  
```bash
python -m venv .venv
.venv\Scripts\activate
```

Установить зависимости:  
```bash
pip itstall -r requirements.txt
```

# Структура проекта
- `utils` содержит `typicode_api.py` - модуль для работы с API и `checker.py` - модуль для проверки статус-кодов и содержимого ответов API.
- `tests` содержит `test_typicode_api.py` - тесты для различных конечных точек API Typicode, используя библиотеку pytest.

# Пояснения
Из за особенностей предоставленного API не смог протестировать `DELETE` на негативный результат, так как API возвращает код `200` даже при удалении несуществующего поста.  
По той же причине сделаны тесты на `500` код `PUT` `PATCH` `POST`, так как API принимает любые введенные данные как верные, за исключением вообще недопустимых данных.
