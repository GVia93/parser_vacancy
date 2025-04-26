from src.hh_api import HeadHunterAPI


def test_hh_fetch_vacancies(monkeypatch):
    """
    Тестируем метод fetch_vacancies без реального запроса
    """

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "items": [{"name": "Mock Vacancy", "alternate_url": "url"}],
                "pages": 1,
            }

    def mock_get(url, params):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    api = HeadHunterAPI()
    vacancies = api.fetch_vacancies("python")
    assert isinstance(vacancies, list)
    assert vacancies[0]["name"] == "Mock Vacancy"
