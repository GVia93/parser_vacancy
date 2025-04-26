from typing import Union


class Vacancy:
    """
    Класс для описания вакансии.
    """

    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary: Union[int, str], description: str):
        self.title = title
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Сравнение вакансий по зарплате.
        """
        return self.get_salary() < other.get_salary()

    def get_salary(self) -> int:
        """
        Получение зарплаты вакансии.
        """
        return self.salary if isinstance(self.salary, int) else 0

    def to_dict(self) -> dict:
        """
        Преобразование экземпляра вакансии в словарь.
        """
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Vacancy":
        """
        Создание экземпляра вакансии из словаря.
        """
        return cls(
            title=data["title"],
            url=data["url"],
            salary=data["salary"],
            description=data["description"],
        )
