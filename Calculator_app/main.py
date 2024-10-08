from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

# App Settings
class CalApp(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Calculator App")
        self.resize(250, 300)

        # All objects/widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Times New Roman",32))


        self.grid = QGridLayout()

        # Button labels
        self.buttons = ["7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", ".", "=", "+"]
        
        row = 0
        col = 0
        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:  # Wrap to the next row after 4 columns
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")
        self.delete.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)

        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)

        master_layout.addLayout(button_row)

        self.setLayout(master_layout)


        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            
            except Exception as e:
                print("Error",e)

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

if __name__ in "__main__":
    app = QApplication([])
    main_window = CalApp()
    main_window.setStyleSheet("QWidget { background-color: #f0f0f8}")
    main_window.show()
    app.exec_()

# #import
# from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QHBoxLayout,QVBoxLayout,QGridLayout


# #App Settings
# app = QApplication([])
# main_window = QWidget()
# main_window.setWindowTitle("Calculator App")
# main_window.resize(250,300)

# #All objects/widgets
# text_box = QLineEdit()
# grid = QGridLayout()

# button = ["7","8","9","/",
#           "4","5","6","*",
#           "1","2","3","-",
#           "0",".","=","+"]

# clear = QPushButton("Clear")
# delete = QPushButton("<")

# #Design
# master_layout = QVBoxLayout()
# master_layout.addWidget(text_box)
# # master_layout.addLayout(grid)

# button_row = QHBoxLayout()
# button_row.addWidget(clear)
# button_row.addWidget(delete)

# master_layout.addWidget(button_row)

# main_window.setLayout(master_layout)



# #show/Run
# main_window.show()
# app.exec_()