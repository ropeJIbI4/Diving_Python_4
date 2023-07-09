#Напишите программу банкомат.
#✔ Начальная сумма равна нулю
#✔ Допустимые действия: пополнить, снять, выйти
#✔ Сумма пополнения и снятия кратны 50 у.е.
#✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
#✔ Нельзя снять больше, чем на счёте
#✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
#✔ Любое действие выводит сумму денег
#Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно #сохраняйте все операции поступления и снятия средств в список.

from datetime import date

BANK = 0
COUNT = 0
COMMISSION = 0.015
BONUS = 0.03
TAX = 0.01

list_operation = []

def add_bank(cash: float) -> None:
    global BANK
    global COUNT
    BANK += cash
    COUNT += 1
    if COUNT % 3 == 0:
        BANK = BANK + BONUS * BANK
        print("Кэшбэк! в размере 3% от суммы: ", BONUS * BANK)

def take_bank(cash: float) -> None:
    global BANK
    global COUNT
    BANK -= cash
    COUNT += 1

    if cash * COMMISSION < 30:
        BANK -= 30
        print("Удержанны % :",30)
    elif cash * COMMISSION > 600:
        BANK -= 600
        print("Удержанны %: ", 600)
    else:
        BANK -= cash * COMMISSION
        print("Удержанны %: ", cash * COMMISSION)
    if COUNT % 3 == 0:
        BANK = BANK + BONUS * BANK
        print("Кэшбэк! в размере 3% от суммы: ", BONUS * BANK)

def exit_bank():
        print("\nДо свидания!\n")
        exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму(кратную 50 у.е)\n"))
        if cash % 50 == 0:
            return cash

def start():

    global BANK
    global TAX



    while True:
        action = input("Операции:\n1-Снятие \n2-Пополнение\n3-Состояние баланса\n4-История операций\n5-Забрать карту\n")

        if action == '1':
            if BANK > 5_000_000:
                BANK = BANK - BANK * TAX
                print("!Внимание!\nУдержен налог на богатство!: ", BANK * TAX)
            cash = check_bank()
            if cash < BANK:
                take_bank(cash)

                list_operation.append([str(date.today()), -1 * cash])
            else:
                print("Баланс равен = 0\n")
            if BANK > 5_000_000:
                BANK = BANK - BANK * TAX
                print("Внимание!\nУдержен налог на богатство!: ", BANK * TAX)
            print("Баланс = ", BANK)
        elif action == '2':
            cash = check_bank()
            add_bank(cash)
            if BANK > 5_000_000:
                BANK = BANK - BANK * TAX
                print("Внимание!\nУдержен налог на богатство!: ", BANK * TAX)
            print("Баланс = ", BANK)

            list_operation.append([str(date.today()), cash])

        elif action == '3':
            print("Баланс = ", BANK)
        elif action == '4':
            print(list_operation)
        else:
            exit_bank()

start()