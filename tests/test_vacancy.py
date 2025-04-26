from src.vacancy import Vacancy


def test_vacancy_creation():
    """
    Тест создания экземпляра вакансии и проверки его атрибутов.
    """
    vacancy = Vacancy("Python Developer", "https://example.com", 150000, "Опыт Python")
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary == 150000
    assert vacancy.description == "Опыт Python"


def test_vacancy_salary_validation():
    """
    Тест проверки значения зарплаты при отсутствии данных (None).
    """
    vacancy = Vacancy("Tester", "https://example.com", None, "Тестирование")
    assert vacancy.get_salary() == 0


def test_vacancy_comparison():
    """
    Тест сравнения вакансий по уровню зарплаты.
    """
    v1 = Vacancy("Dev1", "url", 100000, "desc")
    v2 = Vacancy("Dev2", "url", 150000, "desc")
    assert v1 < v2
