# import random
import threading as thr
import time


class Store():
    def __init__(self, name=''):
        self._name = name
        self.in_books = {}
        self.out_books = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    def add_books(self, *books, store_source=None):

        b_list = self.get_book_sources_lists(store_source)

        for book in books:
            if not book in b_list:
                b_list.append(book)
                if store_source:
                    store_source.minus_books(book, store_need=self)

        self.in_books[store_source] = b_list

    def minus_books(self, *books, store_need):
        for book in books:
            books_lists = self.in_books.values()
            for b_list in books_lists:
                if book in b_list:
                    b_list.remove(book)
                    store_need.add_books(book, store_source=self)

    def get_book_lists(self):
        b_list = []
        for b_dics in self.in_books:
            b_list.extend(self.in_books.get(b_dics))

        return b_list

    def get_book_sources_lists(self, source):
        if self.in_books:
            try:
                return self.in_books[source]
            except:
                return []
        else:
            return []

    def find_book_inside(self, book_name):
        books_lists = self.in_books.values()
        for b_list in books_lists:
            for book in b_list:
                if book_name == book.name:
                    return book
        else:
            return None


class Library(Store):
    def __init__(self):
        super().__init__()


class ReadHall(Store):
    def __init__(self, library):
        super().__init__()
        self.library = library

    def give_books(self, person):

        books_need = person.books_need

        books_list = []

        for i in books_need:
            finded_book = self.library.find_book_inside(i)
            if finded_book:
                books_list.append(finded_book)
            else:
                print(f'* book {i} - not founded!')

        for _book in books_list:
            if _book.is_inside_used():
                self.library.minus_books(_book, store_need=self)
                self.minus_books(_book, store_need=person)
            else:
                self.library.minus_books(_book, store_need=person)


class Person(Store):
    def __init__(self):
        super().__init__()
        self.books_need = []

    def add_books_need(self, *b_names):
        for n in b_names:
            self.books_need.append(n)

    def read(self):
        if self.in_books:
            for b_dict in self.in_books:
                for book in self.in_books[b_dict]:
                    book.start()


class Status():
    def __init__(self, time_limit, inside_used=False):
        self._time_limit = time_limit
        self._inside_used = inside_used

    @property
    def time_limit(self):
        return self._time_limit

    @time_limit.setter
    def time_limit(self, v):
        self._time_limit = v

    @property
    def inside_used(self):
        return self._inside_used

    @inside_used.setter
    def inside_used(self, v):
        self._inside_used = v


class Book(thr.Thread):
    def __init__(self, name, status):
        super().__init__()
        self._name = name
        self._status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, v):
        self._status = v

    def is_inside_used(self):
        return self.status.inside_used

    def get_time_limit(self):
        return self.status.time_limit

    def run(self):
        timer = self.get_time_limit()
        while timer:
            time.sleep(timer)
            if self.is_inside_used():
                print(f'{self.name}  reading -  in hall\n')
            else:
                print(f'{self.name}  reading  - in home\n')
            timer -= 1

        print(f'{self.name} - has stopped')

    def stop(self):
        self._is_running = False


status_inside = Status(1, True)
status_outside = Status(5, False)

bn1 = Book('bn1', status_inside)
bn2 = Book('bn2', status_outside)
bn3 = Book('bn3', status_inside)
bn4 = Book('bn4', status_outside)

print(bn1)

libr = Library()
libr.name = 'Tech_library'

print(libr.name)
libr.add_books(bn1, bn2, bn3, bn4, store_source=None)

print(libr.find_book_inside('bn3'))

read_hall = ReadHall(libr)
read_hall.name = '-=Read hall=-'

stud = Person()
stud.name = 'Vasya'
stud.add_books_need('bn1', 'bn2')
read_hall.give_books(stud)

stud2 = Person()
stud2.name = 'Petya'
stud2.add_books_need('bn3', 'bn4')
read_hall.give_books(stud2)

stud.read()
stud2.read()


