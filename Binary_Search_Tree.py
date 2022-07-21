class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right =  None
        self.height = 1

  def __init__(self):
      self.__root = None
  
  def __balance(self, current_node):
      if self.__get_balance_value(current_node) == 0 or self.__get_balance_value(current_node) == 1 or self.__get_balance_value(current_node) == -1:
          return current_node #Base case
      if self.__get_balance_value(current_node) == -2: #Left heavy
          if self.__get_balance_value(current_node.left) == -1 or self.__get_balance_value(current_node.left) == 0: #Left left
              return self.__rotate_right(current_node)
          if self.__get_balance_value(current_node.left) == 1: #Left right
              current_node.left = self.__rotate_left(current_node.left) #First part of double rotation
              return self.__rotate_right(current_node) #Second part of double rotation
      if self.__get_balance_value(current_node) == 2: #Right heavy
          if self.__get_balance_value(current_node.right) == 1 or self.__get_balance_value(current_node.right) == 0: #Right right
              return self.__rotate_left(current_node)
          if self.__get_balance_value(current_node.right) == -1: #Right left
              current_node.right = self.__rotate_right(current_node.right)#First part of double rotation
              return self.__rotate_left(current_node)
               
  def __rotate_left(self, current_node):
      pivot = current_node.right
      current_node.right = pivot.left
      pivot.left = current_node
      self.__calc_height(current_node)
      self.__calc_height(pivot)
      return pivot
          
  def __rotate_right(self, current_node):
      pivot = current_node.left
      current_node.left = pivot.right
      pivot.right = current_node
      self.__calc_height(current_node)
      self.__calc_height(pivot)
      return pivot
          
  def __get_balance_value(self, current_node):
      left = 0
      right = 0
      if current_node.left is not None: #If the current node has a left or right child then it will collect their heights
          left += current_node.left.height
      if current_node.right is not None:
          right += current_node.right.height
      balance_value = right - left
      return balance_value
          
  def insert_element(self, value):
      self.__root = self.__insert_element(value, self.__root)
      
  def __insert_element(self, value, current_node):
      if current_node is None: #Base case
          current_node = Binary_Search_Tree.__BST_Node(value)
          return current_node
      elif value < current_node.value:
          current_node.left = self.__insert_element(value, current_node.left) #Recure left
      elif value > current_node.value:
          current_node.right = self.__insert_element(value, current_node.right) #Recure right
      else:
          raise ValueError("Value already in the tree")
      self.__calc_height(current_node) #Calculates the high of the subroot node
      return self.__balance(current_node)
          
  def __calc_height(self, current_node):
      left = 0
      right = 0
      if current_node.left is None and current_node.right is None:
          current_node.height = 1
      else:
          if current_node.left is not None: #If the current node has a left or right child then it will collect their heights
              left += current_node.left.height
          if current_node.right is not None:
              right += current_node.right.height
      if left > right:
          current_node.height = 1 + left #lh + 1
      else:
          current_node.height = 1 + right #rh + 1
      return current_node.height
        
  def __find_m(self, current_node):
      while current_node.left is not None: #Finds the min value node 
          current_node = current_node.left
      return current_node
          
  def __remove_element(self, value, current_node):
      if current_node is None:
          raise ValueError("Value isn't in the tree or tree is empty")
      if value == current_node.value:
          if current_node.left is None and current_node.right is None: #Checks if the node has no children
              return None
          if current_node.left is None and current_node.right is not None: #Checks if the node has 1 child on the right
              return current_node.right
          if current_node.left is not None and current_node.right is None: #Checks if the node has 1 child on the left
              return current_node.left
          if current_node.left is not None and current_node.right is not None: #Checks if the node has 2 children
              m = self.__find_m(current_node.right)
              current_node.value = m.value #Replaces the node to be removed to the min value
              current_node.right = self.__remove_element(current_node.value, current_node.right) #Removes the duplicate
              self.__calc_height(current_node)
              return self.__balance(current_node)
      elif value < current_node.value:
          current_node.left = self.__remove_element(value, current_node.left)
      else:
          current_node.right = self.__remove_element(value, current_node.right)
      self.__calc_height(current_node)
      return self.__balance(current_node)

  def remove_element(self, value):
      self.__root = self.__remove_element(value, self.__root)
    
  def __in_order(self, current_node): 
      list_string = []
      if current_node is not None:
          list_string = self.__in_order(current_node.left) #Left child
          list_string.append(str(current_node.value)) #Appends the parent node
          list_string = list_string + self.__in_order(current_node.right) #Right child
      return list_string

  def in_order(self): #LPR
      if self.__root is None:
          return "[ ]" 
      else:
          string_rep = "[ "
          string_rep += ", ".join(self.__in_order(self.__root))
          string_rep += " ]"
          return string_rep
      
  def __to_list(self, current_node):
      list_rep = []
      if current_node is not None:
          list_rep = self.__to_list(current_node.left) #Left child
          list_rep.append(current_node.value) #Appends the parent node
          list_rep = list_rep + self.__to_list(current_node.right) #Right child
      return list_rep
      
  def to_list(self):
      return self.__to_list(self.__root)
          
  def __pre_order(self, current_node): 
      list_string = []
      if current_node is not None:
          list_string.append(str(current_node.value)) #Appends the parent node
          list_string += self.__pre_order(current_node.left) #Left child
          list_string += self.__pre_order(current_node.right) #Right child
      return list_string

  def pre_order(self): #PLR
      if self.__root is None:
          return "[ ]"
      else:
          string_rep = "[ "
          string_rep += ", ".join(self.__pre_order(self.__root))
          string_rep += " ]"
          return string_rep
      
  def __post_order(self, current_node): 
      list_string = []
      if current_node is not None:
          list_string += self.__post_order(current_node.left) #Left child
          list_string += self.__post_order(current_node.right) #Right child
          list_string.append(str(current_node.value)) #Append the parent node
      return list_string

  def post_order(self): #LRP
      if self.__root is None:
          return "[ ]"
      else:
          string_rep = "[ "
          string_rep += ", ".join(self.__post_order(self.__root))
          string_rep += " ]"
          return string_rep

  def get_height(self):
      if self.__root is None:
          return 0
      else:
          return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.