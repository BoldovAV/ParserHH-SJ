# import json
from abc import ABC, abstractmethod

from src.work_with_json import SJJson, HHJson


# from src.API import HeadHunt, SuperJob


class BasicRequest(ABC):
    """Абстрактный класс для классов по обработке вакансий с разных сайтов"""
    @abstractmethod
    def get_vacancies_from_json(self):
        pass
    #
    # @abstractmethod
    # def key_words(self):
    #     pass

    # @abstractmethod
    # def avg_payment(self):
    #     pass

    # @abstractmethod
    # def top_n(self, num: int):
    #     pass


class BaseOpera:

    def __str__(self):
        return (f'{self.name}\nОплата от {self.pay_from} до {self.pay_to} {self.currency}\n'
                f'г. {self.city}, тип работы (вахта/удаленка и т.д.): {self.work_place}\n'
                f'Работодатель: {self.employer}\n'
                f'Требуемый опыт: {self.exp}\n'
                f'{self.url}')

    def avg_payment(self):
        if isinstance(self.pay_from, int) and isinstance(self.pay_to, int):
            return (self.pay_from + self.pay_to) / 2
        elif isinstance(self.pay_from, int):
            return self.pay_from
        else:
            return self.pay_to


class HeadHuntSearch(BasicRequest, BaseOpera, HHJson):
    """Класс для обработки ответов по запросу с сайта HH.ru"""

    def __init__(self, call):
        super().__init__()
        self.name = self.from_json()[call]['name']  # Название должности
        self.city = self.from_json()[call]['area']['name']  # Город
        self.work_place = self.from_json()[call]['schedule']['name']  # Место работы
        self.pay_from = self.from_json()[call]['salary']['from'] \
            if isinstance(self.from_json()[call]['salary']['from'], int) \
            else "'Не указано'"  # Оплата от
        self.pay_to = self.from_json()[call]['salary']['to'] \
            if isinstance(self.from_json()[call]['salary']['to'], int) \
            else "'Не указано'"  # Оплата до
        self.currency = self.from_json()[call]['salary']['currency']  # Валюта
        self.url = self.from_json()[call]['alternate_url']  # Ссылка
        self.employer = self.from_json()[call]['employer']['alternate_url']  # Ссылка на работодателя
        self.exp = self.from_json()[call]['experience']['name']  # Опыт работы

    def get_vacancies_from_json(self):
        return self.from_json()
    #
    # def key_words(self):
    #     pass
    #
    # def avg_payment(self):
    #     if isinstance(self.pay_from, int) and isinstance(self.pay_to, int):
    #         return (self.pay_from + self.pay_to) / 2
    #     elif isinstance(self.pay_from, int):
    #         return self.pay_from
    #     else:
    #         return self.pay_to
    #
    # def top_n(self, num: int):
    #     pass


class SuperJobSearch(BasicRequest, BaseOpera, SJJson):
    """Класс для обработки ответов по запросу с сайта SuperJob.ru"""

    def __init__(self, call):
        super().__init__()
        self.name = self.from_json()[call]['profession']  # Название должности
        self.city = self.from_json()[call]['town']['title']  # Город
        self.work_place = self.from_json()[call]['place_of_work']['title']  # Место работы
        self.pay_from = self.from_json()[call]['payment_from'] \
            if isinstance(self.from_json()[call]['payment_from'], int) \
            else "'Не указано'"  # Оплата от
        self.pay_to = self.from_json()[call]['payment_to'] \
            if isinstance(self.from_json()[call]['payment_to'], int) \
            else "'Не указано'"  # Оплата до
        self.currency = self.from_json()[call]['currency']  # Валюта
        self.url = self.from_json()[call]['link']  # Ссылка
        self.employer = self.from_json()[call]['client']['link']  # Ссылка на работодателя
        self.exp = self.from_json()[call]['experience']['title']  # Опыт работы

    def get_vacancies_from_json(self):
        return self.from_json()
    #
    # def key_words(self):
    #     pass

    # def avg_payment(self):
    #     if isinstance(self.pay_from, int) and isinstance(self.pay_to, int):
    #         return (self.pay_from + self.pay_to)/2
    #     elif isinstance(self.pay_from, int):
    #         return self.pay_from
    #     else:
    #         return self.pay_to

# a = HeadHuntSearch(1)  # keyword='Developer', salary_to=1000000, salary_from=10
# b = SuperJobSearch(1)
# # print(a.from_json()[1]['salary']['from'])
# print(a)
# print(b)
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


# HHJson
#     Полный день 654
# 	Удаленная работа 95
# 	Гибкий график 35
# 	Сменный график 32
# 	Вахтовый метод 9

# sj
# Неполная
# Полная
# Неполная дистанционная
# Сменная
# Вахтовая
# Удаленная работа
# На территории работодателя
