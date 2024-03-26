import pandas as pd

df = pd.read_csv('dataset_cleaned.csv')

def extract_code_from_link(link):
    split_link = link.split('/')
    return split_link[5] if len(split_link) == 7 else split_link[4]

df['Product Code'] = df['link'].apply(extract_code_from_link)

result = df.groupby(['sub_category', 'Product Code']).agg({'no_of_ratings': 'max'}).reset_index()
result = result.groupby('sub_category').agg({'no_of_ratings': lambda x: round(x.mean())}).reset_index()

avg_per_sub = dict(zip(result['sub_category'], result['no_of_ratings']))

print(avg_per_sub)