from src.user_classes import Welcome

print("Добрый день. Данная программа помогает парсить"
      " сайты для поиска работы.")

chose = False
while not chose:
    chose_site = Welcome()
    chose = chose_site.site_search


print("[eq")
