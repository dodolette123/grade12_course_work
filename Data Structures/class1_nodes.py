class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

snacks = Node("Peanuts")
drinks = Node("Cola")
fruit = Node("Strawberry")

snacks.set_link_node(drinks)
drinks.set_link_node(fruit)

drinks_data = snacks.get_link_node().get_value()
fruit_data = drinks.get_link_node().get_value()
print(drinks_data)
print(fruit_data)

print(snacks.get_value())
print(snacks.get_link_node().get_link_node().get_value())