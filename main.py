alex = {
    "Abakumova":{
        "lecturer": "Абакумова Елена Викторовна",
        "department": "Кафедра изобразительного искусства и дизайна",
        "email": "Abakumova@gmail.com",
        "academicDegree": "Кандидат педагогических наук",
        "academicTitle": "Доцент",
        "number": "89999999999"},

    "Aberegova":{
        "lecturer": "Абрегова Жанна Османовна",
        "department": "Кафедра отечественной истории, историографии, теории и методологии",
        "email": "Aberegova@yandex.ru",
        "academicDegree": "Кафедра изобразительного искусства и дизайна",
        "academicTitle": "Доцент",
        "number": "89888888888"},

    'Belova':{
        "lecturer": "Белова Дина Владимировна",
        "department": "Институт физической культуры и Дзюдо",
        "email": "dikabelova65@yandex.ru",
        "academicDegree": "Кандидат педагогических наук",
        "academicTitle": "Доцент",
        "number": "89094686965"},

    "Sitnikova":{
        "Фамилия": "Ситникова",
        "Имя": "Юлиана",
        "Отчество": "Евгеньевна",
        "Дата рождения": "06.05.2006г",
        "Полных лет": "19",
        "Прописка": "г.Майкоп, ул.Шовгенова 342",
        "Место обучения": "АГУ",
        "Факультет": "Факультет иностранных языков",
        "Курс": "1",
        "Статус": "В отношениях с......",
        "Интересные факты": "Любит смешариков. Имеет 20+ любовников((("}
        }

print("Привет!!!\n"
      "Кого Ищем?")
user_data = input('Enter teachers name: ')
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if user_data == 'Abakumova':
    print("Преподаватель: ", alex["Abakumova"]["lecturer"])
    print("Факультет: ", alex["Abakumova"]["department"])
    print("Почта: ", alex["Abakumova"]["email"])
    print("Научная степень: ", alex["Abakumova"]["academicDegree"])
    print("Должность: ", alex["Abakumova"]["academicTitle"])
    print("Номер: ", alex["Abakumova"]["number"])

elif user_data == 'Aberegova':
    print("Преподаватель: ", alex["Aberegova"]["lecturer"])
    print("Факультет: ", alex["Aberegova"]["department"])
    print("Почта: ", alex["Aberegova"]["email"])
    print("Научная степень: ", alex["Aberegova"]["academicDegree"])
    print("Должность: ", alex["Aberegova"]["academicTitle"])
    print("Номер: ", alex["Aberegova"]["number"])

elif user_data == 'Belova':
    print("Преподаватель: ", alex["Belova"]["lecturer"])
    print("Факультет: ", alex["Belova"]["department"])
    print("Почта: ", alex["Belova"]["email"])
    print("Научная степень: ", alex["Belova"]["academicDegree"])
    print("Должность: ", alex["Belova"]["academicTitle"])
    print("Номер: ", alex["Belova"]["number"])

elif user_data == 'Sitnikova':
    print("Фамилия: ", alex["Sitnikova"]["Фамилия"])
    print("Имя: ", alex["Sitnikova"]["Имя"])
    print("Отчество: ", alex["Sitnikova"]["Отчество"])
    print("Дата рождения: ", alex["Sitnikova"]["Дата рождения"])
    print("Полных лет: ", alex["Sitnikova"]["Полных лет"])
    print("Прописка: ", alex["Sitnikova"]["Прописка"])
    print("Место обучения: ", alex["Sitnikova"]["Место обучения"])
    print("Факультет: ", alex["Sitnikova"]["Факультет"])
    print("Курс: ", alex["Sitnikova"]["Курс"])
    print("Статус: ", alex["Sitnikova"]["Статус"])
    print("Интересные факты: ", alex["Sitnikova"]["Интересные факты"])
else:
    print("Sorry, i dont found anyone(")