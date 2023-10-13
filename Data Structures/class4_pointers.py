class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_node):
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
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
# Complete this function:
def nth_last_node(linked_list, n):
  current = None
  tail_pointer = linked_list.head_node
  count = 0
  while tail_pointer:
    tail_pointer = tail_pointer.get_next_node()
    count += 1
    if count >= n + 1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(10, 0, -1): 
    k = Node(i)
    linked_list.insert_beginning(k)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.get_value())
def find_middle_alt(linked_list):
    slow_ptr = linked_list.head_node
    fast_ptr = linked_list.head_node
    if linked_list.head_node is not None:
        while (fast_ptr is not None and fast_ptr.get_next_node() is not None):
            fast_ptr = fast_ptr.get_next_node().get_next_node() 
            if fast_ptr is not None:
                slow_ptr = slow_ptr.get_next_node() 
        return slow_ptr

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(11): 
    k = Node(i)
    linked_list.insert_beginning(k)
  return linked_list
"""
test_list = generate_test_linked_list()
print(test_list.stringify_list())
middle_node = find_middle_alt(test_list)
print(middle_node.get_value())
"""