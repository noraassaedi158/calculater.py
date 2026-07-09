import signal
import sys
import json
import random
import datetime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PySide6.QtCore import QTimer
with open("qoutes.json", 'r') as file:
    q = json.load(file)
def en():
 return random.choice(q["encourage"])

my_app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Calculator")
screen= QLineEdit()
screen.setPlaceholderText(en())
screen.setReadOnly(True)
def calc_num(n):
    screen.setText(screen.text()+ n)
def wipe():
    screen.setText(screen.setPlaceholderText((en())))
def sp():
    values = screen.text().split()
    numbers=[int(n) for n in values if n.isnumeric()==True]
    operators=[o for o in values if o.isnumeric()!=True]
    if len(numbers) == 0 :
        print("error, love")
    val = numbers[0]
    for oper in range(0, len(operators)):
        if operators[oper] == "-":
            val=val-numbers[oper + 1]
        if operators[oper] == "+":
            val = val + numbers[oper + 1]
        if operators[oper] == "X":
            val = val * numbers[oper + 1]
        if operators[oper] == "÷":
             if numbers[oper + 1] == 0:
                val="Error: cannot divide by 0"
             else:
                 val = val / numbers[oper + 1]
    screen.clear()
    screen.setText(str(val))
cleared=QPushButton("Clear")
cleared.clicked.connect(wipe)
date= QLabel("Date: " + datetime.datetime.now().strftime("%A %d %B %Y"))
time=QLabel()
def time_rn():
     time.setText("Time: " + datetime.datetime.now().strftime("%I:%M %p"))
clock=QTimer()
clock.setInterval(1000)
clock.timeout.connect(time_rn)
clock.start()
one=QPushButton(" 1 ")
one.clicked.connect(lambda: calc_num("1") )
two=QPushButton(" 2 ")
two.clicked.connect(lambda: calc_num("2") )
three= QPushButton(" 3 ")
three.clicked.connect(lambda: calc_num("3") )
four =QPushButton(" 4 ")
four.clicked.connect(lambda: calc_num("4") )
five =QPushButton(" 5 ")
five.clicked.connect(lambda: calc_num("5") )
six=QPushButton(" 6 ")
six.clicked.connect(lambda: calc_num("6") )
seven=QPushButton(" 7 ")
seven.clicked.connect(lambda: calc_num("7") )
eight =QPushButton(" 8 ")
eight.clicked.connect(lambda: calc_num("8") )
nine=QPushButton(" 9 ")
nine.clicked.connect(lambda: calc_num("9") )
zero =QPushButton(" 0 ")
zero.clicked.connect(lambda: calc_num("0") )
addition_button = QPushButton(" + ")
addition_button.clicked.connect(lambda: calc_num(" + ") )
subtraction_button = QPushButton(" - ")
subtraction_button.clicked.connect(lambda: calc_num(" - ") )
multi_button = QPushButton(" x ")
multi_button.clicked.connect(lambda: calc_num(" X ") )
divi_button = QPushButton(" ÷ ")
divi_button.clicked.connect(lambda: calc_num(" ÷ ") )
equals = QPushButton(" = ")
equals.clicked.connect(sp)
title= QLabel("This is my first personal mini project! ")
whole_layout = QVBoxLayout()
whole_layout.addWidget(title)
whole_layout.addWidget(date)
whole_layout.addWidget(time)
whole_layout.addWidget(screen)
whole_layout.addWidget(cleared)
buttons_layout= QGridLayout()
buttons_layout.addWidget(one, 0,0)
buttons_layout.addWidget(two, 0, 1)
buttons_layout.addWidget(three, 0, 2)
buttons_layout.addWidget(four, 1, 0)
buttons_layout.addWidget(five, 1, 1)
buttons_layout.addWidget(six, 1, 2)
buttons_layout.addWidget(seven, 2, 0)
buttons_layout.addWidget(eight, 2, 1)
buttons_layout.addWidget(nine, 2, 2)
buttons_layout.addWidget(zero,3, 0)
buttons_layout.addWidget(addition_button, 3, 1)
buttons_layout.addWidget(subtraction_button, 3, 2)
buttons_layout.addWidget(multi_button, 4,0)
buttons_layout.addWidget(equals ,4, 1)
buttons_layout.addWidget(divi_button, 4, 2)
whole_layout.addLayout(buttons_layout)
window.setLayout(whole_layout)
window.resize(200, 300)
window.show()

my_app.exec()

        
