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
  def get_restaurant(self):
    print( """------------\n Restaurant Name: {} \n Address: {} \n Rating: {}/5 \n Description: {} """.format(self.name, self.address + ", " + self.suburb, self.rating, self.short_description))
  def get_name(self):
    return self.name
  def get_restaurant_category(self):
    return str(self.category)



    
 
  