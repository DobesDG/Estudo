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
    queue = collections.deque([50])
    visited = []
    while queue: 
        node = queue.popleft()
        visited.append(node)
        [queue.append(ele) for ele in al[node]]
    print(f"Breadth First Search:\n{visited}")

def order_choosen(order_print):
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
        global dict 
        dict = {}
        adjacency_list = treelist(root)
        bfs(adjacency_list)
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
    orders = ["In Order", "Pre Order","Post Order","Breath First Search"]
    for idx, order in enumerate(orders):
        print("{}) {}".format(idx + 1, order))
    order_print = int(input("Choose Order: "))
    order_choosen(order_print)

main()