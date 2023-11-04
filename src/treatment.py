import json
from abc import ABC, abstractmethod

from src.API import HeadHunt, SuperJob


class BasicRequest(ABC):

    @abstractmethod
    def key_words(self):
        pass

    @abstractmethod
    def payment(self):
        pass

    @abstractmethod
    def to_json(self, path):
        pass


class HeadHuntSearch(BasicRequest, HeadHunt):

    def __init__(self, keyword=None, salary_from=None,
                 salary_to=None):
        super().__init__(keyword, salary_from, salary_to)

    def to_json(self, path):
        with open(path, "w") as file:  # , encoding='windows-1251'
            file.writelines(json.dumps(json.loads(b.text), indent=4))



    def key_words(self):
        pass

    def payment(self):
        pass


class SuperJobSearch(BasicRequest, SuperJob):

    def __init__(self, keyword=None, payment_from=None,
                 payment_to=None):
        super().__init__(keyword, payment_from, payment_to)

    def to_json(self, path):
        with open(path, "w") as file:
            file.writelines(json.dumps(self.get_vacancies(), indent=4))

    def key_words(self):
        pass

    def payment(self):
        pass


a = HeadHuntSearch(keyword='Developer', salary_to=1000000, salary_from=10)
c = SuperJobSearch(keyword='Developer', payment_to=1000000, payment_from=10)
b = a.get_vacancies()
b1 = c.get_vacancies()

a.to_json("HH.json")
# a.print_info()
# print(type(b))
# print(type(b))
# print(type(b1))
# print(json.loads(b.text))
# print(b.text)
# asd = json.dumps(b.content)
# print(asd)

# print(b.headers)
# print(b.reason)

# with open('HH.json', 'r') as file:
#     print(type(file))
#     af = file.readline()
#     print(type(af))
