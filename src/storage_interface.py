from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class VacancyStorage(ABC):
    """
    Абстрактный класс для хранилища вакансий.
    """

    @abstractmethod
    def save_all(self, vacancies: list[Vacancy]) -> None:
        """
        Сохранение всех вакансий в хранилище.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[Vacancy]:
        """
        Получение всех вакансий из хранилища.
        """
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в хранилище.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии из хранилища.
        """
        pass
