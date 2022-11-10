from validators import url
from pyfiglet import figlet_format
from requests import get
from colorama import init, Fore, Back, Style
from re import findall

firstpronouns = ["я", "мы"]
otherpronouns = ["ты", "вы", "он", "она", "оно", "они"]


def checkUrl(pageurl):
    return url(pageurl)


def checkText(text):
    formatted = text.lower()

    firstperson = otherperson = 0

    words = findall(r'\b[ЁёА-я]+\b', formatted)

    for word in words:
        firstperson += int(word in firstpronouns)
        otherperson += int(word in otherpronouns)

    return firstperson > otherperson, firstperson, otherperson


def main():
    # Логотип команды
    logo = figlet_format("NatusCoders")
    print(Style.BRIGHT + logo[:logo.rfind("\n", 0, -2):], end="\n")
    print("ЯМы тестировщики by NatusCodersTeam\n" + Style.RESET_ALL)

    # Ввод
    pageurl = input("Введите адрес сайта (http:// | https://): ")
    while not checkUrl(pageurl):  # Проверка на правильность ввода
        print(Back.LIGHTRED_EX + "Неправильно введён адрес сайта, попробуйте ещё раз" + Back.RESET)
        pageurl = input("Введите адрес сайта (http:// | https://): ")

    # Получение текста из ссылки на сайт
    text = get(pageurl).text
    # Получение результата проверки
    result, firstperson, otherperson = checkText(text)

    # Вывод
    print('\n' + (Back.LIGHTGREEN_EX + Style.BRIGHT + "Сайт прошел проверку." if result
                  else Back.RED + Style.BRIGHT + "Сайт не прошел проверку") + Back.RESET + Style.RESET_ALL)
    print(f"Колличество личных местоимений 1-го лица:\t{firstperson}")
    print(f"Колличество остальных личных местоимений:\t{otherperson}")


if __name__ == '__main__':
    init()  # Инициализация цвета в консоли
    main()  # Основная функция
