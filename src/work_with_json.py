import json
import os
from abc import ABC, abstractmethod

from src.API import HeadHunt, SuperJob

path = os.path.join("..", "json_files")


class JsonFile(ABC):

    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def from_json(self):
        pass


class HHJson(JsonFile, HeadHunt):
    path_hh = os.path.join(path, "HH.json")

    def __init__(self, keyword=None, salary_from=None,
                 salary_to=None):
        super().__init__(keyword, salary_from, salary_to)

    def to_json(self):
        with open(self.path_hh, "w", encoding='utf-8') as file:  # , encoding='windows-1251'
            file.writelines(json.dumps(json.loads(self.get_vacancies()),
                                       ensure_ascii=False, indent=4))

    def from_json(self):
        with open(self.path_hh, "r", encoding='utf-8') as file:
            text = json.load(file)
            return text['items']


class SJJson(JsonFile, SuperJob):
    path_sj = os.path.join(path, "SJ.json")

    def __init__(self, keyword=None, payment_from=None,
                 payment_to=None):
        super().__init__(keyword, payment_from, payment_to)

    def to_json(self):
        with open(self.path_sj, "w", encoding='utf-8') as file:
            file.writelines(json.dumps(self.get_vacancies(),
                                       indent=4, ensure_ascii=False))

    def from_json(self):
        with open(self.path_sj, "r", encoding='utf-8') as file:
            text = json.load(file)
            return text['objects']

# a = HHJson(keyword='ss13rfhncgj', salary_to=1000000, salary_from=10)
# c = SJJson(keyword='Developer', payment_to=1000000, payment_from=10)
# # a.to_json()
# # # # c.to_json()
# print(len(c.from_json()))
# # print(a.from_json())
