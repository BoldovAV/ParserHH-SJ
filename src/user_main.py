from operator import itemgetter

from src.treatment import HeadHuntSearch, SuperJobSearch
from src.user_classes import HowPay, Welcome
from src.work_with_json import HHJson, SJJson

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

chose_site, how_get = Welcome(keyword=profession, pay_from=pay_from, pay_to=pay_to).site_search()

all_vak_hh = []
all_vak_sj = []

while True:
    try:
        if chose_site == 3:

            how_get_hh = how_get[0]
            how_get_sj = how_get[1]

            for i in range(how_get_hh):
                all_vak_hh.append((HeadHuntSearch(i)))

            for i in range(how_get_sj):
                all_vak_sj.append((SuperJobSearch(i)))

            how_vak = abs(int(input("По сколько вакансий с каждого сайта вы хотите посмотреть?\n")))

            if how_vak <= how_get_hh and how_vak <= how_get_sj:
                how_vak_hh = how_vak
                how_vak_sj = how_vak
            if how_vak > how_get_hh:
                how_vak_hh = how_get_hh
            if how_vak > how_get_sj:
                how_vak_sj = how_get_sj

        else:
            how_get = how_get[0]
            how_vak = abs(int(input("Сколько вакансий вы хотите посмотреть?\n")))

            if chose_site == 1:

                for i in range(how_get):
                    all_vak_hh.append((HeadHuntSearch(i)))

                if how_vak > how_get:
                    how_vak_hh = how_get
                else:
                    how_vak_hh = how_vak

            else:

                for i in range(how_get):
                    all_vak_sj.append((SuperJobSearch(i)))

                if how_vak > how_get:
                    how_vak_sj = how_get
                else:
                    how_vak_sj = how_vak

    except ValueError:
        print("Должно быть число")
    else:
        break

sort = input("Отсортировать по среднему уровню зарплаты? (Да/Нет)").lower()
if sort == "да":
    sort = 1
    if chose_site == 3:
        all_sort_hh = sorted(all_vak_hh, key=lambda x: x.avg_payment)
        all_sort_sj = sorted(all_vak_sj, key=lambda x: x.avg_payment)
    elif chose_site == 1:
        all_sort_hh = sorted(all_vak_hh, key=lambda x: x.avg_payment)
    else:
        all_sort_sj = sorted(all_vak_sj, key=lambda x: x.avg_payment)
    # all_vak_hh.sort(key=lambda x: x = statistics.mean(self.pay_from, self.pay_to))
    # all_vak_sj = []
else:
    print("Ну нет, так нет")
    sort = 0


# for site in where:
#     for i in range(len(site.from_json())):
#         all_vak.append(site(i))
