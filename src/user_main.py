
from src.user_classes import HowPay, Welcome, GoFind



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
