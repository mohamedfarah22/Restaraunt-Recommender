from collections import deque
from unicodedata import category
from linked_list import Restaurant_object
class TreeNode:
  def __init__(self):
    
    self.children = {} # references to other nodes
 
  def add_category_node(self, category_list):
   for category in category_list:
    self.children[category]={}
  
  def add_meal_type_node(self,meal_type):
    for meal in meal_type:
      for key in self.children.keys():
        if meal in self.children[key].keys():
          print('{meal} is already in tree'.format(meal))
        self.children[key][meal] = {}
  
  def add_price_point_node(self,price_point_list):
    for price in price_point_list:
      for key in self.children.keys():
        for key2 in self.children[key].keys():
          for key3 in self.children[key][key2].keys():
            if price in self.children[key][key2][key3].keys():
              print('{price} is already in tree'.format(price))
            self.children[key][key2][key3][price]=[]
  def add_dietary_requirement(self, dietary_requirements_list):
     for dietary_requirement in dietary_requirements_list:
      for key in self.children.keys():
        for key2 in self.children[key].keys():
          if dietary_requirement in self.children[key][key2].keys():
            print('{dietary_requirement} is already in tree'.format(dietary_requirement))
          self.children[key][key2][dietary_requirement]={}


  def show_children_dict(self):
    print(self.children)
  
  
  def add_restaurant(self,list):
    for restaurant in list:
     parameters_dict= {}
     parameters_dict['categories'] = restaurant[3].split(',')
     parameters_dict['meal_type'] = restaurant[7].split(',')
     parameters_dict['dietary_requirements']= restaurant[8].split(',')
     parameters_dict['price_point'] = restaurant[2].split(',')
     for category in parameters_dict['categories']:  
      category = category.strip()
      for meal_type in parameters_dict['meal_type']:
        meal_type = meal_type.strip()
        for dietary_requirement in parameters_dict['dietary_requirements']:
          dietary_requirement = dietary_requirement.strip()
          for price in parameters_dict['price_point']:
             price.split()
             self.children[category][meal_type][dietary_requirement][price].append(Restaurant_object(restaurant))
  def find_category(self, target):
    possible_categories = []
    for key in self.children.keys():
      if target in key:
        possible_categories.append(key)
    return possible_categories
  def find_meal_type(self,category, target):
    possible_meal_types = []
    for key in self.children[category].keys():
      if target in key:
        possible_meal_types.append(key)
    return possible_meal_types
  def find_dietary_requirements(self, category, meal_type, target):
    possible_dietary_requirements = []
    for key in self.children[category][meal_type].keys():
      if target in key:
        possible_dietary_requirements.append(key)
    return possible_dietary_requirements
  
  def find_price_point(self, category, meal_type, dietary_requirement, target):
    price_point_string = ''
    target = int(target)
    for i in range(target):
      price_point_string+='$'
    return price_point_string
  def find_restaurants(self, category, meal_type, dietary_requirement, price_point):
    return self.children[category][meal_type][dietary_requirement][price_point]  
  


    
  
 



  