# Data Structures Library

This repository contains a Python library implementing various fundamental data structures and algorithms.
It provides implementations for Linked Lists, Queues, Stacks, Sorting algorithms, and Searching algorithms.

---

## Table of Contents
- Overview
- Installation
- Usage
- Features
  - LinkedList
  - DoublyLinkedList
  - CircularLinkedList
  - DoublyCircularLinkedList
  - Stack
  - Queue
  - Sorting Algorithms
  - Searching Algorithms
- Contributing


Overview
This library provides efficient implementations of various data structures, including different types of linked lists, stack, queue, and
popular sorting and searching algorithms. It is designed to help developers understand and utilize data structures in Python projects.



## Installation
1. Clone the repository:
   
   git clone https://github.com/DarshChavan/data-structures-library.git

2. Navigate to the project directory:
   
   cd data-structures-library
  

3. Use the modules by importing them into your Python scripts.


### Usage
Import the required module in your Python project to use the desired data structure or algorithm.
For example:

```python
from DataStructures.linkedlist import LinkedList
from DataStructures.sort import bubble_sort

# Using LinkedList
ll = LinkedList()
ll.Insert_At_Head(10)
ll.Insert_At_Last(20)
ll.Display()

# Using bubble_sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

```

## Features

### LinkedList
A singly linked list with the following functionalities:
- Delete_At_Head(): Removes the first node.
- Delete_At_Last(): Removes the last node.
- Delete_At_Index(k): Removes the node at index `k`.
- Delete_Of_Value(val): Removes the first node with value `val`.
- Insert_At_Head(data): Inserts `data` at the beginning.
- Insert_At_Last(data): Inserts `data` at the end.
- Insert_At_Index(data, k): Inserts `data` at index `k`.
- Insert_Before_Value(data, val): Inserts `data` before the first occurrence of `val`.
- Display(): Prints all nodes.

### DoublyLinkedList
A doubly linked list with the following functionalities:
- Delete_At_Head(): Removes the first node.
- Delete_At_Last(): Removes the last node.
- Delete_At_Index(k): Removes the node at index `k`.
- Delete_A_Node(node): Deletes the specified node.
- Insert_At_Head(data): Inserts `data` at the beginning.
- Insert_At_Last(data): Inserts `data` at the end.
- Insert_At_Index(data, k): Inserts `data` at index `k`.
- Insert_Before_Last(data): Inserts `data` before the last node.
- Insert_Before_Node(data, node): Inserts `data` before a specified node.
- Display(): Prints all nodes.

### CircularLinkedList
A circular singly linked list with the following functionalities:
- Delete_At_Head(): Removes the first node.
- Delete_At_Last(): Removes the last node.
- Delete_At_Index(k): Removes the node at index `k`.
- Insert_At_Head(data): Inserts `data` at the beginning.
- Insert_At_Last(data): Inserts `data` at the end.
- Insert_At_Index(data, k): Inserts `data` at index `k`.
- Insert_Before_Value(data, val): Inserts `data` before the first occurrence of `val`.
- Display(): Prints all nodes.

### DoublyCircularLinkedList
A circular doubly linked list with the following functionalities:
- Delete_At_Head(): Removes the first node.
- Delete_At_Last(): Removes the last node.
- Delete_At_Index(k): Removes the node at index `k`.
- Delete_A_Node(node): Deletes the specified node.
- Insert_At_Head(data): Inserts `data` at the beginning.
- Insert_At_Last(data): Inserts `data` at the end.
- Insert_At_Index(data, k): Inserts `data` at index `k`.
- Insert_Before_End(data): Inserts `data` before the last node.
- Insert_Before_Node(data, node): Inserts `data` before a specified node.
- Display(): Prints all nodes.

### Stack
A stack implemented using a list, supporting the following operations:
- push(x): Adds `x` to the top of the stack.
- pop(): Removes and returns the top element.
- peek(): Returns the top element without removing it.
- get_size(): Returns the number of elements in the stack.

### Queue
A queue implemented using a list, supporting the following operations:
- enqueue(data): Adds `data` to the end of the queue.
- dequeue(): Removes and returns the first element.
- peek(): Returns the first element without removing it.
- get_size(): Returns the number of elements in the queue.

### Sorting Algorithms
- bubble_sort(arr): Sorts the array using the Bubble Sort algorithm.
- selection_sort(arr): Sorts the array using the Selection Sort algorithm.
- insertion_sort(arr): Sorts the array using the Insertion Sort algorithm.
- merge_sort(arr): Sorts the array using the Merge Sort algorithm.
- quick_sort(arr, low, high): Sorts the array using the Quick Sort algorithm.

### Searching Algorithms
- linear_search(arr, target): Searches for `target` using Linear Search. Returns the index if found, otherwise returns `-1`.
- binary_search(arr, target): Searches for `target` using Binary Search. Returns the index if found, otherwise returns `-1`. **Note:** The array must be sorted.



## Contributing
Contributions are welcome! If you would like to add new features, fix bugs, or improve documentation, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.




