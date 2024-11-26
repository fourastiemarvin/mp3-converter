import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QListWidget, QPushButton, QLabel
)
class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()

      # Set main window
      self.setWindowTitle("MP3 Converter")
      # self.setGeometry(100, 100, 400, 300)
      # Create central widget
      central_widget = QWidget(self)
      self.setCentralWidget(central_widget)
      # Create main layout
      main_layout = QVBoxLayout()

      # Add field and button for user input
      self.link_input = QLineEdit()
      self.link_input.setPlaceholderText("Ajouter un lien Youtube")
      main_layout.addWidget(self.link_input)
      add_button = QPushButton("Ajouter le lien")
      add_button.clicked.connect(self.add_link_to_list)
      main_layout.addWidget(add_button)

      # Add list for the links
      self.link_list = QListWidget()
      main_layout.addWidget(self.link_list)
      button = QPushButton("Convertir en MP3")
      button.clicked.connect(self.convert)
      main_layout.addWidget(button)

      # Add label for message display
      self.message_label = QLabel("")
      main_layout.addWidget(self.message_label)

      # Apply the main layout to the central widget
      central_widget.setLayout(main_layout)

   def convert(self):
      pass

   def add_link_to_list(self):
      link = self.link_input.text().strip()

      if link:
         self.link_list.addItem(link)
         # self.message_label.setText(f"{link} a été ajouté à la liste.")
         self.link_input.clear()
      # else:
      #       self.message_label.setText("Le champ est vide, entrez un nom.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
