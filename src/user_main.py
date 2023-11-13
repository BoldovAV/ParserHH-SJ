# from operator import itemgetter
#
# from src.treatment import HeadHuntSearch, SuperJobSearch
from src.user_classes import HowPay, Welcome, GoFind

# from src.work_with_json import HHJson, SJJson

if __name__ == "__main__":

    print("Добрый день. Данная программа помогает парсить"
          " сайты для поиска работы.")
    # Запрос слова/фразы, по которой будет осуществлен поиск
    profession = input("Введите название профессии по которой осуществлять поиск\n").capitalize()
    pay = HowPay()
    pay_from = pay.pay_from_()  # Запрос минимальной оплаты, будет зациклен пока
    # не будут введены корректные значения
    pay_to = pay.pay_to_()  # Также для максимальной
    while True:  # Проверка чтобы максимум был больше минимума. Или один из пределов 0
        if pay_from <= pay_to or pay_from == 0 or pay_to == 0:
            break
        else:
            print("Минимальная оплата должна быть меньше максимальной,"
                  " или одна из них должны быть 0 (не указана).\n"
                  "Попробуйте еще раз\n")
            pay_from = pay.pay_from_()
            pay_to = pay.pay_to_()
    # Создание экземпляра класса по поиску
    chose_site, how_get = Welcome(keyword=profession, pay_from=pay_from, pay_to=pay_to).site_search()
    # Создание экземпляра класса для обработки полученных данных, также
    # с определением с какими сайтами работать, если по одному из выбранных получено 0 вакансий
    start_find = GoFind(chose_site)
    if chose_site == 3:
        start_find.all_site(how_get)
    elif chose_site == 1:
        start_find.hh_ru(how_get)
    else:
        start_find.sj_ru(how_get)

# GoFind()
#
# all_vak_hh = []
# all_vak_sj = []
# how_vak_hh = 0
# how_vak_sj = 0
#
# while True:
#     try:
#         if chose_site == 3:
#
#             how_get_hh = how_get[0]
#             how_get_sj = how_get[1]
#
#             for i in range(how_get_hh):
#                 all_vak_hh.append((HeadHuntSearch(i)))
#
#             for i in range(how_get_sj):
#                 all_vak_sj.append((SuperJobSearch(i)))
#
#             how_vak = abs(int(input("По сколько вакансий с каждого сайта вы хотите посмотреть?\n")))
#
#             if how_vak <= how_get_hh and how_vak <= how_get_sj:
#                 how_vak_hh = how_vak
#                 how_vak_sj = how_vak
#             if how_vak > how_get_hh:
#                 how_vak_hh = how_get_hh
#             if how_vak > how_get_sj:
#                 how_vak_sj = how_get_sj
#
#         else:
#             how_get = how_get[0]
#             how_vak = abs(int(input("Сколько вакансий вы хотите посмотреть?\n")))
#
#             if chose_site == 1:
#
#                 for i in range(how_get):
#                     all_vak_hh.append((HeadHuntSearch(i)))
#
#                 if how_vak > how_get:
#                     how_vak_hh = how_get
#                 else:
#                     how_vak_hh = how_vak
#
#             else:
#
#                 for i in range(how_get):
#                     all_vak_sj.append((SuperJobSearch(i)))
#
#                 if how_vak > how_get:
#                     how_vak_sj = how_get
#                 else:
#                     how_vak_sj = how_vak
#
#     except ValueError:
#         print("Должно быть число")
#     else:
#         break
#
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
