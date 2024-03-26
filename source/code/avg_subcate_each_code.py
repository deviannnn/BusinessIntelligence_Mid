import pandas as pd

df = pd.read_csv('dataset_cleaned.csv')

def extract_code_from_link(link):
    split_link = link.split('/')
    return split_link[5] if len(split_link) == 7 else split_link[4]

df['Product Code'] = df['link'].apply(extract_code_from_link)

avg_per_sub = {'Air Conditioners': 278, 'All Appliances': 943, 'All Car & Motorbike Products': 693, 'All Electronics': 8807, 'All Exercise & Fitness': 755, 'All Grocery & Gourmet Foods': 876, 'All Home & Kitchen': 3185, 'All Pet Supplies': 842, 'All Sports, Fitness & Outdoors': 651, 'Amazon Fashion': 3060, 'Baby Bath, Skin & Grooming': 1429, 'Baby Fashion': 160, 'Baby Products': 6389, 'Backpacks': 841, 'Badminton': 90, 'Bags & Luggage': 391, 'Ballerinas': 78, 'Beauty & Grooming': 1178, 'Bedroom Linen': 296, 'Camera Accessories': 2518, 'Cameras': 2500, 'Camping & Hiking': 243, 'Car & Bike Care': 236, 'Car Accessories': 98, 'Car Electronics': 237, 'Car Parts': 90, 'Cardio Equipment': 87, 'Casual Shoes': 228, 'Clothing': 350, 'Coffee, Tea & Beverages': 368, 'Cricket': 102, 'Cycling': 308, 'Diapers': 3581, 'Diet & Nutrition': 389, 'Dog supplies': 587, 'Ethnic Wear': 185, 'Fashion & Silver Jewellery': 121, 'Fashion Sales & Deals': 55, 'Fashion Sandals': 49, 'Fitness Accessories': 152, 'Football': 148, 'Formal Shoes': 86, 'Furniture': 279, 'Garden & Outdoors': 285, 'Gold & Diamond Jewellery': 32, 'Handbags & Clutches': 116, 'Headphones': 5140, 'Health & Personal Care': 3669, 'Heating & Cooling Appliances': 355, 'Home Audio & Theater': 312, 'Home Décor': 313, 'Home Entertainment Systems': 2005, 'Home Furnishing': 671, 'Home Improvement': 884, 'Home Storage': 410, 'Household Supplies': 381, 'Indoor Lighting': 228, 'Industrial & Scientific Supplies': 862, 'Innerwear': 222, 'International Toy Store': 938, 'Janitorial & Sanitation Supplies': 317, 'Jeans': 125, 'Jewellery': 52, "Kids' Clothing": 184, "Kids' Fashion": 327, "Kids' Shoes": 297, "Kids' Watches": 160, 'Kitchen & Dining': 793, 'Kitchen & Home Appliances': 796, 'Kitchen Storage & Containers': 593, 'Lab & Scientific': 94, 'Lingerie & Nightwear': 179, 'Luxury Beauty': 568, 'Make-up': 479, "Men's Fashion": 675, 'Motorbike Accessories & Parts': 156, 'Musical Instruments & Professional Audio': 346, 'Nursing & Feeding': 721, 'Personal Care Appliances': 486, 'Refrigerators': 297, 'Refurbished & Open Box': 4, 'Rucksacks': 370, 'Running': 316, 'STEM Toys Store': 1566, 'School Bags': 475, 'Security Cameras': 359, 'Sewing & Craft Supplies': 396, 'Shirts': 78, 'Shoes': 336, 'Snack Foods': 446, 'Speakers': 1652, 'Sports Shoes': 257, 'Sportswear': 424, 'Strength Training': 235, 'Strollers & Prams': 621, 'Suitcases & Trolley Bags': 148, 'Sunglasses': 318, 'T-shirts & Polos': 120, 'Televisions': 2489, 'Test, Measure & Inspect': 273, 'The Designer Boutique': 74, 'Toys & Games': 1423, 'Toys Gifting Store': 5352, 'Travel Accessories': 276, 'Travel Duffles': 167, 'Value Bazaar': 31115, 'Wallets': 401, 'Washing Machines': 399, 'Watches': 118, 'Western Wear': 142, "Women's Fashion": 492, 'Yoga': 142}

df_avg_per_sub = pd.DataFrame(list(avg_per_sub.items()), columns=['sub_category', 'avg_per_sub'])

df = pd.merge(df, df_avg_per_sub, on='sub_category', how='left')

result = df.groupby('Product Code').agg({'avg_per_sub': 'mean'}).reset_index()
result['avg_per_sub'] = result['avg_per_sub'].round().astype(int)

result_dict = dict(zip(result['Product Code'], result['avg_per_sub']))

with open('result_dict.txt', 'w') as file:
    for product_code, avg_per_sub in result_dict.items():
        file.write(f'{product_code}: {avg_per_sub}\n')