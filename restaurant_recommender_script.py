#restaurant recommender script
from cmath import nan
from http.client import OK
from xmlrpc.client import NOT_WELLFORMED_ERROR
import restaurant_data
from tree_data_structure import TreeNode
import linked_list
from welcome import get_dietary_requirement, get_meal_type, get_price_input, get_user_category_input, remove_duplicates
from linked_list import Restaurant_object
all_restaurant_data = restaurant_data.all_restaurant_data
restaurant_categories = restaurant_data.restaurant_category
restaurant_meal_types = restaurant_data.restaurant_meal_type
restaurant_dietary_requirements = ['Halal', 'Vegan', 'Vegetarian', 'Gluten Free', 'Dairy Free', 'None']
restaurant_price = restaurant_data.restaurant_price
#remove duplicate from above categories
#import duplicate removing helper functions from welcome.py and apply it to each filter
restaurant_categories = remove_duplicates(restaurant_categories)
restaurant_meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Brunch', 'Café', 'Bakery']
restaurant_price = remove_duplicates(restaurant_price)
# init tree node for restaurant recommender
restaurant_recommender = TreeNode()
#add categories, meal type, price to tree node
restaurant_recommender.add_category_node(restaurant_categories)
restaurant_recommender.add_meal_type_node(restaurant_meal_types)
restaurant_recommender.add_dietary_requirement(restaurant_dietary_requirements)
restaurant_recommender.add_price_point_node(restaurant_price)
#restaurant_recommender.show_children_dict()
# create a restaurant node for each restaurant 
restaurant_recommender.add_restaurant(all_restaurant_data)

#recommender program based on user input(category)
category_input = get_user_category_input()
possible_categories =restaurant_recommender.find_category(category_input)
print(possible_categories)
while len(possible_categories)>1:
    category_input = get_user_category_input()
    possible_categories =restaurant_recommender.find_category(category_input)
    print(possible_categories)
category_to_index = possible_categories[0]

#meal type selection based on user in put
meal_type_input = get_meal_type()
possible_meal_types = restaurant_recommender.find_meal_type(category_to_index, meal_type_input)
print(possible_meal_types)
while len(possible_meal_types)>1:
    meal_type_input = get_meal_type()
    possible_meal_types = restaurant_recommender.find_meal_type(category_to_index, meal_type_input)
    print(possible_meal_types)
meal_type_input_to_index = possible_meal_types[0]

# dietary requirement selection based on user 

dietary_requirement_input = get_dietary_requirement()
possible_dietary_requirements = restaurant_recommender.find_dietary_requirements(category_to_index, meal_type_input_to_index, dietary_requirement_input)
print(possible_dietary_requirements)
while len(possible_dietary_requirements)>1:
    dietary_requirement_input = get_dietary_requirement()
    possible_dietary_requirements = restaurant_recommender.find_dietary_requirements(category_to_index, meal_type_input_to_index, dietary_requirement_input)
    print(possible_dietary_requirements)
dietary_requirement_to_index= possible_dietary_requirements[0]

# price point selection based on user

price_input = get_price_input()
price_point_to_index = restaurant_recommender.find_price_point(category_to_index, meal_type_input_to_index, dietary_requirement_to_index, price_input)

# retrieving restaurant recommendation

all_relevant_restaurants = restaurant_recommender.find_restaurants(category_to_index, meal_type_input_to_index, dietary_requirement_to_index, price_point_to_index)
for restaurant in all_relevant_restaurants:
    restaurant.get_restaurant()

