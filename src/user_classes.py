from src.work_with_json import HHJson, SJJson


class Welcome:

    def __init__(self, keyword, pay_from, pay_to):
        self.keyword = keyword
        self.pay_from = pay_from  # if pay_from is not None else 0
        self.pay_to = pay_to  # if pay_from is not None else 0

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
            print("Не корректный ввод")
            self.site_search()

        else:
            if num == 0:
                print('Всего хорошего!')
                exit()
            else:
                if num == 1:
                    print(f"\nВы выбрали поиск по HeadHunter.ru\n")
                    how = HHJson(keyword=self.keyword,
                                 salary_from=self.pay_from,
                                 salary_to=self.pay_to)
                    how.to_json()
                    how_get = len(how.from_json())
                    if how_get == 0:
                        print("Увы, по такому запросу ничего не найдено, попробуйте снова")
                        exit()
                    print(f"Получено {how_get} вакансий")
                    num = (num, [how_get])
                elif num == 2:
                    print(f"\nВы выбрали поиск по SuperJob.ru\n")
                    how = SJJson(keyword=self.keyword,
                                 payment_from=self.pay_from,
                                 payment_to=self.pay_to)
                    how.to_json()
                    how_get = len(how.from_json())
                    if how_get == 0:
                        print("Увы, по такому запросу ничего не найдено, попробуйте снова")
                        exit()
                    num = (num, [how_get])
                    print(f"Получено {how_get} вакансий")
                else:
                    print("\nВы выбрали поиск по всем\n")
                    how_hh = HHJson(keyword=self.keyword,
                                    salary_from=self.pay_from,
                                    salary_to=self.pay_to)
                    how_hh.to_json()
                    how_sj = SJJson(keyword=self.keyword,
                                    payment_from=self.pay_from,
                                    payment_to=self.pay_to)
                    how_sj.to_json()
                    how_get_hh = len(how_hh.from_json())
                    how_get_sj = len(how_sj.from_json())
                    if how_get_hh == 0 and how_get_sj == 0:
                        print("Увы, по такому запросу ничего не найдено, попробуйте снова")
                        exit()
                    elif how_get_hh != 0 and how_get_sj == 0:
                        num = 1
                    elif how_get_hh == 0 and how_get_sj != 0:
                        num = 2
                    print(f"Получено: \n{how_get_hh} вакансий c HH.ru и\n"
                          f"{how_get_sj} вакансий c SJ.ru")
                    num = (num, [how_get_hh, how_get_sj])
            return num


class HowPay:

    def pay_from_(self):
        try:
            pay_min = int(input('Укажите минимальный уровень зарплаты\n'))
            assert pay_min >= 0
        except ValueError:
            print("Не корректный ввод, должно быть целое, не отрицательное число")
            return self.pay_from_()
        except AssertionError:
            print("Значение должно быть не отрицательным")
            return self.pay_from_()
        else:
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
