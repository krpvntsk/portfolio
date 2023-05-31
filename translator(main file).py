import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from learner import Ui_MainWindow as LearnerUi_MainWindow
from deletemode import Ui_Deletemode
from study import Ui_studymode
import random


# in this part, we create the base of the GUI,
# initialize the graphics platform, create the main window,
# and also show this window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = LearnerUi_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# this function accepts words written in text fields, puts them in variables,
# opens a file and writes our combination there in a special way, after which it clears these fields
def new_word_write():
    word_for_translation = ui.plainTextEdit.toPlainText()
    translation = ui.plainTextEdit_2.toPlainText()

    with open('words.txt', 'r+', encoding='utf-8') as file:
        file.seek(0)
        file.readlines()
        file.write(f"{word_for_translation} - {translation} - 1\n")
        ui.plainTextEdit.setPlainText('')
        ui.plainTextEdit_2.setPlainText('')


# connect the function to the button
ui.pushButton.clicked.connect(new_word_write)


# creating the main function that will ensure the removal of unnecessary pairs from the file,
# in which we first create a window for deleting these pairs (imported from the file deletemode.py)
def delete_mode():
    global delete_mode_window
    delete_mode_window = QtWidgets.QMainWindow()
    d_mode_ui = Ui_Deletemode()
    d_mode_ui.setupUi(delete_mode_window)
    delete_mode_window.show()

# this function opens a file, clears the field for words,
# retrieves words from the file and writes them to the field (thus updating the field)
    def delete_mode_refresh():
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            d_mode_ui.plainTextEdit.clear()
            for i, line in enumerate(lines):
                data = line.split(' - ')
                word_for_translation = data[0]
                translation = data[1]
                i += 1
                formatted_line = f"{i}. {word_for_translation} - {translation}\n"
                d_mode_ui.plainTextEdit.appendPlainText(formatted_line)

# this function is intended to get a value from the spinbox widget and update the field with the words
    def get_spinbox_value():
        value = d_mode_ui.spinBox.value()
        delete_row(value-1)
        delete_mode_refresh()

# this function takes the line number (it is defined in the previous function)
# and uses this number to search for a line in the file and delete it
    def delete_row(row_number):
        with open('words.txt', 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            file.seek(0)
            for i, line in enumerate(lines):
                if i != row_number:
                    file.write(line)
            file.truncate()

# automatic initial update of the field
# and connection of the button to the get_spinbox_value function (value + field update)
    delete_mode_refresh()
    d_mode_ui.pushButton.clicked.connect(get_spinbox_value)


# connecting the Delete mode button on the main window with the function of launching this mode
ui.pushButton_2.clicked.connect(delete_mode)


# the functions of interaction with the word deletion mode are over,
# now we will work in a similar way with the word learning mode
# the study function opens a word study window and creates a list and a dictionary
# that will be needed to work with the weighting algorithm
def study():
    global studymode
    studymode = QtWidgets.QMainWindow()
    ui = Ui_studymode()
    ui.setupUi(studymode)
    studymode.show()
    choices = []
    search = {}
    current_word = None

# this function reads pairs from a file, calculates the total weight,
# finds a random number between 0 and the total weight,
# after that the weight of the first number is added to the variable up_to,
# if this number is greater than the random number, the given word will be selected for translation,
# so the greater the weight number, the greater the chance of this number being selected for translation
    def pair_refresh():
        nonlocal current_word
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(' - ')
                word_for_translation = data[0]
                translation = data[1]
                weight = int(data[2].rstrip())
                choices.append((word_for_translation, weight))
                search[word_for_translation] = translation

        total_weight = sum(weight for word, weight in choices)
        r = random.uniform(0, total_weight)
        up_to = 0
        for word, weight in choices:
            if up_to + weight > r:
                current_word = word
                break
            up_to += weight

        ui.label.setText(current_word)
        ui.plainTextEdit.setPlainText('')

# this function is the main and largest one, its tasks are:
# 1) to check whether the word is correctly translated
# 2) to set a new weight for the word
# 3) to set the color of the input field to green/red depending on the correctness of the answer
    def check_translation():
        if current_word is None:
            return

# a word from the field is obtained, cleaned of spaces and hyphens
        get_text = ui.plainTextEdit.toPlainText().rstrip()

# then the condition is checked, if the received word corresponds to the word in the file,
# the weight decreases, the field is painted green and vice versa,
# if it does not match, then it is red, the weight increases
        if get_text == search[current_word]:
            for i, (word, weight) in enumerate(choices):
                if word == current_word:
                    if weight > 1:
                        choices[i] = (word, weight - 1)
                        break
            with open('words.txt', 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    data = line.split(' - ')
                    word_for_translation = data[0]
                    translation = data[1]
                    weight = str(next(weight for word, weight in choices if word == word_for_translation))
                    file.write(f"{word_for_translation} - {translation} - {weight}\n")
                file.truncate()

            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(QtCore.Qt.GlobalColor.green))
            ui.plainTextEdit.setPalette(palette)
            QTimer.singleShot(1500, lambda: ui.plainTextEdit.setPalette(QtGui.QPalette()))
        else:
            for i, (word, weight) in enumerate(choices):
                if word == current_word:
                    if weight < 5:
                        choices[i] = (word, weight + 1)
                        break
            with open('words.txt', 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    data = line.split(' - ')
                    word_for_translation = data[0]
                    translation = data[1]
                    weight = str(next(weight for word, weight in choices if word == word_for_translation))
                    file.write(f"{word_for_translation} - {translation} - {weight}\n")
                file.truncate()

            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(QtCore.Qt.GlobalColor.red))
            ui.plainTextEdit.setPalette(palette)
            QTimer.singleShot(1500, lambda: ui.plainTextEdit.setPalette(QtGui.QPalette()))

# we connect buttons with functions
    ui.pushButton.clicked.connect(pair_refresh)
    ui.pushButton_2.clicked.connect(check_translation)
    pair_refresh()


# connect the third button with the study function, perform the main cycle of event processing,
# and close the program after its completion
ui.pushButton_3.clicked.connect(study)
sys.exit(app.exec())

