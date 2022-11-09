class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
     
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                   self.left = Node(data)
                else:
                    self.left.insert(data)

            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

root = Node (10)
root.insert(9)
root.insert(11)
root.insert(5)
root.insert(8)

root.print_tree()



    