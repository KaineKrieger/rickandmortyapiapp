# importing the requests function to do the getting api part
import requests
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Rick And Morty Api App")

        #setting up layouts
        main_layout = QHBoxLayout()

        title_box = QHBoxLayout()
        top_box = QVBoxLayout()
        bot_box = QVBoxLayout()

        #title for app
        title_label = QLabel("Rick And Morty Character Generator")
        
        font1 = title_label.font()
        font1.setPointSize(20)
        title_label.setFont(font1)

        #aligning the title
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)

        title_box.addWidget(title_label)
        btn = QPushButton("help")
        





        main_layout.addLayout(title_box)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# base is the website for the api
# base = "https://rickandmortyapi.com/api/"

# there are more endpoints i could make but for now its just character, check the website docs when you come back to make an app out of this
# endpoint = "character"

# THIS DOESNT mean the url by itself its making the new url from the base while adding aditional endpoints, check docs for formatting
# url = base + endpoint

# calling the api for data
# response = requests.get(url)

# character_selection = str(input("give me a number in the range 1-826: "))

# response = requests.get(url + "/" + character_selection)

# basic boolean to make sure it works.
# if response.ok:
    
    # print(response.text)

# else:
    # print(response.status_code)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


