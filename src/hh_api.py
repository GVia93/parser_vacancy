import requests

from .api_interface import JobAPI


class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API hh.ru
    """

    def fetch_vacancies(self, keyword: str) -> list[dict]:
        """
        Получение всех вакансий по ключевому слову с постраничной загрузкой.
        """
        url = "https://api.hh.ru/vacancies"
        all_vacancies = []
        page = 0
        while True:
            params = {"text": keyword, "area": 1, "per_page": 100, "page": page}
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            items = data.get("items", [])
            if not items:
                break
            all_vacancies.extend(items)
            if page >= data.get("pages", 0) - 1:
                break
            page += 1
        return all_vacancies
