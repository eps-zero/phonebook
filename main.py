import csv
from csv_generator import generate_csv_data
from functions import display_entries, add_entry, edit_entry, search_entries


def main():
    entries_per_page = 5  # Number of entries displayed per page
    with open("data.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        entries = list(reader)

        page_num = 1  # Current page number
        display_entries(entries, page_num, entries_per_page)
        while True:
            print("Input")
            print(" ~ 'n' --- next page")
            print(" ~ 'p' --- previous page")
            print(" ~ 'a' --- add contact")
            print(" ~ 'e' --- edit contact")
            print(" ~ 's' --- search contact")
            print(" ~ 'q' --- quite")

            choice = input()

            if choice == 'n':
                page_num += 1
                display_entries(entries, page_num, entries_per_page)
            elif choice == 'p':
                page_num = max(1, page_num - 1)
                display_entries(entries, page_num, entries_per_page)
            elif choice == 'a':
                add_entry(entries)  # Add a new contact
                display_entries(entries, page_num, entries_per_page)
            elif choice == 'e':
                personal_phone_to_edit = input(
                    "Input personal phone for edit: ")
                # Edit an existing contact
                edit_entry(entries, personal_phone_to_edit)
            elif choice == 's':
                search_term = input("Input search term: ")
                matching_entries = search_entries(entries, search_term)
                display_entries(matching_entries, page_num, entries_per_page)
                search_page_num = 1
                while True:
                    print("Input")
                    print(" ~ 'n' --- next page")
                    print(" ~ 'p' --- previous page")
                    print(" ~ 'c' --- close")

                    choice = input()

                    if choice == 'n':
                        search_page_num += 1
                        display_entries(matching_entries,
                                        search_page_num, entries_per_page)
                    elif choice == 'p':
                        search_page_num = max(1, page_num - 1)
                        display_entries(matching_entries,
                                        search_page_num, entries_per_page)
                    elif choice == 'c':
                        break
            elif choice == 'q':
                break
            else:
                print("Unknown command!")


if __name__ == "__main__":
    num_entries = 20
    # Generate fake CSV data for testing
    fake_entries = generate_csv_data(num_entries)
    main()
