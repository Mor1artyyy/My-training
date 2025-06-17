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
        "number": "89094686965"}
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
else:
    print("Sorry, i dont found anyone(")