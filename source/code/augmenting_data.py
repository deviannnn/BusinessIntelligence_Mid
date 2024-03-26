import pandas as pd
import numpy as np
import random 

data = pd.read_csv('dataset_cleaned.csv')

dataset_augmented = []
num_copies = 100

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
    "Dallas", "Austin", "Jacksonville", "San Jose", "Fort Worth", "Columbus", "Charlotte", "Indianapolis",
    "San Francisco", "Seattle", "Denver", "Oklahoma City", "Nashville", "El Paso", "Washington", "Las Vegas",
    "Boston", "Portland", "Louisville", "Memphis", "Detroit", "Baltimore", "Milwaukee", "Albuquerque", "Tucson",
    "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Colorado Springs", "Omaha", "Raleigh",
    "Virginia Beach", "Long Beach", "Miami", "Oakland", "Minneapolis", "Tulsa", "Bakersfield", "Tampa", "Wichita",
    "Arlington", "Aurora", "New Orleans", "Cleveland", "Anaheim", "Honolulu", "Henderson", "Stockton", "Riverside",
    "Lexington", "Corpus Christi", "Orlando", "Irvine", "Cincinnati", "Santa Ana", "Newark", "Saint Paul", "Pittsburgh",
    "Greensboro", "Lincoln", "Durham", "Plano", "Anchorage", "Jersey City", "St. Louis", "Chandler", "North Las Vegas",
    "Chula Vista", "Buffalo", "Gilbert", "Reno", "Madison", "Fort Wayne", "Toledo", "Lubbock", "St. Petersburg", "Laredo",
    "Irving", "Chesapeake", "Glendale", "Winston-Salem", "Scottsdale", "Garland", "Boise", "Norfolk", "Port St. Lucie",
    "Spokane", "Richmond", "Fremont", "Huntsville", "Tacoma", "Baton Rouge", "Santa Clarita", "San Bernardino", "Hialeah",
    "Frisco", "Modesto", "Cape Coral", "Fontana", "Moreno Valley", "Des Moines", "Rochester", "Fayetteville", "Yonkers",
    "McKinney", "Worcester", "Salt Lake City", "Little Rock", "Columbus", "Augusta", "Sioux Falls", "Grand Prairie",
    "Tallahassee", "Amarillo", "Oxnard", "Peoria", "Overland Park", "Montgomery", "Birmingham", "Grand Rapids",
    "Knoxville", "Vancouver", "Huntington Beach", "Providence", "Brownsville", "Glendale", "Akron", "Tempe",
    "Newport News", "Chattanooga", "Mobile", "Fort Lauderdale", "Cary", "Shreveport", "Ontario", "Eugene", "Aurora",
    "Elk Grove", "Salem", "Santa Rosa", "Clarksville", "Rancho Cucamonga", "Oceanside", "Springfield", "Pembroke Pines",
    "Garden Grove", "Fort Collins", "Lancaster", "Palmdale", "Murfreesboro", "Salinas", "Corona", "Killeen", "Hayward",
    "Paterson", "Macon", "Lakewood", "Alexandria", "Roseville", "Surprise", "Springfield", "Charleston", "Kansas City",
    "Sunnyvale", "Bellevue", "Hollywood", "Denton", "Escondido", "Joliet", "Naperville", "Bridgeport", "Savannah",
    "Mesquite", "Pasadena", "Rockford", "Pomona", "Jackson", "Olathe", "Gainesville", "McAllen", "Syracuse", "Waco",
    "Visalia", "Thornton", "Torrance", "Fullerton", "Columbia", "Lakewood", "New Haven", "Hampton", "Miramar",
    "Victorville", "Warren", "West Valley City", "Cedar Rapids", "Stamford", "Orange", "Dayton", "Midland", "Kent",
    "Elizabeth", "Pasadena", "Carrollton", "Coral Springs", "Sterling Heights", "Fargo", "Lewisville", "Meridian",
    "Norman", "Palm Bay", "Athens", "Columbia", "Abilene", "Pearland", "Santa Clara", "Round Rock", "Topeka",
    "Allentown", "Clovis", "Simi Valley", "College Station", "Thousand Oaks", "Vallejo", "Concord", "Rochester",
    "Arvada", "Lafayette", "Independence", "West Palm Beach", "Hartford", "Wilmington", "Lakeland", "Billings",
    "Ann Arbor", "Fairfield", "Berkeley", "Richardson", "North Charleston", "Cambridge", "Broken Arrow", "Clearwater",
    "West Jordan", "Evansville", "League City", "Antioch", "Manchester", "High Point", "Waterbury", "Westminster",
    "Richmond", "Carlsbad", "Las Cruces", "Murrieta", "Lowell", "Provo", "Springfield", "Elgin", "Odessa", "Lansing",
    "Pompano Beach", "Beaumont", "Temecula", "Gresham", "Allen", "Pueblo", "Everett", "South Fulton", "Peoria", "Nampa",
    "Tuscaloosa", "Miami Gardens", "Santa Maria", "Downey", "Concord", "Ventura", "Costa Mesa", "Sugar Land", "Menifee",
    "Tyler", "Sparks", "Greeley", "Rio Rancho", "Sandy Springs", "Dearborn", "Jurupa Valley", "Edison", "Spokane Valley",
    "Hillsboro", "Davie", "Green Bay", "Centennial", "Buckeye", "Boulder", "Goodyear", "El Monte", "West Covina",
    "Brockton", "New Braunfels", "El Cajon", "Edinburg", "Renton", "Burbank", "Inglewood", "Rialto", "Lee's Summit",
    "Bend", "Woodbridge", "South Bend", "Wichita Falls", "St. George", "Fishers", "Carmel", "Vacaville", "Quincy",
    "Conroe", "Chico", "San Mateo", "Lynn", "Albany", "Hesperia", "New Bedford", "Davenport", "Daly City"
]

avg_subcate_each_code = {}
with open('avg_subcate_each_code.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 2:
            product_code = parts[0].strip()
            avg_value = int(parts[1].strip())
            avg_subcate_each_code[product_code] = avg_value

def target_profit_linear_scaling(no_of_ratings, avg_per_sub):
    scaling_factor = no_of_ratings / avg_per_sub
    
    if scaling_factor > 2.5:
        scaling_factor = 2.5
    if scaling_factor <= 1:
        scaling_factor = 1.75
    
    max_target_profit = int(round(no_of_ratings * scaling_factor))
    return max_target_profit


def generate_random_profit(no_of_ratings, avg_per_sub):
    random_profits = np.zeros(len(cities)).astype(int)

    max_target_profit = target_profit_linear_scaling(no_of_ratings, avg_per_sub)

    target_profit = np.random.randint(no_of_ratings, max_target_profit)
    
    while sum(random_profits) != target_profit:
        idx = np.random.choice(len(cities))

        if sum(random_profits) < target_profit:
            random_profits[idx] += np.random.choice([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5])
        else:
            random_profits[idx] = max(0, random_profits[idx] - np.random.choice([1, 2, 3, 3, 3, 4, 4, 5, 5]))

    return random.sample(list(random_profits), num_copies)

def generate_random_city():
    return random.sample(cities, num_copies)

def extract_code_from_link(link):
    split_link = link.split('/')
    return split_link[5] if len(split_link) == 7 else split_link[4]

global_id = 0
global_id_by_category = 0
previous_sub_category = ""
random_values = {}
final = pd.DataFrame()

for _, row in data.iterrows():
    if row['sub_category'] != previous_sub_category:
        global_id_by_category = 0
        previous_sub_category = row['sub_category']

    current_code = extract_code_from_link(row['link'])
    if current_code not in random_values:
        random_values[current_code] = {
            'profits': generate_random_profit(row['no_of_ratings'], avg_subcate_each_code.get(current_code, 0)),
            'cities': generate_random_city()
        }

    random_profits = random_values[current_code]['profits']
    random_cities = random_values[current_code]['cities']
    
    for i in range(num_copies):
        new_row = row.copy()
        new_row['_'] = global_id
        new_row['id'] = global_id
        global_id += 1
        new_row['id_by_category'] = global_id_by_category
        global_id_by_category += 1
        new_row['profit'] = random_profits[i]
        new_row['city'] = random_cities[i]

        final = pd.concat([final, pd.DataFrame([new_row])], ignore_index=True)
        final.to_csv('dataset_augmented.csv', index=False)

final.to_csv('dataset_augmented.csv', index=False)