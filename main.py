from src.hh_api import HeadHunterAPI
from src.json_storage import JSONStorage
from src.utils import (filter_vacancies_by_keyword,
                       filter_vacancies_by_salary_range, get_top_vacancies,
                       sort_vacancies_by_salary)
from src.vacancy import Vacancy


def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем через консоль.
    """
    hh = HeadHunterAPI()
    storage = JSONStorage()

    query = input("Введите поисковый запрос: ")
    vacancies_data = hh.fetch_vacancies(query)

    vacancies = []
    for item in vacancies_data:
        salary_info = item.get("salary")
        salary_from = salary_info.get("from") if salary_info else None
        vacancies.append(
            Vacancy(
                title=item.get("name", "Без названия"),
                url=item.get("alternate_url", ""),
                salary=salary_from,
                description=item.get("snippet", {}).get("requirement", "Нет описания"),
            )
        )

    storage.save_all(vacancies)
    print(f"Сохранено {len(vacancies)} вакансий в файл.")

    keywords = input("Введите ключевые слова для фильтрации через пробел: ").split()
    filtered = filter_vacancies_by_keyword(vacancies, keywords)

    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")
    try:
        salary_min, salary_max = map(int, salary_range.split("-"))
        filtered = filter_vacancies_by_salary_range(filtered, salary_min, salary_max)
    except ValueError:
        print("Неверный формат диапазона зарплат. Фильтрация по зарплате пропущена.")

    sorted_vacancies = sort_vacancies_by_salary(filtered)
    print(f"Найдено {len(sorted_vacancies)} вакансий после фильтрации.")

    top_n = int(input("Введите количество вакансий для отображения: "))
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    if not top_vacancies:
        print("Нет вакансий, соответствующих критериям.")
    else:
        for vacancy in top_vacancies:
            print(f"{vacancy.title} | {vacancy.salary} | {vacancy.url}")


if __name__ == "__main__":
    user_interaction()
