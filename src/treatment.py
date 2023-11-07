import json
from abc import ABC, abstractmethod

from src.API import HeadHunt, SuperJob


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


class HeadHuntSearch(BasicRequest):
    """Класс для обработки ответов по запросу с сайта HH.ru"""

    def get_vacancies_from_json(self):
        pass

    def key_words(self):
        pass

    def payment(self):
        pass


class SuperJobSearch(BasicRequest):
    """Класс для обработки ответов по запросу с сайта SuperJob.ru"""

    def get_vacancies_from_json(self):
        pass

    def key_words(self):
        pass

    def payment(self):
        pass


a = HeadHuntSearch(keyword='Developer', salary_to=1000000, salary_from=10)
c = SuperJobSearch(keyword='Developer', payment_to=1000000, payment_from=10)
# b = a.get_vacancies()
# b1 = c.get_vacancies()
c.to_json("SJ.json")
# a.to_json("HH.json")
# a.print_info()
# print(type(b))
# print(type(b))
# print(type(b1))
# print(json.loads(b.text))
# print(b.text)
# asd = json.dumps(b.content)
# print(asd)

# print(b.headers)
# print(b.reason)

# with open('HH.json', 'r') as file:
#     print(type(file))
#     af = file.readline()
#     print(type(af))
