#restaurant recommender script
import restaurant_data
from tree_data_structure import TreeNode
import linked_list
from welcome import remove_duplicates
from linked_list import Restaurant_object
all_restaurant_data = restaurant_data.all_restaurant_data
restaurant_categories = restaurant_data.restaurant_category
restaurant_meal_types = restaurant_data.restaurant_meal_type
restaurant_dietary_requirements = ['Halal', 'Vegan', 'Vegetarian', 'Gluten Free', 'Dairy Free']
restaurant_price = restaurant_data.restaurant_price
#remove duplicate from above categories
#import duplicate removing helper functions from welcome.py and apply it to each filter
restaurant_categories = remove_duplicates(restaurant_categories)
restaurant_meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Brunch', 'Cafe']
restaurant_price = remove_duplicates(restaurant_price)
# init tree node for restaurant recommender
restaurant_recommender = TreeNode()
#add categories, meal type, price to tree node
restaurant_recommender.add_category_node(restaurant_categories)
restaurant_recommender.add_meal_type_node(restaurant_meal_types)
restaurant_recommender.add_dietary_requirement(restaurant_dietary_requirements)
restaurant_recommender.add_price_point_node(restaurant_price)
restaurant_recommender.show_children_dict()
# create a restaurant node for each restaurant.

