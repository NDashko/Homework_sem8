# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.

def open_file():
    try:
        with open(r'phonebook.txt', 'r', encoding='UTF-8') as file:
            phonebook = file.readlines()
    except FileNotFoundError:
        phonebook = []
    return phonebook



def show_contacts(phonebook):
    if not phonebook:
        print('Справочник пуст.')
    else:
        print('Контакты: ')
        for contacts in phonebook:
            print(contacts.strip())


def save_file_phonebook(phonebook):
    with open(r'phonebook.txt', 'w', encoding='UTF-8') as file:
        file.writelines(phonebook)

def add_contact(phonebook):
    full_name = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    contact = f"ФИО: {full_name} Телефон: {phone_number} \n"
    phonebook.append(contact)
 


def update_contact(phonebook):
    query = input('Введите имя или фамилию контакта для изменения: ')
    found_contacts = []
    for contact in phonebook:
        if query.lower() in contact.lower():
            found_contacts.append(contact)
    if found_contacts:
        print('Найденные контакты: ')
        for index, contact in enumerate(found_contacts):
            print(f'{index + 1}. {contact.strip()}')
        choice = input('Выберите номер контакта для изменения: ')
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            contact = found_contacts[int(choice) - 1]
            print(f'Выбран контакт:\n{contact.strip()}')
            new_phone_number = input('Введите новый номер телефона (оставьте пустым, если не нужно изменять): ')
            if new_phone_number:
                contact = contact.replace(contact.split(':')[2], f' {new_phone_number} ')
            phonebook.remove(found_contacts[int(choice) - 1])
            phonebook.append(contact)
            print('Контакты успешно изменен.')
        else:
            print('Неверный выбор контакта.')
    else:
        print("Контакты не найдены.")


def delete_contact(phonebook):
    query = input('Введите имя или фамилию контакта для изменения: ')
    found_contacts = []
    for contact in phonebook:
        if query.lower() in contact.lower():
            found_contacts.append(contact)
    if found_contacts:
        print('Найденные контакты: ')
        for index, contact in enumerate(found_contacts):
            print(f'{index + 1}. {contact.strip()}')
        choice = input('Выберите номер контакта для удаления: ')
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            contact = found_contacts[int(choice) - 1]
            print(f'Выбран контакт для удаления: \n{contact.strip()}')
            phonebook.remove(found_contacts[int(choice) - 1])
            print('Контакт успешно удален.')
        else:
            print('Неверный выбор контакта.')
    else:
        print('Контакт не найден')


def main():
    phonebook = open_file()

    while True:
        
        print('1. Показать контакты')
        print('2. Добавить контакт')
        print('3. Изменить контакт')
        print('4. Удалить контакт')
        print('5. Сохранить контакт')
        print('6. Выход')

        choice = input('Выберите номер действия: ')

        if choice == '1':
            show_contacts(phonebook)
        elif choice == '2':
            add_contact(phonebook)
        elif choice == '3':
            update_contact(phonebook)
        elif choice == '4':
            delete_contact(phonebook)
        elif choice == '5':
            save_file_phonebook(phonebook)
            print("Файл успешно сохранен.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор действия. Пожалуйста, выберите номер от 1 до 5.")


if __name__ == '__main__':
    main()