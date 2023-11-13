from src.treatment import HeadHuntSearch, SuperJobSearch
from src.work_with_json import HHJson, SJJson


class Welcome:
    """Стартовый класс, который спрашивает по каким сайтам искать,
    и осуществляет поиск по выбранным сайтам, записывая результат в файл json"""

    def __init__(self, keyword, pay_from, pay_to):
        self.keyword = keyword  # Ключевое слово (фраза), по которому осуществляется поиск
        self.pay_from = pay_from  # Желаемая минимальная оплата
        self.pay_to = pay_to  # Желаемая максимальная оплата

    def site_search(self):
        """Метод, определяющий по каким сайтам, искать.
        Содержит проверки на корректность вводимых данных"""
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
                    if how_get == 0:  # В случае, если ни одной вакансии не найдено,
                        # об этом сообщается, а программа завершается
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
                    if how_get_hh == 0 and how_get_sj == 0:  # Если по одному из сайтов
                        # не найдено вакансий, дальнейшая работа идет с тем, на котором что-то нашлось
                        print("Увы, по такому запросу ничего не найдено, попробуйте снова")
                        exit()
                    elif how_get_hh != 0 and how_get_sj == 0:
                        num = (1, [how_get_hh])
                    elif how_get_hh == 0 and how_get_sj != 0:
                        num = (2, [how_get_sj])
                    else:
                        num = (num, [how_get_hh, how_get_sj])
                    print(f"Получено: \n{how_get_hh} вакансий c HH.ru\n"
                          f"{how_get_sj} вакансий c SJ.ru")
            return num


class HowPay:
    """Класс спрашивающий, какую оплату (мин/макс) пользователь хотел бы.
    В нем устроенна проверка на корректность вводимых данных (type: int >= 0)"""

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


class GoFind:
    """Класс для обработки полученных запросов"""
    all_vak_hh = []
    all_vak_sj = []

    def __init__(self, chose_site):
        self.chose_site = chose_site

    def all_site(self, list_site):
        """Метод по работе со всеми сайтами"""
        while True:
            try:
                how_get_hh = list_site[0]
                how_get_sj = list_site[1]

                for i in range(how_get_hh):
                    self.all_vak_hh.append((HeadHuntSearch(i)))

                for i in range(how_get_sj):
                    self.all_vak_sj.append((SuperJobSearch(i)))
                # Упрощенная проверка того, что вводит пользователь (главное чтобы число,
                # если ввести отрицательное, возьмется по модулю
                how_vak = abs(int(input("По сколько вакансий с каждого сайта вы хотите посмотреть?\n")))

            except ValueError:
                print("Должно быть число")
            else:
                sort = input("Отсортировать по среднему уровню зарплаты? (Да/Нет)\n").lower()
                if sort in ['да', 'yes']:
                    self.all_vak_hh, self.all_vak_sj = self.sort_vak(self.chose_site)
                else:
                    print("Как хотите\n")
                if how_vak <= how_get_hh and how_vak <= how_get_sj:  # Проверка на случай,
                    # если введенное число будет больше числа полученных вакансий. В таком
                    # случае будут показаны все
                    how_vak_hh = how_vak
                    how_vak_sj = how_vak
                if how_vak > how_get_hh:
                    how_vak_hh = how_get_hh
                if how_vak > how_get_sj:
                    how_vak_sj = how_get_sj
                break
        print("HH.ru:\n")
        for i in range(how_vak_hh):
            print(f'{self.all_vak_hh[i]}\n')
        print("SJ.ru:\n")
        for i in range(how_vak_sj):
            print(f'{self.all_vak_sj[i]}\n')

    def hh_ru(self, list_site):
        """Метод по работе только с HH.ru"""
        while True:
            try:
                how_get_hh = list_site[0]

                for i in range(how_get_hh):
                    self.all_vak_hh.append((HeadHuntSearch(i)))

                how_vak = abs(int(input("Сколько вакансий вы хотите посмотреть?\n")))
            except ValueError:
                print("Должно быть число")
            else:
                sort = input("Отсортировать по среднему уровню зарплаты? (Да/Нет)\n").lower()
                if sort in ['да', 'yes']:
                    self.all_vak_hh = self.sort_vak(self.chose_site)
                else:
                    print("Как хотите\n")
                if how_vak > how_get_hh:
                    how_vak_hh = how_get_hh
                else:
                    how_vak_hh = how_vak
                break
        print("HH.ru:\n")
        for i in range(how_vak_hh):
            print(f'{self.all_vak_hh[i]}\n')

    def sj_ru(self, list_site):
        """Метод по работе только с SJ.ru"""
        while True:
            try:
                how_get_sj = list_site[0]

                for i in range(how_get_sj):
                    self.all_vak_sj.append((SuperJobSearch(i)))

                how_vak = abs(int(input("Сколько вакансий вы хотите посмотреть?\n")))

            except ValueError:
                print("Должно быть число")
            else:
                sort = input("Отсортировать по среднему уровню зарплаты? (Да/Нет)\n").lower()
                if sort in ['да', 'yes']:
                    self.all_vak_sj = self.sort_vak(self.chose_site)
                else:
                    print("Как хотите\n")
                if how_vak > how_get_sj:
                    how_vak_sj = how_get_sj
                else:
                    how_vak_sj = how_vak
                break
        print("SJ.ru:\n")
        for i in range(how_vak_sj):
            print(f'{self.all_vak_sj[i]}\n')

    def sort_vak(self, site):
        """Метод для сортировки полученных вакансий по среднему уровню оплаты"""
        if site == 1:
            all_sort_hh = sorted(self.all_vak_hh, key=lambda x: x.avg_payment(), reverse=True)
            return all_sort_hh
        elif site == 2:
            all_sort_sj = sorted(self.all_vak_sj, key=lambda x: x.avg_payment(), reverse=True)
            return all_sort_sj
        else:
            all_sort_hh = sorted(self.all_vak_hh, key=lambda x: x.avg_payment(), reverse=True)
            all_sort_sj = sorted(self.all_vak_sj, key=lambda x: x.avg_payment(), reverse=True)
            return all_sort_hh, all_sort_sj

    # sort = input("Отсортировать по среднему уровню зарплаты? (Да/Нет)\n").lower()
    # if sort == "да":
    #     if chose_site == 3:
    #         all_sort_hh = sorted(all_vak_hh, key=lambda x: x.avg_payment(), reverse=True)
    #         all_sort_sj = sorted(all_vak_sj, key=lambda x: x.avg_payment(), reverse=True)
    #         print("HH.ru:\n")
    #         for i in range(how_vak_hh):
    #             print(f'{all_sort_hh[i]}\n')
    #         print("SJ.ru:\n")
    #         for i in range(how_vak_sj):
    #             print(f'{all_sort_sj[i]}\n')
    #     elif chose_site == 1:
    #         all_sort_hh = sorted(all_vak_hh, key=lambda x: x.avg_payment(), reverse=True)
    #         for i in range(how_vak_hh):
    #             print(f'{all_sort_hh[i]}\n')
    #
    #     else:
    #         all_sort_sj = sorted(all_vak_sj, key=lambda x: x.avg_payment(), reverse=True)
    #         for i in range(how_vak_sj):
    #             print(f'{all_sort_sj[i]}\n')
    #
    #     # all_vak_hh.sort(key=lambda x: x = statistics.mean(self.pay_from, self.pay_to))
    #     # all_vak_sj = []
    # else:
    #     print("Ну нет, так нет")
    #     if chose_site == 3:
    #         print("HH.ru:\n")
    #         for i in range(how_vak_hh):
    #             print(f'{all_vak_hh[i]}\n')
    #         print("SJ.ru:\n")
    #         for i in range(how_vak_sj):
    #             print(f'{all_vak_sj[i]}\n')
    #     elif chose_site == 1:
    #         for i in range(how_vak_hh):
    #             print(f'{all_vak_hh[i]}\n')
    #
    #     else:
    #
    #         for i in range(how_vak_sj):
    #             print(f'{all_vak_sj[i]}\n')
