tasks = ['1. Interstellar','2. Breaking Bad','3. Go and see']

while 1 == 1:
    len_true = len(tasks) + 1
    num = len_true.__str__() + ". "

    print("\n",tasks)

    def task_appends():
        tasks.append(num+input())

    def task_pop(index):
        if 1<=index<=len(tasks):
            tasks.pop(index-1)

    def task_done(index):
        if 1<=index<=len(tasks):
            tasks[index-1]=" (посмотрел) " + tasks[index-1]

    def task_undone(index):
        if 1<=index<=len(tasks):
            if tasks[index-1][:13] == " (посмотрел) ":
                tasks[index-1] = tasks[index-1][13:]
            else:
                print("\nТы не отмечал его как посмотренный")

    choice = input("\nВыберите действие\n1. Отметить фильм как просмотренный\n2. Отметить фильм как непросмотренный\n3. Добавить фильм\n4. Удалить фильм\n5. Выход\n\n")

    if choice == "1":
        index_select = int(input("Выберите фильм: "))
        if index_select != int:
            "bruh"
        task_done(index_select)

    if choice == "2":
        index_select = int(input("Выберите фильм: "))
        if index_select != int:
            "bruh"
        task_undone(index_select)

    if choice == "3": print("Новый фильм: "); task_appends()

    if choice == "4":
        index_select = int(input("Выберите фильм: "))
        if index_select != int:
            "bruh"
        task_pop(index_select)

    if choice == "5":
        exit()