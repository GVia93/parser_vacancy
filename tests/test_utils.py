import pytest

from src.utils import (filter_vacancies_by_keyword,
                       filter_vacancies_by_salary_range, get_top_vacancies,
                       sort_vacancies_by_salary)
from src.vacancy import Vacancy


@pytest.fixture
def vacancies():
    """
    Список тестовых вакансий.
    """
    return [
        Vacancy("Python Dev", "url", 150000, "Python Django"),
        Vacancy("Java Dev", "url", 120000, "Java Spring"),
        Vacancy("Go Dev", "url", 90000, "Go Kubernetes"),
    ]


def test_filter_by_keyword(vacancies):
    """
    Тест фильтрации вакансий по ключевому слову в описании.
    """
    result = filter_vacancies_by_keyword(vacancies, ["Python"])
    assert len(result) == 1
    assert result[0].title == "Python Dev"


def test_sort_by_salary(vacancies):
    """
    Тест сортировки вакансий по убыванию зарплаты.
    """
    sorted_v = sort_vacancies_by_salary(vacancies)
    assert sorted_v[0].salary == 150000


def test_get_top_vacancies(vacancies):
    """
    Тест получения топ-N вакансий по зарплате.
    """
    top = get_top_vacancies(vacancies, 2)
    assert len(top) == 2


def test_filter_by_salary_range(vacancies):
    """
    Тест фильтрации вакансий по диапазону зарплаты.
    """
    result = filter_vacancies_by_salary_range(vacancies, 100000, 160000)
    assert len(result) == 2
