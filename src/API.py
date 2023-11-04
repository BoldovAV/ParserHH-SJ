import os
from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJob(AbstractAPI):
    api_key: str = os.getenv('SUPER_JOB_KEY').lstrip().rstrip()

    # super_job = https://api.superjob.ru/2.0/vacancies/:params
    # super_job = https://api.superjob.ru/2.0/vacancies/234234/

    def get_vacancies(self):
        pass


class HeadHunt(AbstractAPI):
    base_url = "https://api.hh.ru/"

    def get_vacancies(self):
        pass


a = SuperJob()
print(a.api_key)
# print(a.super_job)
