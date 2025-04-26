from src.vacancy import Vacancy


def filter_vacancies_by_keyword(vacancies: list[Vacancy], keywords: list[str]) -> list[Vacancy]:
    """
    Фильтрация вакансий по ключевым словам в описании.
    """
    return [
        vacancy
        for vacancy in vacancies
        if any(
            keyword.lower() in (vacancy.description or "").lower()
            for keyword in keywords
        )
    ]


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортировка вакансий по зарплате по убыванию.
    """
    return sorted(vacancies, key=lambda vacancy: vacancy.get_salary(), reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Получение топ-N вакансий с самой высокой зарплатой.
    """
    return vacancies[:top_n]


def filter_vacancies_by_salary_range(vacancies: list[Vacancy], salary_min: int, salary_max: int) -> list[Vacancy]:
    """
    Фильтрация вакансий по диапазону зарплаты.
    """
    return [
        vacancy
        for vacancy in vacancies
        if salary_min <= vacancy.get_salary() <= salary_max
    ]
