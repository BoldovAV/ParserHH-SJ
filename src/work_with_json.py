import json
from abc import ABC, abstractmethod

from src.API import HeadHunt, SuperJob


class JsonFile(ABC):

    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def from_json(self):
        pass


class HHJson(JsonFile, HeadHunt):

    def __init__(self, keyword=None, salary_from=None,
                 salary_to=None):
        super().__init__(keyword, salary_from, salary_to)

    def to_json(self):
        with open("HH.json", "w", encoding='utf-8') as file:  # , encoding='windows-1251'
            file.writelines(json.dumps(json.loads(self.get_vacancies()),
                                       ensure_ascii=False, indent=4))

    def from_json(self):
        with open("HH.json", "r", encoding='utf-8') as file:
            text = json.load(file)
            return text['items']


class SJJson(JsonFile, SuperJob):

    def __init__(self, keyword=None, payment_from=None,
                 payment_to=None):
        super().__init__(keyword, payment_from, payment_to)

    def to_json(self):
        with open("SJ.json", "w", encoding='utf-8') as file:
            file.writelines(json.dumps(self.get_vacancies(),
                                       indent=4, ensure_ascii=False))

    def from_json(self):
        with open("SJ.json", "r", encoding='utf-8') as file:
            text = json.load(file)
            return text['objects']


a = HHJson(keyword='ss13rfhncgj', salary_to=1000000, salary_from=10)
# c = SJJson(keyword='Developer', payment_to=1000000, payment_from=10)
a.to_json()
# # c.to_json()
# print(c.from_json())
# print(a.from_json())
