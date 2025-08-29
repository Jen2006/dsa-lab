class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} as head node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end of the list.")

    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Value {key} not found in the list.")
            return

        if prev is None:
            # Deleting head
            self.head = current.next
        else:
            prev.next = current.next

        print(f"Deleted node with value {key}.")

    def update(self, old_value, new_value):
        current = self.head
        while current and current.data != old_value:
            current = current.next

        if not current:
            print(f"Value {old_value} not found in the list.")
            return

        current.data = new_value
        print(f"Updated node value from {old_value} to {new_value}.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    sll = SinglyLinkedList()

    while True:
        print("\nOptions: insert | delete | update | display | exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "insert":
            val = input("Enter value to insert: ")
            sll.insert(val)

        elif choice == "delete":
            val = input("Enter value to delete: ")
            sll.delete(val)

        elif choice == "update":
            old_val = input("Enter value to update: ")
            new_val = input("Enter new value: ")
            sll.update(old_val, new_val)

        elif choice == "display":
            sll.display()

        elif choice == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
