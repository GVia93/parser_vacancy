import json
from pathlib import Path

from .storage_interface import VacancyStorage
from .vacancy import Vacancy


class JSONStorage(VacancyStorage):
    """
    Класс для работы с вакансиями в JSON файле.
    """

    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = Path(filename)
        self.__filename.parent.mkdir(parents=True, exist_ok=True)
        if not self.__filename.exists():
            self.__filename.write_text("[]", encoding="utf-8")

    def save_all(self, vacancies: list[Vacancy]) -> None:
        """
        Сохранение списка вакансий в файл.
        """
        with self.__filename.open("w", encoding="utf-8") as f:
            json.dump(
                [vacancy.to_dict() for vacancy in vacancies],
                f,
                ensure_ascii=False,
                indent=4,
            )

    def get_all(self) -> list[Vacancy]:
        """
        Получение списка вакансий из файла.
        """
        with self.__filename.open(encoding="utf-8") as f:
            data = json.load(f)
        return [Vacancy.from_dict(item) for item in data]

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл, если её ещё нет.
        """
        vacancies = self.get_all()
        if vacancy.to_dict() not in [v.to_dict() for v in vacancies]:
            vacancies.append(vacancy)
            self.save_all(vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии из файла.
        """
        vacancies = self.get_all()
        vacancies = [v for v in vacancies if v.to_dict() != vacancy.to_dict()]
        self.save_all(vacancies)
