class Node:
    def __init__(self,children=None):
         if children:
              self.children = children
         else:
              self.children = []