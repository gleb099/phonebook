from typing import List, Tuple


class Phonebook:
    """
    Класс для работы с телефонным справочником.

    Args:
        phonebook_path (str): Путь к файлу, используемому для хранения записей справочника.
        page_records (int, optional): Количество записей, отображаемых на одной странице. По умолчанию 5.

    Attributes:
        phonebook_path (str): Путь к файлу справочника.
        page_records (int): Количество записей на одной странице.
    """

    def __init__(self, phonebook_path: str, page_records: int = 5):
        self.phonebook_path = phonebook_path
        self.page_records = page_records

    def write(self, records: list):
        """
        Записывает список записей в файл справочника.

        Args:
            records (list): Список записей для записи в файл.
        """
        with open(self.phonebook_path, 'w', encoding="UTF-8") as f:
            f.writelines(records)

    def read(self) -> List[str]:
        """
        Считывает записи из файла справочника.

        Returns:
            list: Список строк, представляющих записи из справочника.
        """
        with open(self.phonebook_path, 'r', encoding="UTF-8") as f:
            records = f.readlines()
        return records

    def display(self, start: int):
        """
        Отображает записи из справочника постранично.

        Args:
            start (int): Номер страницы, с которой начинать отображение.
        """
        records = self.read()
        k = 0
        for i in range((start - 1) * self.page_records, len(records)):
            record = records[i]
            print(f"{i + 1}. {record.splitlines()[0]}")
            k += 1
            if k == 5:
                cnext = int(input("\n1. Дальше\n2. Выйти из просмотра\nВыбор: "))
                print()
                if cnext == 1:
                    k = 0
                    continue
                else:
                    break

    def add_record(self, record: str):
        """
        Добавляет новую запись в справочник.

        Args:
            record (str): Строка с данными новой записи.
        """
        with open(self.phonebook_path, 'a', encoding="UTF-8") as f:
            f.write(record + '\n')

    def edit_record(self, ind: int):
        """
        Редактирует существующую запись в справочнике.

        Args:
            ind (int): Индекс записи для редактирования.
        """
        ind -= 1
        records = self.read()
        record = records[ind].split(',')
        print(f"1. Фамилия: {record[0]}")
        print(f"2. Имя: {record[1]}")
        print(f"3. Отчество: {record[2]}")
        print(f"4. Организация: {record[3]}")
        print(f"5. Рабочий телефон: {record[4]}")
        print(f"6. Личный телефон: {record[5]}")
        while True:
            number = int(input("Что необходимо изменить? (номер): "))
            change = input("Введите изменения: ")
            record[number - 1] = change
            done = int(input("1. Продолжить изменения\n2. Завершение редактирования\nВыбор: "))
            if done == 2:
                break
        records[ind] = ",".join(record)
        self.write(records)

    def search(self, query: str) -> Tuple[List[str], List[int]]:
        """
        Поиск записей в справочнике на основе запроса.

        Args:
            query (str): Запрос для поиска в записях справочника.

        Returns:
            tuple: Кортеж, содержащий два списка.
                Первый список содержит совпадающие записи в виде строк.
                Второй список содержит индексы совпадающих записей.
        """
        records = self.read()
        res = list()
        inds = list()
        for i in range(len(records)):
            if query.lower() in records[i].lower():
                res.append(records[i])
                inds.append(i + 1)
        return res, inds


def main():
    phonebook = Phonebook('phonebook.txt')
    while True:
        print("1. Просмотреть справочник")
        print("2. Добавить контакт")
        print("3. Редактировать контакт")
        print("4. Поиск по справочнику")
        print("5. Выход")

        choice = int(input("Выберите действие(номер): ").split()[0])
        print()

        match choice:
            case 1:
                start = int(input("Введите номер страницы: "))
                phonebook.display(start)
                print("Конец просмотра")
            case 2:
                last_name = input("Фамилия: ")
                name = input("Имя: ")
                patronymic = input("Отчество: ")
                company = input("Организация: ")
                work_phone = input("Рабочий телефон: ")
                personal_phone = input("Личный телефон: ")
                record = f"{last_name},{name},{patronymic},{company},{work_phone},{personal_phone}"
                phonebook.add_record(record)
                print("Запись добавлена")
            case 3:
                search = int(
                    input("Найти контакт для изменения\n1. По индексу контакта\n2. Использовать поиск\nВыбор: "))
                if search == 1:
                    phonebook.edit_record(int(input("Введите индекс контакта: ")))
                else:
                    query = input("Введите запрос для поиска: ")
                    results = phonebook.search(query)
                    if len(results[0]) == 0:
                        print("По запросу ничего не найдено")
                    elif len(results[0]) == 1:
                        print("По запросу найден один контакт:")
                        phonebook.edit_record(results[1][0])
                    else:
                        print("По запросу найдено несколько контактов:")
                        for i in range(len(results[0])):
                            print(f"{results[1][i]}. ", results[0][i].split("\n")[0])
                        ind = int(input("Контакт для изменения (его индекс): "))
                        phonebook.edit_record(ind)
                print("Контакт изменен")
            case 4:
                query = input("Введите запрос для поиска: ")
                results = phonebook.search(query)
                if results:
                    print("Результаты поиска:")
                    for i in range(len(results[0])):
                        print(f"{results[1][i]}. ", results[0][i].split("\n")[0])
                else:
                    print("Ничего не найдено")
            case 5:
                print("Справочник закрыт")
                break
            case _:
                print("Неверно")
        print()


if __name__ == '__main__':
    main()
