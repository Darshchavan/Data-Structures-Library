"""
DataStructures Package

This package provides implementations of various data structures and algorithms:
- Linked Lists (Singly, Doubly, Circular, and Doubly Circular)
- Stack
- Queue
- Sorting Algorithms
- Searching Algorithms
"""

# Importing core classes and functions to simplify access
from .linkedlist import LinkedList, DoublyLinkedList, CircularLinkedList, DoublyCircularLinkedList
from .stack import Stack
from .myqueue import MyQueue
from .sort import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from .search import linear_search, binary_search


