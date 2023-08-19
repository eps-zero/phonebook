from faker import Faker
import csv

fake = Faker()


def fake_phone_number(fake: Faker) -> str:
    return f'+7 {fake.msisdn()[3:]}'


def generate_csv_data(num_entries):
    entries = []
    for _ in range(num_entries):
        entry = {
            "last_name": fake.last_name(),
            "first_name": fake.first_name(),
            "middle_name": fake.first_name(),
            "organization": fake.company(),
            "work_phone": fake_phone_number(fake),
            "personal_phone": fake_phone_number(fake)
        }
        entries.append(entry)

    with open("data.csv", "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["last_name", "first_name", "middle_name",
                      "organization", "work_phone", "personal_phone"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)
