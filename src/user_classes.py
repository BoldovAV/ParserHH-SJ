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
                elif num == 2:
                    print("Вы выбрали поиск по SuperJob.ru")
                else:
                    print("Вы выбрали поиск по всем")
                return num
