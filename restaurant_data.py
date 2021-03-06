import pandas as pd
import numpy as np
import os
pre = os.path.dirname(os.path.realpath(__file__))
fname = 'south yarra refined data.xlsx'
path = os.path.join(pre, fname)
df = pd.read_excel(path, 0) # can also index sheet by name or fetch all sheets
restaurant_names = df['Name'].tolist()
restaurant_ratings = df['Rating'].tolist()
restaurant_price = df['Price'].tolist()
restaurant_category = df['Category'].tolist()
restaurant_type = df['Type'].tolist()
restaurant_address = df['Address'].tolist()
restaurant_suburb = df['Suburb'].tolist()
restaurant_meal_type = df['Meal Type'].tolist()
restaurant_dietary_requirements = df['Dietary Requirements Available'].replace({np.nan: 'None'}).tolist()
restaurant_short_description = df['Short Description'].tolist()
all_restaurant_data = []

for name in restaurant_names:
    all_restaurant_data.append([name])
index = 0
for restaurant in all_restaurant_data:
    restaurant.append(restaurant_ratings[index])
    restaurant.append(restaurant_price[index])
    restaurant.append(restaurant_category[index])
    restaurant.append(restaurant_type[index])
    restaurant.append(restaurant_address[index])
    restaurant.append(restaurant_suburb[index])
    restaurant.append(restaurant_meal_type[index])
    restaurant.append(restaurant_dietary_requirements[index])
    restaurant.append(restaurant_short_description[index])
    index+=1




#print(restaurant_names,restaurant_ratings,restaurant_price, restaurant_category, restaurant_type, restaurant_address, restaurant_suburb, restaurant_meal_type, restaurant_dietary_requirements, restaurant_short_description)
