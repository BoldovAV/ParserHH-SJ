# class MyError(Exception):
#
#     def __init__(self, *args, **kwargs):
#         self.message = args[0] if args else "Не корректный ввод"
#
#     def __str__(self):
#         return self.message
from src.work_with_json import HHJson, SJJson


class Welcome:

    def __init__(self, keyword, pay_from=0, pay_to=0):
        self.keyword = keyword
        self.pay_from = int(pay_from)  # if pay_from is not None else 0
        self.pay_to = int(pay_to)  # if pay_from is not None else 0

    def site_search(self):
        try:
            site_for_search = input('\nПо какому сайту вы хотели бы'
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
            self.site_search()

        else:
            if num == 0:
                print('Всего хорошего!')
                exit()
            else:
                if num == 1:
                    print("\nВы выбрали поиск по HeadHunter.ru\n")
                    HHJson(keyword=self.keyword,
                           salary_from=self.pay_from,
                           salary_to=self.pay_to).to_json()
                elif num == 2:
                    print("\nВы выбрали поиск по SuperJob.ru\n")
                    SJJson(keyword=self.keyword,
                           payment_from=self.pay_from,
                           payment_to=self.pay_to).to_json()
                else:
                    print("\nВы выбрали поиск по всем\n")
                    HHJson(keyword=self.keyword,
                           salary_from=self.pay_from,
                           salary_to=self.pay_to).to_json()
                    SJJson(keyword=self.keyword,
                           payment_from=self.pay_from,
                           payment_to=self.pay_to).to_json()
                return num


class HowPay:

    def pay_from_(self):
        try:
            pay_min = int(input('Укажите минимальный уровень зарплаты\n'))
            # print(pay_min)
            # print(type(pay_min))
            assert pay_min >= 0
        except ValueError:
            print("Не корректный ввод, должно быть целое, не отрицательное число")
            # print(pay_min)
            # print(type(pay_min))
            return self.pay_from_()
        except AssertionError:
            print("Значение должно быть не отрицательным")
            # print(pay_min)
            # print(type(pay_min))
            return self.pay_from_()
        else:
            # print(pay_min)
            # print(type(pay_min))
            return pay_min

    def pay_to_(self):
        try:
            pay_max = int(input('Укажите максимальный уровень зарплаты\n'))
            assert pay_max >= 0

        except ValueError:
            print("Не корректный ввод, должно быть целое, не отрицательное число")
            return self.pay_to_()
        except AssertionError:
            print("Значение должно быть не отрицательным")
            return self.pay_to_()
        else:
            return pay_max


print("Добрый день. Данная программа помогает парсить"
      " сайты для поиска работы.")

profession = input("Введите название профессии по которой осуществлять поиск\n").capitalize()
pay = HowPay()
pay_from = pay.pay_from_()
pay_to = pay.pay_to_()
while True:
    if pay_from <= pay_to or pay_from == 0 or pay_to == 0:
        break
    else:
        print("Минимальная оплата должна быть меньше максимальной,"
              " или одна из них должны быть 0 (не указана).\n"
              "Попробуйте еще раз\n")
        pay_from = pay.pay_from_()
        pay_to = pay.pay_to_()
# print(type(pay_from))
# print(pay_from)
chose_site = Welcome(keyword=profession, pay_from=pay_from, pay_to=pay_to)
# print(chose_site.keyword)
# print(chose_site.pay_from)
# print(chose_site.pay_to)
print(chose_site.site_search())
