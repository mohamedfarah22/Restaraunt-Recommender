from turtle import title


def welcome_to_restaurant_recommender():
    print('''-------------------------------------------\n\n     Weclome to Restaurant Recommender!!! \n \n -------------------------------------------''')
    

# helper functions
def remove_duplicates(list):
    new_list = []
    for item in list:
        if item in new_list:
            continue
        new_list.append(item)
    return new_list    
def get_user_category_input():
    category = input('What category of food would you like to eat: ')
    return  category.capitalize()
def get_meal_type():
    meal_type = input('What meal type are you having: ')
    return meal_type.capitalize()
def get_dietary_requirement():
    dietary_requirement= input('What is your dietary requirements?: ')  
    return dietary_requirement.capitalize()
def get_price_input():
    price_point = input('What is your desired price point? (Choose a number from 1 to 5 where 1 is the cheapest and 5 is the most expensive): ')
    return price_point
