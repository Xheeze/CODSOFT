import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap

class PhonebookApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Phonebook 2k23')
        icon = QIcon(QPixmap('xheeze.png'))  # Icon speciale
        self.setWindowIcon(icon)

        # Create widgets
        self.name_label = QLabel('Name:')
        self.name_entry = QLineEdit()
        self.phone_label = QLabel('Phone:')
        self.phone_entry = QLineEdit()

        self.add_button = QPushButton('Add Contact')
        self.add_button.clicked.connect(self.add_contact)

        self.search_label = QLabel('Search:')
        self.search_entry = QLineEdit()

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_contact)

        self.name_edit_label = QLabel('Name to Edit:')
        self.name_edit_entry = QLineEdit()
        self.new_phone_label = QLabel('New Phone:')
        self.new_phone_entry = QLineEdit()

        self.edit_button = QPushButton('Edit Contact')
        self.edit_button.clicked.connect(self.edit_contact)

        self.name_delete_label = QLabel('Name to Delete:')
        self.name_delete_entry = QLineEdit()

        self.delete_button = QPushButton('Delete Contact')
        self.delete_button.clicked.connect(self.delete_contact)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)

        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self.close)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)
        layout.addWidget(self.add_button)

        layout.addWidget(self.search_label)
        layout.addWidget(self.search_entry)
        layout.addWidget(self.search_button)

        layout.addWidget(self.name_edit_label)
        layout.addWidget(self.name_edit_entry)
        layout.addWidget(self.new_phone_label)
        layout.addWidget(self.new_phone_entry)
        layout.addWidget(self.edit_button)

        layout.addWidget(self.name_delete_label)
        layout.addWidget(self.name_delete_entry)
        layout.addWidget(self.delete_button)

        layout.addWidget(self.result_display)

        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()

        with open('Contacts.txt', 'a') as file:
            file.writelines(('\n', f'{name} : {phone}', '\n'))

        self.update_display()

    def search_contact(self):
        search_term = self.search_entry.text()
        result = ""

        with open('Contacts.txt', 'r') as file:
            for line in file:
                if search_term in line:
                    result += line

        self.result_display.setPlainText(result)

    def edit_contact(self):
        name_to_edit = self.name_edit_entry.text()
        new_phone = self.new_phone_entry.text()

        with open('Contacts.txt', 'r') as file:
            lines = file.readlines()

        with open('Contacts.txt', 'w') as file:
            for line in lines:
                if name_to_edit in line:
                    line = f'{name_to_edit} : {new_phone}\n'
                file.write(line)

        self.update_display()

    def delete_contact(self):
        name_to_delete = self.name_delete_entry.text()

        with open('Contacts.txt', 'r') as file:
            lines = file.readlines()

        with open('Contacts.txt', 'w') as file:
            for line in lines:
                if name_to_delete not in line:
                    file.write(line)

        self.update_display()

    def update_display(self):
        with open("Contacts.txt", "r") as file:
            content = file.read()
            self.result_display.setPlainText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    phonebook_app = PhonebookApp()
    phonebook_app.show()
    sys.exit(app.exec_())