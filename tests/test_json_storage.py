from src.json_storage import JSONStorage
from src.vacancy import Vacancy


def test_json_storage_operations(tmp_path):
    """
    Тест операций добавления, получения и удаления вакансий в JSONStorage.
    """
    file_path = tmp_path / "test_vacancies.json"
    storage = JSONStorage(filename=str(file_path))

    vacancy = Vacancy("Test Dev", "url", 100000, "Testing")

    assert storage.get_all() == []

    storage.add_vacancy(vacancy)
    vacancies = storage.get_all()
    assert len(vacancies) == 1
    assert vacancies[0].title == "Test Dev"

    storage.delete_vacancy(vacancy)
    assert storage.get_all() == []
