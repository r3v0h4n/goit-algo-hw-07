from avl import AVLNode, insert, delete_node, max_node, min_node, sum_nodes

def main():
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)

    print(f"Max: {max_node(root)}")
    print(f"Min: {min_node(root)}")
    print(f"Sum: {sum_nodes(root)}")
    

if __name__ == "__main__":
    main()