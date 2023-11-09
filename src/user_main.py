# class MyError(Exception):
#
#     def __init__(self, *args, **kwargs):
#         self.message = args[0] if args else "Не корректный ввод"
#
#     def __str__(self):
#         return self.message


class Welcome:

    def __init__(self, keyword, pay_from=0, pay_to=0):
        self.keyword = keyword
        self.pay_from = int(pay_from)
        self.pay_to = int(pay_to)

    @property
    def site_search(self):
        try:
            site_for_search = input('По какому сайту вы хотели бы'
                                    ' осуществить поиск работы.\n'
                                    '1 -> HeadHunter.ru\n'
                                    '2 -> SuperJob.ru\n'
                                    '3 -> По всем\n'
                                    '0 -> Для выхода из программы\n')
            num = int(site_for_search)
            assert 0 <= num < 4
        except (TypeError, ValueError, AssertionError):
            # raise MyError("Не корректный ввод")
            print("Не корректный ввод")
            self.site_search

        else:
            if num == 0:
                print('Всего хорошего!')
                exit()
            else:
                if num == 1:
                    print("Вы выбрали поиск по HeadHunter.ru")
                elif num == 2:
                    print("Вы выбрали поиск по SuperJob.ru")
                else:
                    print("Вы выбрали поиск по всем")
                return num


class HowPay:

    def pay_from_(self):
        try:
            pay_from = int(input('Укажите минимальный уровень зарплаты\n'))
            assert pay_from >= 0
        except ValueError:
            print("Не корректный ввод, должно быть целое, не отрицательное число")
            self.pay_from_()
        except AssertionError:
            print("Значение должно быть не отрицательным")
            self.pay_from_()
        else:
            return pay_from


    def pay_to_(self):
        try:
            pay_to = int(input('Укажите максимальный уровень зарплаты\n'))
            assert pay_to >= 0

        except ValueError:
            print("Не корректный ввод, должно быть целое, не отрицательное число")
            self.pay_to_()
        except AssertionError:
            print("Значение должно быть не отрицательным")
            self.pay_to_()
        else:
            return pay_to


# class HowPay:
#
#     def __init__(self):
#         self.__pay_from = 0
#         self.__pay_to = 0
#
#     @property
#     def pay_from(self):
#         return self.__pay_from
#
#     @pay_from.setter
#     def pay_from(self, from_):
#         try:
#             self.__pay_from = int(from_)
#         except ValueError:
#             print("xuy")
#
#         # try:
#
#     pay_from = int(input('Укажите минимальный уровень зарплаты\n'))
#
# except ValueError:
#     print("Не корректный ввод")
#     return False
#
# try:
#     pay_to = int(input('Укажите максимальный уровень зарплаты\n'))
# except ValueError:
#     print("Не корректный ввод")
#     return False
# else:
#     return [pay_from, pay_to]


print("Добрый день. Данная программа помогает парсить"
      " сайты для поиска работы.")

profession = input("Введите название профессии по которой осуществлять поиск\n").capitalize()
pay = HowPay()
pay_from = pay.pay_from_()
pay_to = pay.pay_to_()


# chose = False
chose_site = Welcome(keyword=profession)
chose = chose_site.site_search
# while not chose:
#     # chose_site = Welcome(keyword=profession)
#     chose = chose_site.site_search
#
# answer = False
# while not answer:
#     answer_work = Welcome()
#     answer = answer_work.ask_key_pay()
