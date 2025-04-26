from abc import ABC, abstractmethod


class JobAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def fetch_vacancies(self, keyword: str) -> list[dict]:
        """
        Получение списка вакансий по ключевому слову.
        """
        pass
