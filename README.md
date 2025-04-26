# Parser Vacancy

## О проекте
**Parser Vacancy** — это консольное приложение для поиска вакансий через API hh.ru, сохранения их в файл и последующей работы с данными.

Функционал:
- Поиск вакансий по ключевому слову
- Сохранение вакансий в формате JSON
- Фильтрация по ключевым словам в описании
- Фильтрация по диапазону зарплат
- Сортировка по уровню зарплаты
- Получение топ-N лучших вакансий

## Стек технологий
- Python 3.13
- requests
- pytest (для тестов)
- poetry (для управления зависимостями)

## Установка

1. Клонировать репозиторий:

```bash
git clone <your-repository-url>
cd vacancy_project
```

2. Установить зависимости:

```bash
poetry install
```

3. Активировать виртуальное окружение:

```bash
poetry shell
```

## Запуск проекта

```bash
python main.py
```

Программа запросит у вас:
- поисковый запрос;
- ключевые слова для фильтрации;
- диапазон зарплат;
- количество вакансий для вывода.

## Тестирование

Запуск всех тестов:

```bash
pytest
```

Запуск тестов с покрытием:

```bash
pytest --cov=src
```

## Структура проекта

```
vacancy_project/
├── src/
│   ├── api_interface.py
│   ├── hh_api.py
│   ├── vacancy.py
│   ├── utils.py
│   ├── storage_interface.py
│   ├── json_storage.py
├── tests/
│   ├── test_vacancy.py
│   ├── test_utils.py
│   ├── test_json_storage.py
│   └── test_hh_api.py
├── data/
│   └── vacancies.json
├── main.py
├── README.md
└── pyproject.toml
```

## Автор
Gvia ✨
