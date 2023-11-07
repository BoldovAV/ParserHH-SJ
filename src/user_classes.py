from src.node import LinkList
# from src.user_main import chose
from src.work_with_json import HHJson, SJJson


class Welcome:

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
            print("Не корректный ввод")
            return False
        else:
            if num == 0:
                print('Всего хорошего!')
                exit()
            else:
                if num == 1:
                    print("Вы выбрали поиск по HeadHunter.ru")
                    self.ask_key_pay()
                elif num == 2:
                    print("Вы выбрали поиск по SuperJob.ru")
                else:
                    print("Вы выбрали поиск по всем")
                return num

    def ask_key_pay(self):
        try:
            profession = input("Введите название профессии по которой осуществлять поиск\n")
            pay_form = int(input('Укажите минимальный уровень зарплаты'))
            pay_to = int(input('Укажите максимальный уровень зарплаты'))
        except ValueError:
            print("Не корректный ввод")
            return False
        else:
            pass


# prof = LinkList()
# if chose == 1:
#     site = HHJson()
#     site.to_json()
#     for i in range(len(site.from_json())):
#         prof.insert_at_end(data)
# elif chose == 2:
#     site = SJJson()
#     site.to_json()
#     all_vacancy = site.from_json()
#     for i in range(len(site.from_json())):
#         prof.insert_at_end(data)
# else:
#     site1 = HHJson()
#     for i in range(len(site1.from_json())):
#         prof.insert_at_end(data)
#     site2 = SJJson()
#     for i in range(len(site2.from_json())):
#         prof.insert_at_end(data)
