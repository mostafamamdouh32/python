# importing libraries
from PyQt5.QtWidgets import *
import sys
from Class import Library, Book


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Library")
        # setting geometry
        self.setGeometry(100, 100, 900, 400)
        # calling method
        self.UiComponents()
        self.validationMSG()
        # showing all the widgets
        self.show()
        self.lib = Library()
        self.lib.load_library("library.csv")

    # method for widgets
    def UiComponents(self):
        label1 = QLabel("title : ", self)
        label1.setGeometry(10, 30, 130, 30)

        self.text1 = QLineEdit(self)
        self.text1.setGeometry(80, 30, 180, 30)

        label2 = QLabel("author : ", self)
        label2.setGeometry(10, 70, 130, 30)

        self.text2 = QLineEdit(self)
        self.text2.setGeometry(80, 70, 180, 30)

        label3 = QLabel("genre : ", self)
        label3.setGeometry(10, 110, 130, 30)

        self.text3 = QLineEdit(self)
        self.text3.setGeometry(80, 110, 180, 30)

        label4 = QLabel("publication_year : ", self)
        label4.setGeometry(10, 150, 130, 30)

        self.text4 = QLineEdit(self)
        self.text4.setGeometry(150, 150, 110, 30)

        label5 = QLabel("Index : ", self)
        label5.setGeometry(10, 190, 130, 30)
        self.text5 = QLineEdit(self)
        self.text5.setGeometry(150, 190, 110, 30)

        ##list
        self.listwidget = QTextBrowser(self)
        self.listwidget.setGeometry(320, 20, 550, 350)
        ##buttons
        button1 = QPushButton("Add Books", self)
        button1.setGeometry(30, 230, 130, 30)
        button1.clicked.connect(self.Addbooks)

        button2 = QPushButton("Remove Books", self)
        button2.setGeometry(170, 230, 130, 30)
        button2.clicked.connect(self.Removebooks)

        button3 = QPushButton("Search Books", self)
        button3.setGeometry(30, 280, 130, 30)
        button3.clicked.connect(self.SearchBook)

        button4 = QPushButton("Display Books", self)
        button4.setGeometry(170, 280, 130, 30)
        button4.clicked.connect(self.Displaybooks)

        button5 = QPushButton("Save library", self)
        button5.setGeometry(100, 320, 130, 30)
        button5.clicked.connect(self.SaveLibrary)

    def validationMSG(self):
        # Search Errors
        self.SearchErros = QLabel("please write a book title or author")
        self.SearchErros.setGeometry(100, 0, 300, 30)
        self.SearchErros.setStyleSheet("border: 1px solid black;")

        self.SearchErros2 = QLabel("Book not found ")
        self.SearchErros2.setGeometry(100, 0, 300, 30)
        self.SearchErros2.setStyleSheet("border: 1px solid black;")
        # End Search Errors

        # Remove Errors
        self.RemoveErros = QLabel("please write a Index of book")
        self.RemoveErros.setGeometry(100, 0, 300, 30)
        self.RemoveErros.setStyleSheet("border: 1px solid black;")

        self.RemoveErros2 = QLabel("Invalid task index")
        self.RemoveErros2.setGeometry(100, 0, 300, 30)
        self.RemoveErros2.setStyleSheet("border: 1px solid black;")
        # Remove ended

        #Addbooks ERRORS
        self.successfully = QLabel("successfully ")
        self.successfully.setGeometry(100, 0, 300, 30)
        self.successfully.setStyleSheet("border: 1px solid black;")

        self.Error = QLabel("Error please Enter all data of book ")
        self.Error.setGeometry(100, 0, 300, 30)
        self.Error.setStyleSheet("border: 1px solid black;")
        # Addbooks ERRORS ENDERD
    # action method
    def Addbooks(self):
        t = self.text1.text()
        a = self.text2.text()
        g = self.text3.text()
        p = self.text4.text()
        if t == "" and  a == "" and g == "" and p == "":
            self.Error.show()
        else :
           self.lib.AddBook(Book(t, a, g, p))
           self.text1.clear()
           self.text2.clear()
           self.text3.clear()
           self.text4.clear()
           self.successfully.show()

    def Removebooks(self):
        if self.text5.text() == "":
            self.RemoveErros.show()
        else:
            index = int(self.text5.text()) - 1
            if 0 <= index < len(self.lib):
               self.lib.RemoveBook(index)
               self.successfully.show()
            else:
               self.RemoveErros2.show()


    def SearchBook(self):
        x = self.text1.text()
        y = self.text2.text()
        Erros = []
        if x == "" and y == "":
           self.SearchErros.show()
           Erros.append("Found")
        else:
           for b in self.lib.Books:
             if b.title.lower() == x.lower() or b.author.lower() == y.lower():
                Erros.append("Found")
                self.listwidget.clear()
                self.listwidget.append(str(b))
             else:
                Erros.append("Not found")
        if "Found" not in Erros:
            self.SearchErros2.show()


    def Displaybooks(self):
      self.listwidget.setText("")
      for i, book in enumerate(self.lib.Books):
        self.listwidget.append(f"{i + 1}. {str(book)}")


    def SaveLibrary(self):
      self.lib.save_library("library.csv")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
