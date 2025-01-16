import csv
from faker import Faker
import random
from datetime import datetime, timedelta
from random_pesel import RandomPESEL
import json


fake = Faker()

# Data
number_of_policeman = 1000
number_of_criminals = 1000
number_of_people = number_of_policeman + number_of_criminals

number_of_newcriminals = 1000
number_of_newpoliceman = 1000
number_of_newpeople = number_of_newcriminals + number_of_newpoliceman

amount_of_ticketsT1 = 500000
amount_of_ticketsT2 = 400000

amount_of_ratingsT1 = 300000
amount_of_ratingsT2 = 200000


job_titles = [
    "Traffic Officer",
    "Traffic Patrol Officer",
    "Traffic Corporal/Sergeant",
    "Traffic Lieutenant",
]

ticket_descriptions = [
    "Speeding",
    "Running Red Lights or Stop Signs",
    "Illegal Turns",
    "Failure to Yield",
    "Distracted Driving",
    "Driving without Proper Documentation",
    "Unsafe Lane Changes",
    "Following Too Closely",
    "Driving Under the Influence (DUI/DWI)",
    "Equipment Violations"
]

violation_articles = [
    "Art. 97",
    "Art. 89",
    "Art. 87",
    "Art. 94",
    "Art. 94a",
    "Art. 96",
    "Art. 90",
    "Art. 93",
    "Art. 178",
    "Art. 98"
]

# Load rating comments from JSON
with open('rating_comments.json', 'r') as f:
    rating_comments = json.load(f)

# Load districts data from JSON
with open('gdansk_districts.json', 'r') as f:
    gdansk_districts = json.load(f)


def random_datetime(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )


def generate_people_data(num_of_people):
    data = []
    pesels = []
    for _ in range(num_of_people):
        pesel = RandomPESEL().generate(min_age=18)
        if pesel not in pesels:
            pesels.append(pesel)
        first_name = fake.first_name()
        surname = fake.last_name()
        data.append((pesel, first_name,
                     surname, 0))
    return data


def generate_officer_data(num_records, people_data):
    """
    Function to generate data for Officer table
    """
    data = []
    i = 100000
    for _ in range(num_records):
        badge_number = i
        # if pesel is present in pesels generate a new one
        pesel = people_data[_][0]
        first_name = people_data[_][1]
        surname = people_data[_][2]
        job_title = random.choice(job_titles)
        job_rank = random.randint(1, 3)
        i += 1
        data.append((badge_number, pesel, first_name,
                     surname, job_title, job_rank, 0))
    return data


def generate_criminal_data(num_records, people_data):
    """
    Function to generate data for Criminal table
    """
    data = []
    i = 100000
    for _ in range(num_records):
        criminal_id = i
        # if pesel is present in pesels generate a new one
        pesel = people_data[_ + number_of_policeman][0]
        first_name = people_data[_ + number_of_policeman][1]
        surname = people_data[_ + number_of_policeman][2]
        penalty_points = random.randint(0, 24)
        i += 1
        data.append((criminal_id, pesel, first_name,
                     surname, penalty_points, 0))
    return data


def add_penalty_points(penalty_points, criminal_data, criminal_id):
    # Convert criminal_data tuple to a list
    criminal_dataH = list(criminal_data)

    # Update penalty points for the specified criminal ID
    criminal_dataH[criminal_id - 100000][4] += penalty_points

    return criminal_dataH


def generate_ticket_data(num_records, officer_badge_numbers, criminal_ids, pairs, is_old, criminal_data):
    data = []
    i = 1
    for _ in range(num_records):
        if is_old == 1:
            ticket_id = i + amount_of_ticketsT1
        else:
            ticket_id = i
        officer_badge_number = random.choice(officer_badge_numbers)
        criminal_id = random.choice(criminal_ids)
        ticket_description = random.choice(ticket_descriptions)
        violation_article = random.choice(violation_articles)
        penalty_points = random.randint(0, 24)

        # criminal_data[criminal_id - 100000][4] += penalty_points

        # criminal_data[criminal_id - 100000] = (criminal_data[criminal_id - 100000][0] + penalty_points, criminal_data[criminal_id - 100000][1])

        if is_old == 1:
            datetime_of_issue = random_datetime(
                datetime(2022, 1, 1), datetime(2024, 1, 1))
        else:
            datetime_of_issue = random_datetime(
                datetime(2020, 1, 1), datetime(2022, 1, 1))
        p = random.randint(0, 11)
        if p == 10:
            amount = (random.randint(70, 75)) * 100
        elif p == 9:
            amount = (random.randint(30, 70)) * 100
        elif p == 8:
            amount = (random.randint(10, 30)) * 100
        elif p == 7 or p == 6:
            amount = (random.randint(5, 10)) * 100
        else:
            amount = (random.randint(1, 5)) * 100

        full_district = random.choice(gdansk_districts['districts'])

        district = full_district['name']

        street = random.choice(full_district['streets'])

        i += 1
        data.append((ticket_id, officer_badge_number, criminal_id, ticket_description,
                     violation_article, penalty_points, datetime_of_issue, amount, street, district, 0))
        pairs.append((officer_badge_number, criminal_id, ticket_id))

    return data, pairs


def generate_rating_data(num_records, pairs, is_old):
    data = []
    i = 1
    for _ in range(num_records):
        if is_old == 1:
            rating_id = i + amount_of_ratingsT1
        else:
            rating_id = i
        points = random.randint(1, 5)
        if (points >= 3):
            comments = random.choice(rating_comments['positive'])
        else:
            comments = random.choice(rating_comments['negative'])
        # pairsChoice = random.choice(pairs)
        pairsChoice = pairs[rating_id - 1]
        i += 1
        officer_badge_numbers = pairsChoice[0]
        criminal_id = pairsChoice[1]
        ticket_id = pairsChoice[2]

        data.append((rating_id, points, comments,
                    officer_badge_numbers, criminal_id, ticket_id, 0))
    return data


def generate_new_people_data(num_of_people, people_data):
    pesels = []
    for pesel, first_name, surname, _ in people_data:
        pesels.append(pesel)
    for _ in range(num_of_people):
        pesel = RandomPESEL().generate(min_age=18)
        if pesel not in pesels:
            pesels.append(pesel)
        first_name = fake.first_name()
        surname = fake.last_name()
        people_data.append((pesel, first_name,
                            surname, 0))
    return people_data


def generate_new_criminal_data(num_records, people_data):
    data = []
    i = 100000
    for _ in range(num_records):
        criminal_id = i + number_of_criminals
        # if pesel is present in pesels generate a new one
        pesel = people_data[_ + number_of_policeman +
                            number_of_criminals + number_of_newpoliceman][0]
        first_name = people_data[_ + number_of_policeman +
                                 number_of_criminals + number_of_newpoliceman][1]
        surname = people_data[_ + number_of_policeman +
                              number_of_criminals + number_of_newpoliceman][2]

        penalty_points = random.randint(0, 24)
        i += 1
        data.append((criminal_id, pesel, first_name,
                     surname, penalty_points, 0))
    return data


def generate_new_officer_data(num_records, people_data):
    data = []
    i = 100000
    for _ in range(num_records):
        badge_number = i + number_of_policeman
        # if pesel is present in pesels generate a new one
        pesel = people_data[_ + number_of_policeman + number_of_criminals][0]
        first_name = people_data[_ +
                                 number_of_policeman + number_of_criminals][1]
        surname = people_data[_ + number_of_policeman + number_of_criminals][2]
        job_title = random.choice(job_titles)
        job_rank = random.randint(1, 3)
        i += 1
        data.append((badge_number, pesel, first_name,
                     surname, job_title, job_rank, 0))
    return data


def write_to_bulk_file(data, filename):
    with open(filename, 'w') as f:
        for record in data:
            line = '|'.join(map(str, record)) + '\n'
            f.write(line)


def give_average(badge_number, rating_data, num_of_records_rating):
    i = 0
    sum = 0
    for _ in range(num_of_records_rating):
        if rating_data[_][3] == badge_number:
            i = i + 1
            sum = sum + rating_data[_][1]

    if i == 0:
        avg = 0
    else:
        avg = sum / i
    return avg


def generate_excel_policeman(officer_data, rating_data, num_of_records_police, num_of_records_rating):
    data = []
    for _ in range(num_of_records_police):
        badge_number = officer_data[_][0]
        pesel = officer_data[_][1]
        first_name = officer_data[_][2]
        surname = officer_data[_][3]
        job_title = officer_data[_][4]
        job_rank = officer_data[_][5]

        full_district = random.choice(gdansk_districts['districts'])

        district = full_district['name']

        street = random.choice(full_district['streets'])

        address = street + ' ' + str(random.randint(1, 50)) + ', '

        avgRating = give_average(
            badge_number, rating_data, num_of_records_rating)

        points = random.randint(0, 1)

        if (points >= 1):
            ListOfComments = random.choice(rating_comments['positive'])
        else:
            ListOfComments = random.choice(rating_comments['negative'])

        StartOfService = random.randint(2005, 2019)

        data.append((badge_number, pesel, first_name,
                     surname, job_title, job_rank, 0, address, "Gdansk", avgRating, ListOfComments, StartOfService, points))
    return data


def generate_excel_criminals(officer_data, num_of_records_police):
    data = []
    for _ in range(num_of_records_police):
        badge_number = officer_data[_][0]
        pesel = officer_data[_][1]
        first_name = officer_data[_][2]
        surname = officer_data[_][3]
        penaltyPoints = officer_data[_][4]
        IsOnProbation = random.randint(0, 1)

        data.append((badge_number, pesel, first_name,
                     surname, penaltyPoints, 0, IsOnProbation))
    return data


pairs = []


# Generate data for T1
people_data = generate_people_data(number_of_people)
officer_data = generate_officer_data(number_of_policeman, people_data)
criminal_data = generate_criminal_data(number_of_criminals, people_data)
officer_badge_numbers = [record[0] for record in officer_data]
criminal_ids = [record[0] for record in criminal_data]
ticket_data, pairs = generate_ticket_data(
    amount_of_ticketsT1, officer_badge_numbers, criminal_ids, pairs, 0, criminal_data)
rating_data = generate_rating_data(amount_of_ratingsT1, pairs, 0)

# Write T1 data to bulk files
write_to_bulk_file(officer_data, 'data/officer_data.csv')
write_to_bulk_file(criminal_data, 'data/criminal_data.csv')
write_to_bulk_file(ticket_data, 'data/ticket_data.csv')
write_to_bulk_file(rating_data, 'data/rating_data.csv')

# Generate data for T2
people_data = generate_new_people_data(number_of_newpeople, people_data)
officer_data_new = generate_new_officer_data(
    number_of_newpoliceman, people_data)
criminal_data_new = generate_new_criminal_data(
    number_of_newcriminals, people_data)
officer_badge_numbers = [record[0] for record in officer_data]
criminal_ids = [record[0] for record in criminal_data]
ticket_dataT2, pairs = generate_ticket_data(
    amount_of_ticketsT2, officer_badge_numbers, criminal_ids, pairs, 1,  criminal_data)
rating_dataT2 = generate_rating_data(amount_of_ratingsT2, pairs, 1)

# Write T2 data to bulk files
write_to_bulk_file(officer_data_new, 'data/officer_dataT2.csv')
write_to_bulk_file(criminal_data_new, 'data/criminal_dataT2.csv')
write_to_bulk_file(ticket_dataT2, 'data/ticket_dataT2.csv')
write_to_bulk_file(rating_dataT2, 'data/rating_dataT2.csv')

# Generate excel data
excel_policeman_data = generate_excel_policeman(
    officer_data, rating_data, number_of_policeman, amount_of_ratingsT1)
write_to_bulk_file(excel_policeman_data, 'data/officer_data_Excel.csv')

excel_criminals_data = generate_excel_criminals(
    criminal_data, number_of_criminals)
write_to_bulk_file(excel_criminals_data, 'data/criminals_data_Excel.csv')


officer_data_all = officer_data + officer_data_new
amount_of_ratings_all = amount_of_ratingsT1 + amount_of_ratingsT2
number_of_policeman_all = number_of_policeman + number_of_newpoliceman
rating_data_all = rating_dataT2 + rating_data
Criminals_dataall = criminal_data + criminal_data_new


excel_policeman_dataT2 = generate_excel_policeman(
    officer_data_all, rating_data_all, number_of_policeman_all, amount_of_ratings_all)
write_to_bulk_file(excel_policeman_dataT2, 'data/officer_data_ExcelT2.csv')


excel_criminals_data = generate_excel_criminals(
    criminal_data, number_of_criminals)
write_to_bulk_file(excel_criminals_data, 'data/criminals_data_ExcelT2.csv')
