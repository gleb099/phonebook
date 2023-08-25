# phonebook

Класс Phonebook:

1. Конструктор __init__ инициализирует путь к файлу справочника и количество записей, отображаемых на одной странице.
2. Метод write записывает список записей в файл справочника.
3. Метод read считывает записи из файла справочника и возвращает их в виде списка строк.
4. Метод display отображает записи справочника постранично. Пользователь может переходить к следующей странице или выйти из просмотра.
5. Метод add_record добавляет новую запись в справочник.
6. Метод edit_record редактирует существующую запись в справочнике, позволяя пользователю выбрать, какую информацию изменить.
7. Метод search выполняет поиск записей в справочнике на основе запроса, возвращает совпадающие записи и их индексы.

Функция main:

1. Создает экземпляр класса Phonebook с указанием пути к файлу справочника.
В бесконечном цикле предоставляет пользователю меню действий:
1. Просмотреть справочник, где пользователь указывает номер страницы для отображения записей.
2. Добавить контакт, запрашивая данные о новом контакте и добавляя их в справочник.
3. Редактировать контакт, позволяя пользователю выбрать контакт для редактирования по индексу или через поиск.
4. Поиск по справочнику, где пользователь вводит запрос и получает результаты поиска.
5. Завершить работу.

Все действия пользователя реализованы с использованием конструкции match, где пользовательский выбор определяет, какое действие будет выполнено. Каждая операция взаимодействует с методами класса Phonebook для выполнения соответствующих задач.