import os
from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keywords):
        pass


class SuperJob(AbstractAPI):
    api_key: str = os.getenv('SUPER_JOB_KEY').lstrip().rstrip()
    
    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.headers = {'X-Api-App-Id': self.api_key}
        self.params = {
            'count': 2,
            'page': 1,
            'town': 'Kaliningrad',
        }

    # super_job = https://api.superjob.ru/2.0/vacancies/:params
    # super_job = https://api.superjob.ru/2.0/vacancies/234234/

    def get_vacancies(self, keywords):
        pass


class HeadHunt(AbstractAPI):
    base_url = "https://api.hh.ru/"

    def get_vacancies(self, keywords):
        pass


a = SuperJob()
print(a.api_key)
print(a.headers)
# print(a.super_job)
