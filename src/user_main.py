from src.user_classes import HowPay, Welcome

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

chose_site = Welcome(keyword=profession, pay_from=pay_from, pay_to=pay_to).site_search()

if chose_site == 3:
    how_vak = input("По сколько вакансий с каждого сайта вы хотите посмотреть?\n")
else:
    how_vak = input("Сколько вакансий вы хотите посмотреть?\n")
