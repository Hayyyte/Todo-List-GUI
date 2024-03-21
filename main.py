import sys
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, QMessageBox, QLabel, QMenuBar
from PyQt5.QtGui import QFont, QIcon, QCursor
import random

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(400, 600)
        self.setFont(QFont("Inter", 12))

        self.menu_bar = QMenuBar()
        self.menu_bar.setStyleSheet("QMenuBar::item:hover { color: black; background-color: #f0f0f0; }")
        self.menu_bar.setFont(QFont("Inter", 10))
        self.help_menu = self.menu_bar.addMenu("Help")
        self.about_action = self.help_menu.addAction("About")
        self.about_action.triggered.connect(self.show_about)
        self.credits_action = self.help_menu.addAction("Credits")
        self.credits_action.triggered.connect(self.show_credits)

        self.title_label = QLabel("To-Do List")
        self.title_label.setFont(QFont("Inter", 24))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("text-decoration: underline;")

        self.quotes_label = QLabel()
        self.quotes_label.setFont(QFont("Inter", 12))
        self.quotes_label.setStyleSheet("padding: 20px; background-color: #ADD8E6; border-radius: 10px;")
        self.quotes_label.setAlignment(Qt.AlignCenter)
        self.quotes_label.setWordWrap(True)
        self.set_random_quote()

        self.task_list = QListWidget()
        self.load_tasks()
        
        self.text_box = QLineEdit()
        self.text_box.returnPressed.connect(self.add_task)
        self.text_box.setStyleSheet("padding: 10px;")
        self.text_box.setFont(QFont("Inter", 16))
        self.text_box.setPlaceholderText("Enter your task here...")

        add_task_button = QPushButton("Add Task")
        add_task_button.clicked.connect(self.add_task)
        add_task_button.setCursor(QCursor(Qt.PointingHandCursor))

        delete_task_button = QPushButton("Delete Task")
        delete_task_button.clicked.connect(self.delete_task)
        delete_task_button.setCursor(QCursor(Qt.PointingHandCursor))

        change_task_button = QPushButton("Change Task")
        change_task_button.clicked.connect(self.change_task)
        change_task_button.setCursor(QCursor(Qt.PointingHandCursor))

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(add_task_button)
        buttons_layout.addWidget(delete_task_button)
        buttons_layout.addWidget(change_task_button)

        main_layout = QVBoxLayout()
        main_layout.setMenuBar(self.menu_bar)
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.quotes_label)
        main_layout.addWidget(self.text_box)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(buttons_layout)
        main_layout.setContentsMargins(25, 20, 25, 20)

        self.setLayout(main_layout)

    def show_about(self):
        QMessageBox.information(self, "About", """
            To enter a task,
            - type your task.
            - click "Add Task"
            
            To delete a task,
            - click the task
            - click "Delete Task"
            
            To change a task,
            - enter your task
            - click on a task you want to change
            - click "Change Task"
        """)
    
    def show_credits(self):
        QMessageBox.information(self, "Credits", "Icon made by juicy_fish from www.flaticon.com")

    def add_task(self):
        new_task = self.text_box.text()
        if new_task:
            self.task_list.addItem(new_task)
            self.text_box.clear()
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))
            self.save_tasks()

    def change_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            new_task_text = self.text_box.text()
            if new_task_text:
                selected_item.setText(new_task_text)
                self.text_box.clear()
                self.save_tasks()
            else:
                QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for index in range(self.task_list.count()):
                task = self.task_list.item(index).text()
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = [line.strip() for line in file.readlines()]
                self.task_list.addItems(tasks)
        except FileNotFoundError:
            pass

    def set_random_quote(self):
        zen_quotes = [
            "The quieter you become, the more you are able to hear. - Zen Proverb",
            "When you realize nothing is lacking, the whole world belongs to you. - Lao Tzu",
            "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
            "The journey of a thousand miles begins with one step. - Lao Tzu",
            "Be content with what you have; rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you. - Lao Tzu",
            "The truth is not always beautiful, nor beautiful words the truth. - Lao Tzu",
            "Life is a series of natural and spontaneous changes. Don't resist them; that only creates sorrow. Let reality be reality. Let things flow naturally forward in whatever way they like. - Lao Tzu",
            "Knowing others is wisdom, knowing yourself is Enlightenment. - Lao Tzu",
            "To the mind that is still, the whole universe surrenders. - Lao Tzu",
            "A journey of a thousand miles begins with a single step. - Lao Tzu",
            "To a mind that is still, the whole universe surrenders. - Chuang Tzu",
            "One does not accumulate but eliminate. It is not daily increase but daily decrease. The height of cultivation always runs to simplicity. - Bruce Lee",
            "Simplicity is the ultimate sophistication. - Leonardo da Vinci",
            "Nature does not hurry, yet everything is accomplished. - Lao Tzu",
            "Be master of mind rather than mastered by mind. - Zen Proverb",
            "The obstacle is the path. - Zen Proverb",
            "The best fighter is never angry. - Lao Tzu",
            "When you realize nothing is lacking, the whole world belongs to you. - Lao Tzu",
            "Time is a created thing. To say 'I don't have time,' is like saying, 'I don't want to.' - Lao Tzu",
            "He who conquers others is strong; He who conquers himself is mighty. - Lao Tzu",
            "Act without expectation. - Lao Tzu",
            "The Tao that can be told is not the eternal Tao; The name that can be named is not the eternal name. - Lao Tzu",
            "Knowing others is intelligence; knowing yourself is true wisdom. Mastering others is strength; mastering yourself is true power. - Lao Tzu",
            "Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step. - Lao Tzu",
            "Those who know do not speak. Those who speak do not know. - Lao Tzu",
            "Health is the greatest possession. Contentment is the greatest treasure. Confidence is the greatest friend. Non-being is the greatest joy. - Lao Tzu",
            "The snow falls, each flake in its appropriate place. - Zen Proverb",
            "The flame that burns twice as bright burns half as long. - Lao Tzu",
            "The more you know, the less you understand. - Lao Tzu",
            "Nature does not hurry, yet everything is accomplished. - Lao Tzu",
            "The wise man is one who knows what he does not know. - Lao Tzu",
            "When you are content to be simply yourself and don't compare or compete, everyone will respect you. - Lao Tzu",
            "A good traveler has no fixed plans and is not intent on arriving. - Lao Tzu",
            "The only journey is the one within. - Rainer Maria Rilke",
            "The only Zen you find on the tops of mountains is the Zen you bring up there. - Robert M. Pirsig",
            "The quieter you become, the more you can hear. - Ram Dass",
            "The past has no power over the present moment. - Eckhart Tolle",
            "One moment can change a day, one day can change a life, and one life can change the world. - Buddha",
            "The biggest communication problem is we do not listen to understand. We listen to reply. - Zen Proverb",
            "To understand everything is to forgive everything. - Buddha",
            "Don't believe everything you think. Thoughts are just that – thoughts. - Allan Lokos",
            "If you want to fly, give up everything that weighs you down. - Buddha",
            "You only lose what you cling to. - Buddha",
            "Let go or be dragged. - Zen Proverb",
            "No mud, no lotus. - Thich Nhat Hanh",
            "The mind is everything. What you think you become. - Buddha",
            "In the end, only three things matter: how much you loved, how gently you lived, and how gracefully you let go of things not meant for you. - Buddha",
            "The less you respond to negative people, the more peaceful your life will become. - Buddha",
            "Be kind whenever possible. It is always possible. - Dalai Lama",
            "Peace comes from within. Do not seek it without. - Buddha"
        ]
        self.quotes_label.setText('"' + random.choice(zen_quotes) + '"')

if __name__ == "__main__":
    app = QApplication([])
    todo_app = ToDoApp()
    todo_app.show()
    app.exec()
