import csv
from faker import Faker
import random
from datetime import datetime, timedelta
from random_pesel import RandomPESEL


fake = Faker()

# Data
number_of_policeman = 1000
number_of_criminals = 1000
number_of_people = number_of_policeman + number_of_criminals


# carefull
number_of_newcriminals = 1000
number_of_newpoliceman = 1000
number_of_newpeople = number_of_newcriminals + number_of_newpoliceman

amount_of_ticketsT1 = 500000
amount_of_ticketsT2 = 400000

amount_of_RatingsT1 = 300000
amount_of_RatingsT2 = 200000


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


positive_descriptions = [
    "They were professional and respectful throughout the process, explaining everything clearly.",
    "I appreciated their prompt response and how they handled the situation calmly.",
    "The officers showed empathy and understanding, which made a difficult experience easier to bear.",
    "They ensured my rights were respected and treated me fairly during the entire process.",
    "Despite the circumstances, they maintained a level of professionalism and courtesy.",
    "I felt intimidated and nervous at first, but they were surprisingly patient and reassuring.",
    "Their thoroughness in the investigation gave me confidence in their commitment to justice.",
    "I was pleasantly surprised by their transparency and willingness to answer my questions.",
    "Their presence made me feel safer, even though I was being detained.",
    "I was impressed by their attention to detail and commitment to resolving the situation.",
    "Their communication was clear and concise, which helped alleviate some of my anxiety.",
    "Despite the tension of the situation, they remained calm and composed.",
    "I appreciated that they treated me with dignity and respect throughout the process.",
    "Their professionalism helped me trust that the outcome would be fair and just.",
    "Their thorough investigation ensured that all aspects of the situation were properly addressed.",
    "I felt supported and advocated for during the entire process.",
    "Their demeanor helped de-escalate the situation and prevent it from escalating further.",
    "They showed genuine concern for my well-being and safety.",
    "Their patience and willingness to listen made me feel like my voice mattered.",
    "I was grateful for their assistance and guidance throughout the process.",
    "Their professionalism and attention to detail gave me confidence in their ability to handle the situation.",
    "They handled the situation with sensitivity and respect for my privacy.",
    "Their actions were firm but fair, and they ensured that I understood the reasons behind their decisions.",
    "Despite the circumstances, they treated me with dignity and respect.",
    "Their professionalism helped me feel reassured during a stressful experience.",
    "Their efforts to keep me informed and involved in the process were greatly appreciated.",
    "Their commitment to following proper procedures helped me trust in the fairness of the outcome.",
    "I felt like they genuinely cared about my well-being and safety.",
    "Their willingness to listen to my perspective helped resolve the situation more amicably.",
    "Despite the seriousness of the situation, they remained approachable and understanding."
]

negative_descriptions = [
    "They were rude and disrespectful, making the situation more stressful than it needed to be.",
    "Their response was slow and inadequate, leaving me feeling vulnerable and unsafe.",
    "The officers showed no empathy or understanding, treating me like a criminal from the start.",
    "They violated my rights and treated me unfairly throughout the entire process.",
    "Their demeanor was aggressive and confrontational, escalating the situation unnecessarily.",
    "I felt harassed and intimidated by their behavior, which only added to my distress.",
    "Their investigation was sloppy and incomplete, leaving important details overlooked.",
    "They were evasive and uncooperative, refusing to provide me with any information.",
    "Their presence made me feel more threatened and anxious, rather than protected.",
    "I was appalled by their lack of professionalism and disregard for proper procedure.",
    "Their communication was vague and confusing, leaving me in the dark about what was happening.",
    "They were chaotic and disorganized, unable to handle the situation effectively.",
    "I felt degraded and humiliated by their treatment, as if I had no rights at all.",
    "Their conduct was unbecoming of law enforcement officers, undermining trust in the system.",
    "Their investigation was biased and one-sided, ignoring crucial evidence and testimonies.",
    "I felt abandoned and alone throughout the process, with no support or guidance.",
    "Their aggression only served to escalate the situation further, putting everyone at risk.",
    "They showed no concern for my well-being or safety, only focused on asserting their authority.",
    "Their dismissive attitude made me feel like my voice didn't matter at all.",
    "I received no help or assistance from them, despite being in a vulnerable position.",
    "Their incompetence was glaringly obvious, making me question their ability to handle any situation.",
    "They showed no respect for my privacy or dignity, treating me like a criminal.",
    "Their actions were arbitrary and unjust, leaving me feeling powerless and disillusioned.",
    "I felt degraded and dehumanized by their treatment, as if I were less than human.",
    "Their lack of professionalism only added to the chaos of the situation, making matters worse.",
    "Their indifference to my plight was disheartening, leaving me feeling abandoned and alone.",
    "Their disregard for proper procedure and protocol eroded any trust I had in them.",
    "I felt like just another number to them, rather than a human being in need of help.",
    "Their refusal to listen to my side of the story only served to perpetuate injustice.",
    "Despite my attempts to cooperate, they treated me with suspicion and hostility."
]

districts = [
    "CHElM",
    "OSOWA",
    "KOKOSZKI",
    "NOWY DWoR",
    "WOJCIECH-LIPCE",
    "PIECKI-MIGOWO",
    "UJEsCISKO-lOSTOWICE",
    "PRZYMORZE MAlE",
    "ZASPA-ROZSTAJE",
    "OLIWA",
    "OLSZYNKA",
    "SIEDLCE"
]

CHELM = [
    "luzycka",
    "lyzwiarska",
    "Antoniego Madalinskiego 2 do konca",
    "Ludwiki Marii Ludwiki",
    "Jana Michonia",
    "Bernarda Milskiego",
    "Milocinska",
    "Feliksa Muzyka",
    "Nad Potokiem",
    "Narciarska",
    "Nieborowska",
    "Niepolomicka",
    "Odrzanska",
    "Grudnia’70",
    "gen. Leopolda Okulickiego",
    "Olimpijska",
    "Pastelowa",
    "Aliny Pienkowskiej",
    "Pilkarska",
    "Platynowa",
    "Zbigniewa Podleckiego",
    "Pohulanka",
    "Przemian",
    "Ptasia 30, 30A",
    "Reformacka",
    "Rogalinska",
    "bpa. Hieronima Rozrazewskiego",
    "Zygmunta Rumla",
    "Ludwika Rydygiera",
    "Gabriela Rzączynskiego",
    "Saneczkarska",
    "Ireny Sendlerowej",
    "Aleja gen.Wladyslawa Sikorskiego",
    "gen. Kazimierza Sosnkowskiego",
    "Srebrna",
    "Starogardzka 22 do konca",
    "Stoczniowcow",
    "Straszynska",
    "Karpackich Strzelcow Karpackich",
    "Antoniego Suchanka",
    "Szermiercza",
    "Szmaragdowa",
    "Lubomira Szopinskiego",
    "prof. Stanislawa Szpora",
    "Wladyslawa swiechockiego",
    "swietokrzyska",
    "Tenisowa",
    "Damazego Tilgnera",
    "Topazowa",
    "Uranowa",
    "Wawelska",
    "Jozefa Wąsika",
    "Kazimierza Wielkiego",
    "Wielkopolska 48 do konca",
    "prof. Jozefa Wieckowskiego",
    "Wigierska",
    "Wilanowska",
    "Wincentego Witosa",
    "Stanislawa Worcella",
    "bpa Andrzeja Wronki",
    "Zamiejska",
    "gen. Elzbiety Zawackiej",
    "Zielonogorska",
    "Zlota",
    "Jerzego Zwierkowskiego"
]

OSOWA = [
    "kpt. Konstantego Maciejewicza",
    "Marsa",
    "Merkurego",
    "Meteorytowa",
    "Miedzygwiezdna",
    "Minerwy",
    "Mirandy",
    "Mysliborska",
    "Nawigatorow",
    "Neptuna",
    "Mieczyslawa Niedzialkowskiego",
    "Nike",
    "Nowa",
    "Nowy swiat",
    "Odyseusza",
    "Okretowa",
    "Orfeusza",
    "Oriona",
    "Osowski Zakątek",
    "Otago",
    "Owczarnia",
    "Ozyrysa",
    "Parkingowa",
    "Parkowa",
    "Parterowa",
    "Parysa",
    "Pegaza",
    "Penelopy",
    "Perseusza",
    "Plac sw. Jana Apostola",
    "Planetarna",
    "Plejady",
    "Plutona",
    "Posejdona",
    "Prometeusza",
    "Rabatki",
    "Regatowa",
    "Relaksowa",
    "Saturna",
    "Seleny",
    "prof. Michala Siedleckiego",
    "Smugowa",
    "Stanislawa Soldka",
    "Sopocka",
    "Spacerowa 46 do konca",
    "Sportowa",
    "Strzelca",
    "Syriusza",
    "Wladyslawa Szafera",
    "Szalupowa",
    "Leonida Teligi",
    "Temidy",
    "Tezeusza",
    "Trapowa",
    "Urana",
    "Victorii",
    "Wegi",
    "Tadeusza Wendy",
    "Wenus",
    "Westy",
    "Willowa",
    "Wodnika",
    "Wolarza",
    "Woźnicy",
    "Mariusza Zaruskiego",
    "Zatokowa",
    "Zeusa",
    "Zlotowska"
]

KOKOSZKI = [
    "Maciejkowa",
    "Macierzankowa",
    "Malinowa",
    "Franciszka Mamuszki",
    "Marcowa",
    "Maszynowa",
    "Metalowcow",
    "Mezowska",
    "Miechucinska",
    "Mirachowska",
    "Montazystow",
    "Nagietkowa",
    "Niegocinska",
    "Nowatorow",
    "Okolna",
    "Osiedlowa",
    "Otominska",
    "Porzeczkowa",
    "Poziomkowa",
    "Przyrodnikow",
    "Rakietowa",
    "Rokitnikowa",
    "Rozwojowa",
    "Stok Rozany Stok",
    "Rumiankowa",
    "Sianowska",
    "Sierakowicka",
    "Sierpniowa",
    "Smegorzynska",
    "Snycerzy",
    "Sominska",
    "Stoklosy",
    "Storczykowa",
    "Sudomska",
    "Sulminska",
    "Swarzewska",
    "Szafranowa",
    "Brata Alberta sw. Brata Alberta",
    "Transportowcow",
    "Tuchomska",
    "Tymiankowa",
    "Wdzydzka",
    "Wesierska",
    "Widlinska",
    "Wiecka",
    "Wielewska",
    "Wiosenna",
    "Wrzesniowa",
    "Zbąszynska",
    "Zbiezna",
    "zukowska"
]

NDWoR = [
    "Macierzy Szkolnej w Gdansku",
    "Jozefa Mehoffera",
    "Piotra Michalowskiego",
    "Piotra Norblina",
    "Romana i Apolonii Ogryczakow",
    "Aleksandra Orlowskiego",
    "dr. Wladyslawa Paneckiego",
    "Polanki 59-118",
    "Aleksandra Potyraly",
    "Henryka Rodakowskiego",
    "Aleksandra Rylkego",
    "Henryka Siemiradzkiego",
    "Kazimierza Sosnickiego",
    "VII Dwor",
    "Wita Stwosza 96-104"
]

WOJCIECHLIPCE = [
    "Antoniego Madalinskiego 1, 1A",
    "Malomiejska",
    "Mostowa",
    "Nad Starą Radunią",
    "Nakielska",
    "Niegowo",
    "Niegowska",
    "Nowiny",
    "Park Orunski",
    "Perlowa",
    "Piaskowa",
    "Plac Orunski",
    "Po Schodkach",
    "Podmiejska"
]

PIECKIMIGOWO = [
    "Antoniego Madalinskiego 1, 1A",
    "Malomiejska",
    "Mostowa",
    "Starą Radunią Nad Starą Radunią",
    "Nakielska",
    "Niegowo",
    "Niegowska",
    "Nowiny",
    "Perlowa",
    "Piaskowa",
    "Plac Orunski",
    "Schodkach Po Schodkach",
    "Podmiejska",
    "Poleska",
    "Torze Przy Torze",
    "Przybrzezna",
    "Przyjemna",
    "Ptasia 1-29; 2-22A",
    "Radunicka",
    "Radunska",
    "Stefana Ramulta",
    "Tadeusza Rejtana",
    "Rowna",
    "Rubinowa",
    "Rzeczna",
    "Sandomierska",
    "Serbska",
    "Smetna",
    "Smolenska",
    "Smolna",
    "Starogardzka 1-20",
    "Stroma",
    "Szafirowa",
    "Szkocka",
    "Ryszarda Tomczaka",
    "Trakt sw. Wojciecha",
    "Turkusowa",
    "Ubocze",
    "Ukosna",
    "Urocza",
    "Wąwoz",
    "Wolynska",
    "Wschodnia",
    "Zamiejska 1-28",
    "Zawiejska",
    "Zawilcowa",
    "Związkowa",
    "zabia",
    "zulawska"
]

UJEsCISKOLOSTOWICE = [
    "Magellana",
    "Heleny Marusarzowny",
    "Morenowa",
    "Morenowe Wzgorze",
    "prof. Stefana Myczkowskiego",
    "Mysliwska 20 do konca",
    "Mysliwskie Wzgorze",
    "Zofii Nalkowskiej",
    "Alfreda Nobla",
    "Oranska",
    "Blaise’a Pascala",
    "Ludwika Pasteura",
    "Piecewska",
    "Piekarnicza",
    "Powstania Kosciuszkowskiego",
    "Listopadowego Powstania Listopadowego",
    "Styczniowego Powstania Styczniowego",
    "prof. Mariana Raciborskiego",
    "Franciszka Rakoczego",
    "Wyrobka Romana Wyrobka",
    "Szczodra",
    "Lipy Trzy Lipy",
    "Aleksandra Volty",
    "Warnenska",
    "Widok",
    "Wilenska 37-63",
    "Wolkowyska",
    "Franciszka Zablockiego",
    "Zacna",
    "Związku Jaszczurczego",
    "Jozefa zylewicza"
]

PRZYMORZEMAlE = [
    "ksiedza Jana Majdera",
    "Malborska",
    "Morawska",
    "II Msciwoja II",
    "Obotrycka",
    "Piastowska 19-107; 20-88",
    "Plac Najswietszej Maryi Panny",
    "Poznanska",
    "Pucka",
    "Aleja Rzeczypospolitej strona niezamieszkala",
    "Rzepichy",
    "Sambora",
    "Slowianska",
    "Slupska",
    "Jana Solikowskiego",
    "Subislawa 1-18",
    "Szczecinska",
    "sląska",
    "swietopelka",
    "Tolkmicka",
    "Wladyslawowska",
    "I Zgody I",
    "II Zgody II",
    "Ziemowita"
]

ZASPAROZSTAJE = [
    "Majewskich",
    "Janusza Meissnera",
    "Augustyna Necla",
    "Park im. Jana Pawla II",
    "Millenium Gdanska Park Millenium Gdanska Inne",
    "Plac Trzeciego Tysiąclecia",
    "Gdanskiej Polonii Gdanskiej",
    "Powstancow Wielkopolskich",
    "Henryka Wieczorkiewicza",
    "zwirki i Wigury"
]

OLIWA = [
    "Aleksandra Majkowskiego",
    "Bernarda Milewskiego",
    "Stefana Miraua",
    "Nadwodna",
    "Stanislawa Noakowskiego",
    "bpa. Edmunda Nowickiego",
    "Obroncow Westerplatte",
    "Opacka",
    "Wladyslawa Orkana",
    "Park Oliwski im. Adama Mickiewicza",
    "Piastowska",
    "Dworcowy Plac Dworcowy",
    "Plac Inwalidow Wojennych",
    "Poczty Gdanskiej",
    "Podhalanska",
    "Polanki 1-58",
    "Pomorska",
    "Opata Jacka Rybinskiego",
    "Sarnia",
    "Artura Schopenhauera",
    "Sloneczna",
    "Sobolowa",
    "Spacerowa",
    "Stary Rynek Oliwski",
    "swierkowa",
    "Tatrzanska",
    "Kazimierza Tetmajera",
    "Stanislawa Wąsowicza",
    "Stwosza Wita Stwosza 1-62A",
    "Stanislawa Witkiewicza",
    "Zacisze",
    "Zajecza",
    "Stefana zeromskiego",
    "zubrowa"
]

OLSZYNKA = [
    "Majowa",
    "Maki",
    "Miedza",
    "Miodowa",
    "Modra",
    "Na Szancach",
    "Niezapominajek",
    "Niwki",
    "Olszynska",
    "Osiedle",
    "Ostrozek",
    "Pasieczna",
    "Piwonii",
    "Pusta",
    "Sierpowa",
    "Slonecznikowa",
    "Stokrotki",
    "Szarotki",
    "sciezki",
    "Tulipanow",
    "Wąskotorowa",
    "Wilgi",
    "Wspolna",
    "Zagony",
    "Zawodzie",
    "Zielna",
    "Zuchow",
    "zarnowiecka",
    "zurawia"
]

SIEDLCE = [
    "Kornela Makuszynskiego",
    "Stanislawa Malachowskiego",
    "Jana Matejki",
    "Matki Polki",
    "Miedziana",
    "Migowska",
    "ks. Leona Miszewskiego",
    "Na Wzgorzu",
    "Gabriela Narutowicza",
    "Cypriana Kamila Norwida",
    "Obywatelska",
    "Karola Olszewskiego",
    "Rozy Ostrowskiej",
    "Akademicki Park Akademicki Inne",
    "Partyzantow",
    "Stanislawa Pawlowskiego",
    "Szczepana Pileckiego",
    "Grzegorza Piramowicza",
    "Plac Jerzego Kolodziejskiego",
    "Wladyslawa Pniewskiego",
    "Podlesna",
    "Wincentego Pola",
    "Politechniczna",
    "Aleksandra Puszkina",
    "Renesansowa",
    "Wladyslawa Reymonta",
    "Rodzinna",
    "Romanska",
    "Eugeniusza Romera",
    "Secesyjna",
    "Siedlicka",
    "Henryka Sienkiewicza",
    "Antoniego Slonimskiego",
    "Juliusza Slowackiego 1-81; 2-90",
    "Jana Sobieskiego",
    "Sobotki",
    "Sosnowa",
    "Srebrniki",
    "Stanislawa Staszica",
    "Suwalska",
    "Wladyslawa Syrokomli",
    "Topolowa",
    "Romualda Traugutta 16-102; 31-121",
    "Trawki",
    "Jana Uphagena",
    "Ludwika Warynskiego 1-8; 40 do konca",
    "Jozefa Wassowskiego",
    "Wilenska 1-35; 2-42",
    "Wlasna Strzecha",
    "Zygmunta Wroblewskiego",
    "Wspolczesna",
    "Zabytkowa",
    "ks. Jozefa Zator Przytockiego",
    "Franciszka Zubrzyckiego",
    "Aleja Zwyciestwa 16/17 do 32"
]

# Function to generate random datetime within a range


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


# Function to generate data for Officer table


def generate_officer_data(num_records, people_data):
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

# Function to generate data for Criminal table


def generate_criminal_data(num_records, people_data):
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


def AddPenaltyPoints(penalty_points, criminal_data, criminal_id):
    # Convert criminal_data tuple to a list
    criminal_dataH = list(criminal_data)

    # Update penalty points for the specified criminal ID
    criminal_dataH[criminal_id - 100000][4] += penalty_points

    return criminal_dataH
# Function to generate data for Ticket table


def generate_ticket_data(num_records, officer_badge_numbers, criminal_ids, pairs, oldORnot, criminal_data):
    data = []
    i = 1
    for _ in range(num_records):
        if oldORnot == 1:
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

        if oldORnot == 1:
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
        # change to gdansk streets and districts

        district = random.choice(districts)

        if (district == "CHElM"):
            street = random.choice(CHELM)

        if (district == "OSOWA"):
            street = random.choice(OSOWA)

        if (district == "KOKOSZKI"):
            street = random.choice(KOKOSZKI)

        if (district == "NOWY DWoR"):
            street = random.choice(NDWoR)

        if (district == "WOJCIECH-LIPCE"):
            street = random.choice(WOJCIECHLIPCE)

        if (district == "PIECKI-MIGOWO"):
            street = random.choice(PIECKIMIGOWO)

        if (district == "UJEsCISKO-lOSTOWICE"):
            street = random.choice(UJEsCISKOLOSTOWICE)

        if (district == "PRZYMORZE MAlE"):
            street = random.choice(PRZYMORZEMAlE)

        if (district == "ZASPA-ROZSTAJE"):
            street = random.choice(ZASPAROZSTAJE)

        if (district == "OLIWA"):
            street = random.choice(OLIWA)

        if (district == "OLSZYNKA"):
            street = random.choice(OLSZYNKA)

        if (district == "SIEDLCE"):
            street = random.choice(SIEDLCE)

        i += 1
        data.append((ticket_id, officer_badge_number, criminal_id, ticket_description,
                     violation_article, penalty_points, datetime_of_issue, amount, street, district, 0))
        pairs.append((officer_badge_number, criminal_id, ticket_id))

    return data, pairs


def generate_rating_data(num_records, pairs, IsItOld):
    data = []
    i = 1
    for _ in range(num_records):
        if IsItOld == 1:
            rating_id = i + amount_of_RatingsT1
        else:
            rating_id = i
        points = random.randint(1, 5)
        if (points >= 3):
            comments = random.choice(positive_descriptions)
        else:
            comments = random.choice(negative_descriptions)
        # pairsChoice = random.choice(pairs)
        pairsChoice = pairs[rating_id - 1]
        i += 1
        officer_badge_numbers = pairsChoice[0]
        criminal_id = pairsChoice[1]
        ticket_id = pairsChoice[2]

        data.append((rating_id, points, comments,
                    officer_badge_numbers, criminal_id, ticket_id, 0))
    return data


def generate_FEWMOREpeople_data(num_of_people, people_data):
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


def generate_FEWMOREcriminal_data(num_records, people_data):
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


def generate_FEWMOREofficer_data(num_records, people_data):
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
            line = '|'.join(map(str, record)) + '$'
            f.write(line)


def write_to_bulk_fileEX(data, filename):
    with open(filename, 'w') as f:
        for record in data:
            line = '|'.join(map(str, record)) + '\n'
            f.write(line)


def GiveAvrage(badge_number, rating_data, num_recordsRate):
    i = 0
    sum = 0
    for _ in range(num_recordsRate):
        if rating_data[_][3] == badge_number:
            i = i + 1
            sum = sum + rating_data[_][1]

    if i == 0:
        Avrage = 0
    else:
        Avrage = sum / i
    return Avrage


def excelpolicamn(officer_data, rating_data, num_recordsPolice, num_recordsRate):
    data = []
    for _ in range(num_recordsPolice):
        badge_number = officer_data[_][0]
        pesel = officer_data[_][1]
        first_name = officer_data[_][2]
        surname = officer_data[_][3]
        job_title = officer_data[_][4]
        job_rank = officer_data[_][5]

        district = random.choice(districts)

        if (district == "CHElM"):
            street = random.choice(CHELM)

        if (district == "OSOWA"):
            street = random.choice(OSOWA)

        if (district == "KOKOSZKI"):
            street = random.choice(KOKOSZKI)

        if (district == "NOWY DWoR"):
            street = random.choice(NDWoR)

        if (district == "WOJCIECH-LIPCE"):
            street = random.choice(WOJCIECHLIPCE)

        if (district == "PIECKI-MIGOWO"):
            street = random.choice(PIECKIMIGOWO)

        if (district == "UJEsCISKO-lOSTOWICE"):
            street = random.choice(UJEsCISKOLOSTOWICE)

        if (district == "PRZYMORZE MAlE"):
            street = random.choice(PRZYMORZEMAlE)

        if (district == "ZASPA-ROZSTAJE"):
            street = random.choice(ZASPAROZSTAJE)

        if (district == "OLIWA"):
            street = random.choice(OLIWA)

        if (district == "OLSZYNKA"):
            street = random.choice(OLSZYNKA)

        if (district == "SIEDLCE"):
            street = random.choice(SIEDLCE)

        address = street + ' ' + str(random.randint(1, 50)) + ', '

        AvrageRating = GiveAvrage(badge_number, rating_data, num_recordsRate)

        points = random.randint(0, 1)

        if (points >= 1):
            ListOfComments = random.choice(positive_descriptions)
        else:
            ListOfComments = random.choice(negative_descriptions)

        StartOfService = random.randint(2005, 2019)

        data.append((badge_number, pesel, first_name,
                     surname, job_title, job_rank, 0, address, "Gdansk", AvrageRating, ListOfComments, StartOfService, points))
    return data


def excelCriminals(officer_data, num_recordsPolice):
    data = []
    for _ in range(num_recordsPolice):
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


# Generate data
people_data = generate_people_data(number_of_people)
officer_data = generate_officer_data(number_of_policeman, people_data)
criminal_data = generate_criminal_data(number_of_criminals, people_data)
officer_badge_numbers = [record[0] for record in officer_data]
criminal_ids = [record[0] for record in criminal_data]
ticket_data, pairs = generate_ticket_data(
    amount_of_ticketsT1, officer_badge_numbers, criminal_ids, pairs, 0, criminal_data)
rating_data = generate_rating_data(amount_of_RatingsT1, pairs, 0)

# Write data to bulk files
write_to_bulk_file(officer_data, 'officer_data.csv')
write_to_bulk_file(criminal_data, 'criminal_data.csv')
write_to_bulk_file(ticket_data, 'ticket_data.csv')
write_to_bulk_file(rating_data, 'rating_data.csv')

# T2
people_data = generate_FEWMOREpeople_data(number_of_newpeople, people_data)
officer_data_new = generate_FEWMOREofficer_data(
    number_of_newpoliceman, people_data)
criminal_data_new = generate_FEWMOREcriminal_data(
    number_of_newcriminals, people_data)
officer_badge_numbers = [record[0] for record in officer_data]
criminal_ids = [record[0] for record in criminal_data]
ticket_dataT2, pairs = generate_ticket_data(
    amount_of_ticketsT2, officer_badge_numbers, criminal_ids, pairs, 1,  criminal_data)
rating_dataT2 = generate_rating_data(amount_of_RatingsT2, pairs, 1)

# Write data to bulk files
write_to_bulk_file(officer_data_new, 'officer_dataT2.csv')
write_to_bulk_file(criminal_data_new, 'criminal_dataT2.csv')
write_to_bulk_file(ticket_dataT2, 'ticket_dataT2.csv')
write_to_bulk_file(rating_dataT2, 'rating_dataT2.csv')

excelpolicamn_data = excelpolicamn(
    officer_data, rating_data, number_of_policeman, amount_of_RatingsT1)
write_to_bulk_fileEX(excelpolicamn_data, 'officer_data_Excel.csv')

excelCriminals_data = excelCriminals(criminal_data, number_of_criminals)
write_to_bulk_fileEX(excelCriminals_data, 'criminals_data_Excel.csv')


officer_data_all = officer_data + officer_data_new
amount_of_Ratingsall = amount_of_RatingsT1 + amount_of_RatingsT2
number_of_policemanall = number_of_policeman + number_of_newpoliceman
rating_dataall = rating_dataT2 + rating_data
Criminals_dataall = criminal_data + criminal_data_new


excelpolicamn_dataT2 = excelpolicamn(
    officer_data_all, rating_dataall, number_of_policemanall, amount_of_Ratingsall)
write_to_bulk_fileEX(excelpolicamn_dataT2, 'officer_data_ExcelT2.csv')


excelCriminals_data = excelCriminals(criminal_data, number_of_criminals)
write_to_bulk_fileEX(excelCriminals_data, 'criminals_data_ExcelT2.csv')
