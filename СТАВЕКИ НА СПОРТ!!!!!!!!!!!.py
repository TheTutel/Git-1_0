import random

def casino():
    print("НЕ СТАВЬТЕ НА СПОРТ!!!!! ВЫ ВСЕ ПРОСРЁТЕ!!!")

cash = 10000

select = 'yes'

while select == 'yes':
    while cash > 0:
        while True:
            bet = int(input("Ставка: "))
            if bet < 0:
                print("Поставьте число больше нуля!")
            if bet > cash:
                print("Поставь число меньше или равное балансу! Баланс:",cash)
            else: break

        number = random.randint(1,100)

        tries_select = int(input("Выберите количество попыток (не пыток): "))

        while tries_select > 0:
            choice = int(input("Ваш выбор: - "))
            if choice == number:
                print("Ты победил!!!        ヾ(≧▽≦*)o")
                cash = (cash + bet * (10 / tries_select))//1
                print(cash)
                select = input("Хотите ещё раз? yes/no\n")
            if choice != number:
                if choice > number:
                    print("Меньше!!!")
                if choice < number:
                    print("Больше!!!")
                if choice - number > 0:
                    if choice - number < 11:
                        if choice - number < 2:
                            print("Очень близко")
                        else:
                            print("Близко")
                if number - choice > 0:
                    if number - choice < 11:
                        if number - choice < 2:
                            print("Очень близко")
                        else:
                            print("Близко")
                tries_select = tries_select - 1
                if tries_select == 0:
                    print("Закончились попытки!")
                    cash = cash - bet
                    print(cash)
if cash == 0:
    print("bruh, you lost all your money and you're kicked from lobby")
    casino()
if cash > 0:
    exit()