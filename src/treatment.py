from abc import ABC, abstractmethod

from src.work_with_json import SJJson, HHJson


class BasicRequest(ABC):
    """Абстрактный класс для классов по обработке вакансий с разных сайтов"""

    @abstractmethod
    def get_vacancies_from_json(self):
        pass


class BaseOpera:

    def __str__(self):
        return (f'{self.name}\nОплата от {self.pay_from} до {self.pay_to} {self.currency}\n'
                f'г. {self.city}, тип работы (вахта/удаленка и т.д.): {self.work_place}\n'
                f'Работодатель: {self.employer}\n'
                f'Требуемый опыт: {self.exp}\n'
                f'{self.url}')

    def avg_payment(self):
        if isinstance(self.pay_from, int) and isinstance(self.pay_to, int):
            return int((self.pay_from + self.pay_to) / 2)
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
