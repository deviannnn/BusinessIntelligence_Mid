import pandas as pd

data = pd.read_csv('dataset_full.csv')
data_clean = []

def process_currency_string(currency_str):
    comma_count = currency_str.count(',')

    if comma_count >= 2:
        parts = currency_str.replace('₹', '').split('.')

        integer_part = parts[0].replace(',', '')
        result = ''
        for i, digit in enumerate(reversed(integer_part)):
            if i > 0 and i % 3 == 0:
                result += ','
            result += digit

        result = '₹' + result[::-1]

        if len(parts) > 1:
            result += '.' + parts[1]

        return result
    else:
        return currency_str
          
def convert_to_number(a):
  if isinstance(a, str):
    return int(float(a.replace(",", "")))
  else:
    return int(a)
    
for idx, row in data.iterrows():
    new_row = row.copy()

    if pd.isnull(row['ratings']) or pd.isnull(row['no_of_ratings']) or pd.isnull(row['actual_price']) or row['no_of_ratings'][0].isdigit() == 0 or row['ratings'][0].isdigit() == 0:
        continue
    else:
        new_row['no_of_ratings'] = convert_to_number(row['no_of_ratings'])
        new_row['discount_price'] = process_currency_string(row['discount_price']) if pd.notnull(row['discount_price']) else None
        new_row['actual_price'] = process_currency_string(row['actual_price'])
        data_clean.append(new_row)
    
dataset_cleaned = pd.DataFrame(data_clean)
dataset_cleaned.to_csv('filter_data.csv', index=False)