"""
Name: Bram Kineman
CC4 - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""


class Books:

    def __init__(self):
        """
        Instantiates a last in first out stack of books.
        """
        self.book_list = []
        self.minimum = None
        self.minimum_list = []

    def insert(self, book: int):
        """
        Insert a book as an integer representing page numbers on top of the stack.
        :param book: int value representing page numbers.
        :return: None
        """
        if self.is_empty():
            self.minimum_list.append(book)
            self.minimum = book
        elif book <= self.minimum:
            self.minimum = book
            self.minimum_list.append(book)

        self.book_list.append(book)

    def remove(self):
        """
        Remove a book from the top of the stack.
        :return: int of the book remove, None if stack is empty.
        """
        if self.is_empty():
            return None
        top = self.book_list.pop()
        if top == self.minimum and not self.is_empty():
            self.minimum_list.pop()
            self.minimum = self.minimum_list[-1]
        return top

    def shortest_book(self):
        """
        Retrieve the length of the shortest book in the stack.
        :return: int representation of the shortest book, None if stack is empty.
        """
        if self.is_empty():
            return None
        return self.minimum_list[-1]

    def is_empty(self):
        """
        Find if there is a stack of books or not.
        :return: True if there are no books, false otherwise.
        """
        return len(self.book_list) == 0
