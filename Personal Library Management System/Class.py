import csv

class Book :
    def __init__(self,title,author,genre,publication_year) :
         self.title=title
         self.author=author
         self.genre=genre
         self.publication_year=publication_year
    def __str__(self):
        return f"Book-title : {self.title} , Author : {self.author} , genre : {self.genre} , publication_Year : {self.publication_year}"


        
class Library :
     def __init__(self) :
          self.Books = []
          self.Errors = []

     def AddBook(self,book):
          self.Books.append(book)

     def RemoveBook(self,index):
          del self.Books[index]

     def SearchBook(self,title):
        for book in self.Books :
           if book.title.lower() == title.lower() or book.author.lower() == title.lower():
                 return book
        raise ValueError("Book not found.")

     def __len__(self):
        return len(self.Books)

     def save_library(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for book in self.Books:
                writer.writerow([book.title, book.author, book.genre, book.publication_year])

     def load_library(self, filename):
        self.Books = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.AddBook(Book(*row))
    
