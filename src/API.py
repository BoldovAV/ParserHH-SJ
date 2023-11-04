import json
import os
from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJob(AbstractAPI):
    api_key: str = os.getenv('SUPER_JOB_KEY').lstrip().rstrip()

    def __init__(self, keywords, payment_from,
                 payment_to):  # , page=1
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.headers = {'X-Api-App-Id': self.api_key}
        self.params = {
            'keyword': keywords,
            'payment_from': payment_from,
            'payment_to': payment_to,
            # 'page': page,
        }

    def get_vacancies(self):
        return requests.get(self.url, headers=self.headers,
                            params=self.params).json()


class HeadHunt(AbstractAPI):

    def __init__(self, keyword, payment_from,
                 payment_to):  # , page=0
        self.url = "https://api.hh.ru/vacancies/"
        self.params = {
            # 'page': page,
            'text': keyword,
            'salary_from': payment_from,
            'salary_to': payment_to
        }


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.get_vacancies()))


    def get_vacancies(self):
        return requests.get(self.url, params=self.params)

# a = SuperJob(keywords='Разработчик')
# b = HeadHunt()
# # print(a.api_key)
# print(a.get_vacancies())
# print(b.get_vacancies())
# # # print(a.super_job)
