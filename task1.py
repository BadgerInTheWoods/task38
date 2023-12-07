# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from os.path import exists
from csv import DictReader, DictWriter
class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def getinfo():
    firstname = 'Ivan'
    lastname = 'Ivanov'

    isvalidphone = False
    isvalidname = False
    while not isvalidname:
        try:
            name = firstname = input("insert name")
            if len(firstname) < 2:
                raise NameError("invaliv name")
            else:
                isvalidname = True
        except NameError as err:
            print(err)
            continue
    while not isvalidphone:
        try:
            phonenumber = int(input("insert phone number "))
            if len(str(phonenumber)) != 11:
                raise LenNumberError("Incorrect number lenght")
            else:
                isvalidphone = True
        except ValueError:
            print("invalid number")
            continue
        except LenNumberError as err:
            print (err)
            continue

    return [firstname, lastname, phonenumber]

def createfile(filename): # with - менеджер контекста
    with open(filename, "w", encoding="utf-8") as data:
        fwriter = DictWriter(data, fieldnames=["Name", "Surname", "Phone number"])
        fwriter.writeheader()

def readfile(filename):
    with open(filename, "r", encoding="utf-8") as data:
        freader = DictReader(data)
        return list(freader)

def writefile(filename, lst):
    res = readfile(filename)
    for elem in res:
        if elem["Phone number"] == str(lst[2]):
            print("already exist")
            return
    obj = {"Name": lst[0], "Surname": lst[1], "Phone number": lst[2]}
    res.append(obj)
    with open(filename, "w", encoding="utf-8", newline="") as data:
        fwriter = DictWriter(data, fieldnames=["Name", "Surname", "Phone number"])
        fwriter.writeheader()
        fwriter.writerows(res)


filename = "Phone.csv"

def main():
    while True:
        command = input("Insert command: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                createfile(filename)
            writefile(filename, getinfo())
        elif command == "r":
            if not exists(filename):
                print("file do not exist")
                continue
            print(readfile(filename))

main()


#HW "Дополнить справочник возможностью копирования данных
#  из одного файла в другой. Пользователь вводит номер строки,
#  которую необходимо перенести из одного файла в другой."
# отсылать ссылку на пулл реквест, пулл делается в свой репо, инструкция на первом уроке