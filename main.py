n = int(input("Введите длину списка: "))
user_list = []
i = 0
while i < n:
    alex = "Введите элемент №" + str(i + 1) + ": "
    user_list.append(input(alex))
    i += 1
    print(user_list)