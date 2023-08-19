import csv


def display_entries(entries, page_num, entries_per_page):
    """
    Display contact entries in a paginated manner.

    :param entries: List of contact entries
    :param page_num: Current page number
    :param entries_per_page: Number of entries displayed per page
    """

    start_idx = (page_num - 1) * entries_per_page
    end_idx = start_idx + entries_per_page
    page_entries = entries[start_idx:end_idx]

    for entry in page_entries:
        print("Last name:", entry["last_name"])
        print("First name:", entry["first_name"])
        print("Middle name:", entry["middle_name"])
        print("Organization:", entry["organization"])
        print("Work phone:", entry["work_phone"])
        print("Personal phone:", entry["personal_phone"])
        print("=" * 30)


def add_entry(entries):
    """
    Add a new contact entry to the list.

    :param entries: List of contact entries
    """
    new_entry = {}
    new_entry["last_name"] = input("Введите фамилию: ")
    new_entry["first_name"] = input("Введите имя: ")
    new_entry["middle_name"] = input("Введите отчество: ")
    new_entry["organization"] = input("Введите название организации: ")
    new_entry["work_phone"] = input("Введите рабочий телефон: ")
    new_entry["personal_phone"] = input("Введите личный телефон: ")

    entries.append(new_entry)
    with open("data.csv", "a", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entries[0].keys())
        writer.writerow(new_entry)


def edit_entry(entries, personal_phone):
    """
    Edit an existing contact entry.

    :param entries: List of contact entries
    :param personal_phone: Personal phone of the contact to be edited
    """
    for entry in entries:
        if entry["personal_phone"] == personal_phone:
            new_last_name = entry["last_name"]
            new_first_name = entry["first_name"]
            new_middle_name = entry["middle_name"]
            new_organization = entry["organization"]
            new_work_phone = entry["work_phone"]
            new_personal_phone = entry["personal_phone"]

            while True:
                print("Input")
                print(" ~ 'l' --- edit last name")
                print(" ~ 'f' --- edit first name")
                print(" ~ 'm' --- edit middle name")
                print(" ~ 'o' --- edit organization")
                print(" ~ 'w' --- edit work phone")
                print(" ~ 'p' --- edit personal phone")
                print(" ~ 's' --- save changes")
                print(" ~ 'с' --- cancel changes")

                choice = input()

                if choice == 'l':
                    new_last_name = input("New last name: ")
                elif choice == 'f':
                    new_first_name = input("New first name: ")
                elif choice == 'm':
                    new_middle_name = input("New middle name: ")
                elif choice == 'o':
                    new_organization = input("New organization: ")
                elif choice == 'w':
                    new_work_phone = input("New work phone: ")
                elif choice == 'p':
                    new_personal_phone = input("New personal phone: ")
                elif choice == 's':
                    entry["last_name"] = new_last_name
                    entry["first_name"] = new_first_name
                    entry["middle_name"] = new_middle_name
                    entry["organization"] = new_organization
                    entry["work_phone"] = new_work_phone
                    entry["personal_phone"] = new_personal_phone
                    break
                elif choice == 'c':
                    return
                else:
                    print("Unknown command!")

    # Saving changes to the file
    with open("data.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entries[0].keys())
        writer.writeheader()
        writer.writerows(entries)


def search_entries(entries, search_term):
    """
    Search for contact entries that match the given search term.

    :param entries: List of contact entries
    :param search_term: Search term
    :return: List of matching contact entries
    """
    matching_entries = []

    for entry in entries:
        if (search_term.lower() in entry["last_name"].lower() or
            search_term.lower() in entry["first_name"].lower() or
            search_term.lower() in entry["middle_name"].lower() or
            search_term.lower() in entry["organization"].lower() or
            search_term in entry["work_phone"] or
                search_term in entry["personal_phone"]):
            matching_entries.append(entry)

    return matching_entries
