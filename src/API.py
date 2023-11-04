import os
from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJob(AbstractAPI):
    api_key: str = os.getenv('SUPER_JOB_KEY').lstrip().rstrip()

    def __init__(self, keywords=None, payment_from=None,
                 payment_to=None):  # , page=1
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
                            params=self.params)


class HeadHunt(AbstractAPI):

    def __init__(self, keyword=None, salary_from=None,
                 salary_to=None):  # , page=0
        self.url = "https://api.hh.ru/"
        self.params = {
            # 'page': page,
            'text': keyword,
            'salary_from': salary_from,
            'salary_to': salary_to
        }

    def get_vacancies(self):
        return requests.get(self.url, params=self.params)

# a = SuperJob(keywords='Разработчик')
# b = HeadHunt()
# # print(a.api_key)
# print(a.get_vacancies())
# print(b.get_vacancies())
# # # print(a.super_job)
