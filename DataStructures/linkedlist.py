class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Delete_At_Head(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        return self.head

    def Delete_At_last(self):
        if self.head is None:
            print('Linked list is empty')
            return None
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next and temp.next.next:
                temp = temp.next
            temp.next = None
        return self.head

    def Delete_At_Index(self, k):
        if self.head is None:
            print('Linked list is empty')
            return None
        if k == 1:
            return self.Delete_At_Head()
        else:
            temp = self.head
            prev = None
            count = 1
            while temp:
                if count == k:
                    prev.next = temp.next
                    return self.head
                prev = temp
                temp = temp.next
                count += 1
            print('Invalid index')
        return self.head

    def Delete_Of_value(self, val):
        if self.head is None:
            print('Linked list is empty')
            return None
        if self.head.data == val:
            return self.Delete_At_Head()
        else:
            temp = self.head
            prev = None
            while temp:
                if temp.data == val:
                    prev.next = temp.next
                    return self.head
                prev = temp
                temp = temp.next
            print('Value not found in list')
        return self.head

    def Insert_At_Head(self, data):
        node = Node1(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head

    def Insert_At_Last(self, data):
        node = Node1(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        return self.head

    def Insert_At_Index(self, data, k):
        if self.head is None:
            if k == 1:
                self.head = Node1(data)
                return self.head
            else:
                print('Linked list is empty and invalid index')
                return None
        elif k == 1:
            return self.Insert_At_Head(data)
        else:
            node = Node1(data)
            temp = self.head
            count = 1
            while temp:
                count += 1
                if count == k:
                    node.next = temp.next
                    temp.next = node
                    return self.head
                temp = temp.next
            print('Invalid index')
        return self.head

    def Insert_Before_Value(self, data, val):
        if self.head is None:
            print('Linked list is empty')
            return None
        elif val == self.head.data:
            return self.Insert_At_Head(data)
        else:
            node = Node1(data)
            temp = self.head
            while temp.next:
                if temp.next.data == val:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next
        return self.head

    def Display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print(None)



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def Delete_At_Head(self):
        if self.head is None:
            print('Linked List is Empty')
            return None
        if self.head.next is None:
            self.head = None
            return None
        else:
            back = self.head
            self.head = self.head.next
            self.head.prev = None
            back.next = None
        return self.head

    def Delete_At_Last(self):
        if self.head is None:
            print('Linked List is Empty')
            return None
        if self.head.next is None:
            self.head = None
            return None
        else:
            temp = self.head
            while temp.next and temp.next.next:
                temp = temp.next
            front = temp.next
            temp.next = None
            front.prev = None
        return self.head

    def Delete_At_Index(self, k):
        if self.head is None:
            print('Linked list is empty')
            return None

        temp = self.head
        count = 1
        while temp:
            if count == k:
                break
            temp = temp.next
            count += 1

        if temp is None:
            print('Invalid index')
            return self.head

        back = temp.prev
        front = temp.next

        if back is None and front is None:
            self.head = None
        elif back is None:
            return self.Delete_At_Head()
        elif front is None:
            return self.Delete_At_Last()
        else:
            back.next = front
            front.prev = back

        temp.next = None
        temp.prev = None
        return self.head

    def Delete_A_Node(self, node):
        back = node.prev
        front = node.next

        if front is None:
            back.next = None
            node.prev = None
            return

        back.next = front
        front.prev = back

        node.next = None
        node.prev = None

    def Insert_At_Head(self, data):
        node = DoublyNode(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return self.head

    def Insert_At_Last(self, data):
        node = DoublyNode(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node.prev = temp
            temp.next = node
        return self.head

    def Insert_Before_Last(self, data):
        if self.head is None:
            return self.Insert_At_Head(data)
        else:
            node = DoublyNode(data)
            tail = self.head
            while tail.next:
                tail = tail.next

            back = tail.prev
            node.next = tail
            node.prev = back
            back.next = node
            tail.prev = node

            return self.head

    def Insert_At_Index(self, data, k):
        if k == 1:  # Insert at the head
            return self.Insert_At_Head(data)

        temp = self.head
        count = 1
        node = DoublyNode(data)

        # Traverse to the position k-1 or end of the list
        while temp and count < k - 1:
            temp = temp.next
            count += 1

        if not temp:  # If `k` is out of bounds
            print("Index out of bounds")
            return self.head

    # Insert in the middle or end
        next_node = temp.next
        node.prev = temp
        node.next = next_node

        if next_node:  # If not inserting at the tail
            next_node.prev = node

        temp.next = node
        return self.head


    def Insert_Before_Node(self,data,node):
        back = node.prev
        new_node = DoublyNode(data)
        new_node.next = node
        new_node.prev = back
        node.prev = new_node
        if back:
            back.next = new_node
        return self.head

    def Display(self):
        current = self.head
        while current:
            print(current.data ,end=' ')
            current = current.next
        print()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def Delete_At_Head(self):
        if self.head is None:
            print('Circular Linked List is empty')
            return None
        elif self.head.next == self.head:  # Single node in the list
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            # Remove the head and update the last node to point to the new head
            temp.next = self.head.next
            self.head = self.head.next
        return self.head

    def Delete_At_last(self):
        if self.head is None:
            print('Circular Linked List is empty')
            return None
        elif self.head.next == self.head:  # Only one node in the list
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            # Now, temp is the last node
            # Traverse back to the second last node and update the next pointer to head
            second_last = self.head
            while second_last.next != temp:
                second_last = second_last.next
            second_last.next = self.head
        return self.head

    def Delete_At_Index(self, k):
        if self.head is None:
            print('Circular Linked List is empty')
            return None
        elif k == 1:
            return self.Delete_At_Head()
        else:
            temp = self.head
            count = 1
            prev = None
            while count < k and temp.next != self.head:
                prev = temp
                temp = temp.next
                count += 1
            if count == k:
                prev.next = temp.next
                
                return self.head
            else:
                print('Invalid index')
        return self.head

    def Insert_At_Head(self, data):
        node = Node2(data)
        if self.head is None:
            self.head = node
            node.next = node  # Pointing to itself, only node in the list
        else:
            node.next = self.head
            temp = self.head
            # Traverse to the last node and update its next pointer to the new head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            self.head = node
        return self.head

    def Insert_At_Last(self, data):
        node = Node2(data)
        if self.head is None:
            self.head = node
            node.next = node  # Pointing to itself
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
        return self.head

    def Insert_At_Index(self, data, k):
        if self.head is None:
            if k == 1:
                self.head = Node2(data)
                self.head.next = self.head  # Single node, points to itself
                return self.head
            else:
                print('Circular Linked List is empty and invalid index')
                return None
        elif k == 1:
            return self.Insert_At_Head(data)
        else:
            node = Node2(data)
            temp = self.head
            count = 1
            prev = None
            while count < k and temp.next != self.head:
                prev = temp
                temp = temp.next
                count += 1
            if count == k:
                prev.next = node
                node.next = temp
                return self.head
            else:
                print('Invalid index')
        return self.head

    def Insert_Before_Value(self, data, val):
        if self.head is None:
            print('Circular Linked List is empty')
            return None
        elif val == self.head.data:
            return self.Insert_At_Head(data)
        else:
            node = Node2(data)
            temp = self.head
            while temp.next != self.head:
                if temp.next.data == val:
                    node.next = temp.next
                    temp.next = node
                    return self.head
                temp = temp.next
            print('Value not found in list')
        return self.head

    def Display(self):
        if self.head is None:
            print('Circular Linked List is empty')
            return
        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()
    

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DoublyCircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def Delete_At_Head(self):
        if self.head is None:
            print('Circular Linked List is Empty')
            return None
        if self.head.next == self.head:
            self.head = None
            return None
        else:
            last = self.head.prev
            self.head = self.head.next
            self.head.prev = last
            last.next = self.head
        return self.head

    def Delete_At_Last(self):
        if self.head is None:
            print('Circular Linked List is Empty')
            return None
        if self.head.next == self.head:
            self.head = None
            return None
        else:
            last = self.head.prev
            last.prev.next = self.head
            self.head.prev = last.prev
        return self.head

    def Delete_At_Index(self, k):
        if self.head is None:
            print('Circular Linked List is empty')
            return None
        temp = self.head
        count = 1
        while temp:
            if count == k:
                break
            temp = temp.next
            count += 1

        if temp is self.head and temp.next == self.head:
            self.head = None
        elif temp == self.head:
            return self.Delete_At_Head()
        elif temp.next is None:
            return self.Delete_At_Last()
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        return self.head

    def Delete_A_Node(self, node):
        if self.head is None:
            return
        back = node.prev
        front = node.next

        if front == self.head:
            self.head = front
        back.next = front
        front.prev = back
        node.next = None
        node.prev = None

    def Insert_At_Head(self, data):
        node = DoublyCircularNode(data)
        if self.head is None:
            self.head = node
            node.next = node  # Circular link to itself
            node.prev = node  # Circular link to itself
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
            self.head = node  # Update head
        return self.head

    def Insert_At_Last(self, data):
        node = DoublyCircularNode(data)
        if self.head is None:
            self.head = node
            node.next = node  # Circular link to itself
            node.prev = node  # Circular link to itself
        else:
            last = self.head.prev
            last.next = node
            node.prev = last
            node.next = self.head
            self.head.prev = node
        return self.head

    def Insert_Before_End(self, data):
        if self.head is None:
            return self.Insert_At_Head(data)
        else:
            node = DoublyCircularNode(data)
            tail = self.head.prev
            node.prev = tail.prev
            node.next = tail
            tail.prev.next = node
            tail.prev = node
        return self.head

    def Insert_At_Index(self, data, k):
        node = DoublyCircularNode(data)

        # Case 1: Empty list
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
            return self.head

        # Case 2: Insert at head (k == 1)
        if k == 1:
            tail = self.head.prev
            node.next = self.head
            node.prev = tail
            tail.next = node
            self.head.prev = node
            self.head = node
            return self.head

        # Case 3: Insert at position k or end
        temp = self.head
        count = 1

        while count < k - 1 and temp.next != self.head:  # Traverse until k-1 or full circle
            temp = temp.next
            count += 1

        # Insert after `temp`
        next_node = temp.next
        node.next = next_node
        node.prev = temp
        temp.next = node
        next_node.prev = node

        return self.head


    def Insert_Before_Node(self, data, node):
        back = node.prev
        new_node = DoublyCircularNode(data)
        new_node.next = node
        new_node.prev = back
        node.prev = new_node
        if back:
            back.next = new_node
        return self.head

    def Display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:  # Stop when we circle back to head
                break
        print()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////       
        
	

