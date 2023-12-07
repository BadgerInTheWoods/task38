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
    isvalidsurname = False

    while not isvalidname:
        try:
            name = firstname = input("insert name ")
            if len(firstname) < 2:
                raise NameError("invalid name ")
            else:
                isvalidname = True
        except NameError as err:
            print(err)
            continue

    while not isvalidsurname:
        try:
            surname = lastname = input("insert surname ")
            if len(lastname) < 2:
                raise NameError("invalid surname ")
            else:
                isvalidsurname = True
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

def copyline(filename):
    c = readfile(filename)
    print("here are the copying options {}".format(c))
    while True:
        whichone = str(input("insert phone number of a person you want to copy "))
        for i in c:
            if whichone in i.values():
                return [k for k in i.values()]
            else:
                continue
        print("no such person in file")
     
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


#filename = input("insert file name ")

def main():
    while True:
        command = input("Insert command: ")
        if command == "q":
            break
        elif command == "w":
            filename = input("insert file name ")
            if not exists(filename):
                createfile(filename)
            writefile(filename, getinfo())
        elif command == "c":
            filename = input("insert file name from which you want to copy data ")
            newfilename = input("insert file name where you want your files to be pasted ")
            if not exists(newfilename):
                createfile(newfilename)
            writefile(newfilename, copyline(filename))
        elif command == "r":
            filename = input("insert file name ")
            if not exists(filename):
                print("file do not exist")
                continue
            print(readfile(filename))

main()



#HW "Дополнить справочник возможностью копирования данных
#  из одного файла в другой. Пользователь вводит номер строки,
#  которую необходимо перенести из одного файла в другой."
# отсылать ссылку на пулл реквест, пулл делается в свой репо, инструкция на первом уроке

