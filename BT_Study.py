import collections

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert (self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def delete(r,node):
    def minvalue(node):
        while current and current.left is not None:
            current = current.left
            return current
        
    if r is None:
        return
    else:
        if node < r.data:
            if r.left is None:
                print("This number is not in the Tree")
            else:
                r.left = delete(r.left, node)
        elif node > r.data:
            if r.right is None:
                print("This number is not in the Tree")
            else:
                r.right = delete(r.right, node)
        else: 
            if r.left is None:
                temp = r.right
                r = None
                return temp
            elif r.right is None:
                temp = r.left
                r = None
                return temp
            temp = minvalue(r.right)

            r.data = temp.data
            r.right = delete(r.right, temp.data)
    return r
                
def inorder(r):
    if r is None:
        return
    else:
        inorder(r.left)
        print(r.data, end=" ")
        inorder(r.right)

def preorder(r):
    if r is None:
        return
    else:
        print(r.data, end= " ")
        preorder(r.left)
        preorder(r.right)

def postorder(r):
    if r is None:
        return
    else:
        postorder(r.left)
        postorder(r.right)
        print(r.data, end=" ")

def treelist(r):
    if r is None:
        return 
    else:
        dict[r.data] = []
        treelist(r.left)
        if r.left:
            dict[r.data].append(r.left.data)
        if r.right:
            dict[r.data].append(r.right.data)
        treelist(r.right)
    return dict

def bfs(al):
    queue = collections.deque([root.data])
    visited = []
    while queue: 
        node = queue.popleft()
        visited.append(node)
        [queue.append(ele) for ele in al[node]]
    print(f"Breadth First:\n{visited}")

def pos(r):
    if r is None:
        return  
    stack = []
    stack.append(r)
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print(f"Pre Order Loop Search:\n{visited}")

def nodesearh(r, node):
    current = r
    while current.data != node:
        if current.right and current.left and node is not None:
            if node < current.data:
                 current = current.left
            if node > current.data:
                current = current.right
            if current.data == node:
                print("It's in the Tree")     
        else:        
            print("It's not in the Tree")
            return       

def order_choosen(order_print):
    global dict 
    dict = {}
    adjacency_list = treelist(root)
    if order_print == 1:
        print("In Order: ")
        inorder(root)
    elif order_print == 2:
        print("Pre Order: ")
        preorder(root)
    elif order_print == 3:
        print("Post Order: ")
        postorder(root)
    elif order_print == 4:
        bfs(adjacency_list)
    elif order_print == 5:
        pos(root)
    elif order_print == 6:
        try:
            node = int(input("Insert Number: "))
        except ValueError:
            print("Insert a root or a number")
            order_choosen(6)
            return
        nodesearh(root,node)
    elif order_print == 7:
        try:
            node = int(input("Insert Number: "))
        except ValueError:
            print("Insert a root or a number")
            order_choosen(7)
            return
        delete(root,node)
        inorder(root)

    else:
        print("Invalid Number")

if __name__ == '__main__':
    root = Node(50)
    root.insert(20)
    root.insert(60)
    root.insert(10)
    root.insert(30)
    root.insert(70)
    root.insert(55)

def main():
    orders = ["In Order","Pre Order","Post Order","Breath First","Pre Order Loop","Node Search", "Delete Node"]
    for idx, order in enumerate(orders):
        print("{}) {}".format(idx + 1, order))
    order_print = int(input("Choose a search order above: "))
    order_choosen(order_print)

main()