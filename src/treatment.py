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


class BaseOpera:
    #
    #     def __init__(self):
    #         self.name = None  # Название должности
    #         self.city = None  # Город
    #         self.work_place = None  # Место работы
    #         self.pay_from = None  # Оплата от
    #         self.pay_to = None  # Оплата до
    #         self.currency = None  # Валюта
    #         self.url = None  # Ссылка
    #         self.employer = None  # Ссылка на работодателя
    #         self.exp = None  # Опыт работы
    #
    def __str__(self):
        return f'{self.name}\nОплата от {self.pay_from} до {self.pay_to} {self.currency}'
        # print(f'{self.name}\nJОплата от {self.pay_from} до {self.pay_to} {self.currency}')


class HeadHuntSearch(BasicRequest, BaseOpera, HHJson):
    """Класс для обработки ответов по запросу с сайта HH.ru"""

    def __init__(self, call):
        super().__init__()
        self.name = self.from_json()[call]['name']  # Название должности
        self.city = self.from_json()[call]['area']['name']  # Город
        self.work_place = self.from_json()[call]['schedule']['name']  # Место работы
        # if self.from_json()[call]['salary']['from'] is None:  # Оплата от
        #     self.pay_from = "'Не указано'"
        # else:
        #     self.pay_from = self.from_json()[call]['salary']['from']
        self.pay_from = self.from_json()[call]['salary']['from'] \
            if isinstance(self.from_json()[call]['salary']['from'], int) \
            else "'Не указано'"  # is not None
        # if self.from_json()[call]['salary']['to'] is None:  # Оплата до
        #     self.pay_to = "'Не указано'"
        # else:
        #     self.pay_to = self.from_json()[call]['salary']['to']
        self.pay_to = self.from_json()[call]['salary']['to'] \
            if isinstance(self.from_json()[call]['salary']['to'], int) \
            else "'Не указано'"
        self.currency = self.from_json()[call]['salary']['currency']  # Валюта
        self.url = self.from_json()[call]['alternate_url']  # Ссылка
        self.employer = self.from_json()[call]['employer']['alternate_url']  # Ссылка на работодателя
        self.exp = self.from_json()[call]['experience']['name']  # Опыт работы

    # def __str__(self):
    #     # print(f'{self.name}\nJОплата от {self.pay_from} до {self.pay_to} {self.currency}')
    #     # super().__str__()
    #     print(self.from_json()[1]['salary']['from'])
    #     print(type(self.from_json()[1]['salary']['from']))
    #     print(self.from_json()[1]['salary']['to'])
    #     print(type(self.from_json()[1]['salary']['to']))
    #     return f'{self.name}\nОплата от {self.pay_from} до {self.pay_to} {self.currency}'

    def get_vacancies_from_json(self):
        return self.from_json()

    def key_words(self):
        pass

    def payment(self):
        pass

    def top_n(self, num: int):
        pass


class SuperJobSearch(BasicRequest, BaseOpera, SJJson):
    """Класс для обработки ответов по запросу с сайта SuperJob.ru"""

    def __init__(self, call):
        super().__init__()
        self.name = self.from_json()[call]['profession']  # Название должности
        self.city = self.from_json()[call]['town']['title']  # Город
        self.work_place = self.from_json()[call]['place_of_work']['title']  # Место работы
        self.pay_from = self.from_json()[call]['payment_from']  # Оплата от
        self.pay_to = self.from_json()[call]['payment_to']  # Оплата до
        self.currency = self.from_json()[call]['currency']  # Валюта
        self.url = self.from_json()[call]['link']  # Ссылка
        self.employer = self.from_json()[call]['client']['link']  # Ссылка на работодателя
        self.exp = self.from_json()[call]['experience']['title']  # Опыт работы

    # def __str__(self):
    #     # print(f'{self.name}\nОплата от {self.pay_from} до {self.pay_to} {self.currency}')
    #     # super().__str__()
    #     return f'{self.name}\nОплата от {self.pay_from} до {self.pay_to} {self.currency}'

    def get_vacancies_from_json(self):
        return self.from_json()

    def key_words(self):
        pass

    def payment(self):
        pass

    def top_n(self, num: int):
        pass


a = HeadHuntSearch(1)  # keyword='Developer', salary_to=1000000, salary_from=10
b = SuperJobSearch(1)
# print(a.from_json()[1]['salary']['from'])
print(a)
print(b)
# # c = SuperJobSearch(keyword='Developer', payment_to=1000000, payment_from=10)
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
# # print(asd)
#
# print(a.from_json())
# print(a.name)

# print(b.headers)
# print(b.reason)

# with open('HH.json', 'r') as file:
#     print(type(file))
#     af = file.readline()
#     print(type(af))
