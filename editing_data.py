# Data manipulation and analysis
import pandas as pd

# Load the dataset
df = pd.read_csv('airbnb_listings.csv')
# Change the names of columns
df.rename(columns={'neighbourhood':'neighbourhood_type', 'neighbourhood_cleansed':'Neighbourhood',
                   'room_type':'Room type', 'accommodates':'Capacity (number of people)',
                   'instant_bookable':'Instant Booking', 'has_availability':'Availability',
                   'host_is_superhost':'Superhost'}, inplace=True)

# Remove the specific substring '</b>' from the values in the 'description' column
df['description'] = df['description'].str.replace('</b>', '')
# Remove the "$" symbol and convert to float format
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
# Replace a specific price outlier 99149.000000 with a corrected value 99.149
# Assuming it was a typo in which a comma and a period were mixed up
df['price'] = df['price'].replace(99149.000000, 99.149)

# Sort the DataFrame by price in ascending order
df.sort_values(by='price', ascending=True, inplace=True)
# Define a function to categorize prices into groups
def get_price_group(x):
    if x<=40:
        return '10-40'
    elif 40<x<=60:
        return '41-60'
    elif 60<x<=80:
        return '61-80'
    elif 80<x<=100:
        return '81-100'
    elif 100<x<=130:
        return '101-130'
    elif 130<x<=160:
        return '131-160'
    elif 160<x<=200:
        return '161-200'
    elif 200<x<=300:
        return '201-300'
    else:
        return '300+' 

# Apply the function to create a new column 'Price Range, $' based on 'price'
df['Price Range, $'] = df['price'].apply(get_price_group)

# Replace 't' with 'yes' and 'f' with 'no' in selected columns
df['Instant Booking'] = df['Instant Booking'].replace({'t': 'yes', 'f': 'no'})
df['Superhost'] = df['Superhost'].replace({'t': 'yes', 'f': 'no'})
df['Availability'] = df['Availability'].replace({'t': 'yes', 'f': 'no'})