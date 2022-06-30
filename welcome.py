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
def add_restaurants_to_tree(all_restaurants,TreeNode):
  for restaurant in all_restaurants:
    category = restaurant[3]
    meal_type = restaurant[7]
    meal_type_list = meal_type.split(',')
    dietary_requirements = restaurant[8]
    dietary_requirements_list = dietary_requirements.split(',')
    price = restaurant[2]
    for meal in meal_type:
        if meal not in meal_type_list:
           meal_type_list.append(meal)
    for dietary_requirement in dietary_requirements_list:
        if dietary_requirement not in dietary_requirements_list:
           dietary_requirements_list.append(dietary_requirement)
    

    
