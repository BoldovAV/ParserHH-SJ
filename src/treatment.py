from abc import ABC, abstractmethod


class BasicRequest(ABC):

    @abstractmethod
    def vacancy_name(self):
        pass

    @abstractmethod
    def key_words(self):
        pass

    @abstractmethod
    def payment(self):
        pass
