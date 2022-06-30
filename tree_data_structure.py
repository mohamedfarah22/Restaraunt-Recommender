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
  # finish logic for adding restaurants to tree
  
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


    
  


    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]
 
  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the  frontier
    for child in current_node.children:
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path) 