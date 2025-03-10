tasks = []

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
            tasks[index-1]=" (done) " + tasks[index-1]

    def task_undone(index):
        if 1<=index<=len(tasks):
            if tasks[index-1][:8] == " (done) ":
                tasks[index-1] = tasks[index-1][8:]

    choice = input("\nВыберите действие\n1. Отметить задачу как выполненную\n2. Отметить задачу как невыполненную\n3. Добавить задачу\n4. Удалить задачу\n5. Выход\n\n")

    if choice == "1":
        index_select = int(input("Выберите задачу: "))
        task_done(index_select)

    if choice == "2":
        index_select = int(input("Выберите задачу: "))
        task_undone(index_select)

    if choice == "3": print("New task: "); task_appends()

    if choice == "4":
        index_select = int(input("Выберите задачу (номер): "))
        task_pop(index_select)

    if choice == "5":
        exit()