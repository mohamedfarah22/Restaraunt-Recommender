#restaurant recommender script
from cmath import nan
from http.client import OK
from xmlrpc.client import NOT_WELLFORMED_ERROR
import restaurant_data
from tree_data_structure import TreeNode
import linked_list
from welcome import get_dietary_requirement, get_meal_type, get_price_input, get_user_category_input, remove_duplicates, welcome_to_restaurant_recommender
from linked_list import Restaurant_object
welcome_to_restaurant_recommender()
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
def category_selection():
 category_input = get_user_category_input()
 possible_categories =restaurant_recommender.find_category(category_input)
 if len(possible_categories)==1:
  print(possible_categories)
 while len(possible_categories)>1 or len(possible_categories)==0:
     if len(possible_categories)==0:
        print('No categories match your input! Please try a different input')
     else:
        print(possible_categories)
     category_input = get_user_category_input()
     possible_categories =restaurant_recommender.find_category(category_input)
 category_to_index = possible_categories[0]
 print("You have chosen to eat at a {} restaurant".format(category_to_index))
 return category_to_index

#meal type selection based on user in put
def meal_type_selection(category_to_index):
 meal_type_input = get_meal_type()
 possible_meal_types = restaurant_recommender.find_meal_type(category_to_index, meal_type_input)
 while len(possible_meal_types)>1 or len(possible_meal_types)==0:
    if len(possible_meal_types)==0:
        print('No meal types match your input! Please try a different input')
    else:
       print(possible_meal_types) 
    meal_type_input = get_meal_type()
    possible_meal_types = restaurant_recommender.find_meal_type(category_to_index, meal_type_input)  
 meal_type_input_to_index = possible_meal_types[0]
 print("You are planning to eat {}".format(meal_type_input_to_index))
 return meal_type_input_to_index

# dietary requirement selection based on user 
def dietary_requirements_selection(category_to_index, meal_type_input_to_index):
 dietary_requirement_input = get_dietary_requirement()
 possible_dietary_requirements = restaurant_recommender.find_dietary_requirements(category_to_index, meal_type_input_to_index, dietary_requirement_input)
 while len(possible_dietary_requirements)>1 or len(possible_dietary_requirements)==0:
    if len(possible_dietary_requirements)==0:
        print('No meal types match your input! Please try a different input')
    else:
       print(possible_dietary_requirements) 
    dietary_requirement_input = get_dietary_requirement()
    possible_dietary_requirements = restaurant_recommender.find_dietary_requirements(category_to_index, meal_type_input_to_index, dietary_requirement_input)
 dietary_requirement_to_index= possible_dietary_requirements[0]
 print("Your dietary requirement is {}".format(dietary_requirement_to_index))
 return dietary_requirement_to_index

# price point selection based on user
def price_point_selection():
 price_input = get_price_input()
 price_point_to_index = restaurant_recommender.find_price_point(price_input)
 return price_point_to_index

# retrieving restaurant recommendation
def retrieve_restaurants(category_to_index, meal_type_input_to_index, dietary_requirement_to_index, price_point_to_index):
 all_relevant_restaurants = restaurant_recommender.find_restaurants(category_to_index, meal_type_input_to_index, dietary_requirement_to_index, price_point_to_index)
 if len(all_relevant_restaurants)>0:
  for restaurant in all_relevant_restaurants:
    restaurant.get_restaurant()
 else:
    print('No restaurants available for your criteria! Please try again!')
 return all_relevant_restaurants

# Execute Program
all_relevant_restaurants = []
while len(all_relevant_restaurants)==0:
    category_type = category_selection()
    meal_type = meal_type_selection(category_type)
    dietary_requirement = dietary_requirements_selection(category_type, meal_type)
    price_point = price_point_selection()
    all_relevant_restaurants=retrieve_restaurants(category_type, meal_type, dietary_requirement, price_point)

