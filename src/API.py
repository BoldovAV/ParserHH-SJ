import os
from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):
    """Абстрактный класс для запросов на сайты HH.ru и SuperJob.ru
    Имеет абстрактный метод для запросов на сайты"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunt(AbstractAPI):

    def __init__(self, keyword, salary_from,
                 salary_to):  # , per_page=20
        self.url = "https://api.hh.ru/vacancies/"
        self.params = {
            # 'per_page': per_page,
            'text': keyword,
            'salary_from': salary_from,
            'salary_to': salary_to,
            'only_with_salary': True,
            # 'currency': 'RUR'
        }

    def get_vacancies(self):
        return requests.get(self.url, params=self.params).text


class SuperJob(AbstractAPI):
    api_key: str = os.getenv('SUPER_JOB_KEY').lstrip().rstrip()

    def __init__(self, keywords, payment_from,
                 payment_to):  # , count=20
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.headers = {'X-Api-App-Id': self.api_key}
        self.params = {
            'keyword': keywords,
            'payment_from': payment_from,
            'payment_to': payment_to,
            'no_agreement': 1,
            # 'count': count,
        }

    def get_vacancies(self):
        return requests.get(self.url, headers=self.headers,
                            params=self.params).json()
