import csv
import random
from datetime import date, timedelta
import string
import os

def generate_ssn(existing_ssns):
  # Generate a unique random Social Security Number (SSN)
  while True:
    ssn = "{:03}-{:02}-{:04}".format(random.randint(1, 999),
                                     random.randint(1, 99),
                                     random.randint(1, 9999))
    if ssn not in existing_ssns:
      return ssn


def generate_date_of_birth():
  # Generate a random date of birth between 1900-01-01 and today
  start_date = date(1900, 1, 1)
  end_date = date.today()
  random_date = start_date + timedelta(
    days=random.randint(0, (end_date - start_date).days))
  return random_date.strftime("%Y-%m-%d")


def generate_date_of_death(date_of_birth):
  # Generate a random date of death after the date of birth
  start_date = date.fromisoformat(date_of_birth)
  end_date = date.today()
  random_date = start_date + timedelta(
    days=random.randint(1, (end_date - start_date).days))
  return random_date.strftime("%Y-%m-%d")


def generate_verification():
  # Generate a random verification status
  verification_status = random.choice(["Verified", "Not Verified"])
  return verification_status


def generate_death_master_file(num_people):
  # Generate the Death Master File with the specified number of people
  if num_people < 1 or num_people > 100:
    print("Invalid number of people. Please enter a value between 1 and 100.")
    return False

  fieldnames = [
    "first_name", "last_name", "middle_initial", "date_of_birth",
    "date_of_death", "ssn", "verification"
  ]
  rows = []
  existing_ssns = set()

  first_names = []
  last_names = []
  with open('names.txt', 'r') as f:
    for line in f.readlines():
      full_name = line.split()
      first_names.append(full_name[0])
      last_names.append(full_name[1])

  for _ in range(num_people):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    middle_initial = random.choice(string.ascii_uppercase)
    date_of_birth = generate_date_of_birth()
    date_of_death = generate_date_of_death(date_of_birth)
    ssn = generate_ssn(existing_ssns)
    existing_ssns.add(ssn)
    verification = generate_verification()

    rows.append([
      first_name, last_name, middle_initial, date_of_birth, date_of_death, ssn,
      verification
    ])

  today = date.today().strftime("%m%d%Y")
  filename = f"randomDMF{today}.csv"
  count = 97  # ASCII code for 'a'

  while os.path.exists(filename):
    filename = f"randomDMF{today}_{chr(count)}.csv"
    count += 1

  with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(rows)

  print(f"Death Master File generated successfully. Saved as {filename}.")
  return True


# User menu
def user_menu():
  while True:
    print("\n-------- User Menu --------")
    print("1. Generate Death Master File")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      while True:
        num_people = int(
          input(
            "Enter the number of random generations to imitate the LADMF from the NTIS: "
          ))
        if generate_death_master_file(num_people):
          break
        print()
    elif choice == "2":
      break
    else:
      print("Invalid choice. Please try again.")


user_menu()

print("Thank you for using the program!")
