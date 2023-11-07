# import json
from abc import ABC, abstractmethod

from src.work_with_json import SJJson, HHJson


# from src.API import HeadHunt, SuperJob


class BasicRequest(ABC):

    @abstractmethod
    def get_vacancies_from_json(self):
        pass

    @abstractmethod
    def key_words(self):
        pass

    @abstractmethod
    def payment(self):
        pass

    @abstractmethod
    def top_n(self, num: int):
        pass


class HeadHuntSearch(BasicRequest, HHJson):
    """Класс для обработки ответов по запросу с сайта HH.ru"""

    def __init__(self, call):
        super().__init__()
        self.name = self.from_json()[call]['name']  # Название должности
        self.city = self.from_json()[call]['area']['name']  # Город
        self.pay_from = self.from_json()[call]['salary']['from']  # Оплата от
        self.pay_to = self.from_json()[call]['salary']['to']  # Оплата до
        self.currency = self.from_json()[call]['salary']['currency']  # Валюта
        self.url = self.from_json()[call]['apply_alternate_url']  # Ссылка
        self.employer = self.from_json()[call]['employer']  # Работодатель
        self.requirement = self.from_json()[call]['snippet']['requirement']  # Требования
        self.role = self.from_json()[call]['professional_roles'][0]['name']  # Роль на работа
        self.exp = self.from_json()[call]['experience']['name']  # Опыт работы

    def get_vacancies_from_json(self):
        pass

    def key_words(self):
        pass

    def payment(self):
        pass

    def top_n(self, num: int):
        pass


class SuperJobSearch(BasicRequest, SJJson):
    """Класс для обработки ответов по запросу с сайта SuperJob.ru"""

    def get_vacancies_from_json(self):
        pass

    def key_words(self):
        pass

    def payment(self):
        pass

    def top_n(self, num: int):
        pass


a = HeadHuntSearch(0)  # keyword='Developer', salary_to=1000000, salary_from=10
# c = SuperJobSearch(keyword='Developer', payment_to=1000000, payment_from=10)
# b = a.get_vacancies()
# b1 = c.get_vacancies()
# c.to_json("SJ.json")
# a.to_json("HH.json")
# a.print_info()
# print(type(b))
# print(type(b))
# print(type(b1))
# print(json.loads(b.text))
# print(b.text)
# asd = json.dumps(b.content)
# print(asd)

print(a.from_json())
print(a.name)

# print(b.headers)
# print(b.reason)

# with open('HH.json', 'r') as file:
#     print(type(file))
#     af = file.readline()
#     print(type(af))
