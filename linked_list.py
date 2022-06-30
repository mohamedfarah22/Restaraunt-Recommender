class Restaurant_object:
  def __init__(self, value, next_node=None):
    self.name = value[0]
    self.rating = value[1]
    self.price = value[2]
    self.category = value[3]
    self.type = value[4]
    self.address = value[5]
    self.suburb = value[6]
    self.meal_type = value[7]
    self.dietary_requirements_available = value[8]
    self.short_description = value[9]
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_restaurant(self):
    print( """------------\n Restaurant Name: {} \n Address: {} \n Rating: {}/5 \n Description: {} """.format(self.name, self.address + ", " + self.suburb, self.rating, self.short_description))
  def get_name(self):
    return self.name
  def get_restaurant_category(self):
    return str(self.category)



class LinkedList:
  def __init__(self, value=None):
    self.head_node = Restaurant_object(value)
 
  def get_head_node(self):
    return self.head_node
 
  def insert_beginning(self, new_value):
    new_node = Restaurant_object(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
 
  def stringify_list(self):
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_name() != None:
         current_node.get_restaurant()
      current_node = current_node.get_next_node()
    
 
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node