
#faker: pip install faker
#openpyxl: pip install openpyxl
#python-docx: pip install python-docx
import random
import datetime
import string
from faker import Faker
from openpyxl import Workbook

# Create a Faker instance for each country
faker_us = Faker('en_US')
faker_br = Faker('pt_BR')
faker_mx = Faker('es_MX')
faker_co = Faker('es_CO')
faker_pt = Faker('pt_PT')
faker_es = Faker('es_ES')
faker_se = Faker('sv_SE')
faker_pl = Faker('pl_PL')
faker_au = Faker('en_AU')
faker_ca = Faker('en_CA')
faker_ar = Faker('es_AR')
faker_in = Faker('en_IN')
faker_ir = Faker('fa_IR')
faker_ch = Faker('de_CH')
faker_fr = Faker('fr_FR')
faker_it = Faker('it_IT')

# Create an Excel workbook and worksheet
wb = Workbook()
ws = wb.active

# Write the headers
ws.append(['Type', 'Name', 'Email', 'Password', 'Birthdate', 'Recovery'])

# Function to generate a random birthdate for someone 18+ years old
def generate_birthdate():
    today = datetime.date.today()
    age = random.randint(18, 70)
    birthdate = today - datetime.timedelta(days=age*365)
    return birthdate.strftime('%Y%m%d')

# Function to generate a random password
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=8))
    return password

# Iterate 10 times and generate a new row for each iteration
for i in range(10):
    # Choose a random name and surname from a random country
    faker_list = [faker_us, faker_br, faker_mx, faker_co, faker_pt, faker_es, faker_se, faker_pl, faker_au, faker_ca, faker_ar, faker_in, faker_ir, faker_ch, faker_fr, faker_it]
    faker = random.choice(faker_list)
    random_name = faker.name()

    # Generate a random birthdate and password
    birthdate = generate_birthdate()
    password = generate_password()

    # Write the row to the Excel worksheet
    ws.append(['', random_name, '', password, birthdate, ''])

# Save the Excel workbook
wb.save('output.xlsx')

# Wait for the user to press a key
input("Press Enter to exit...")