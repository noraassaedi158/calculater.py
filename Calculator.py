import signal
import sys
import json
import random
import datetime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PySide6.QtCore import QTimer, Qt

with open("qoutes.json", 'r') as file:
    q = json.load(file)

def en():
 return random.choice(q["encourage"])

my_app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Calculator")
screen= QLineEdit()
screen.setFixedHeight(30)
screen.setPlaceholderText(en())
screen.setReadOnly(True)

def calc_num(n):
    screen.setText(screen.text()+ n)
def wipe():
    screen.clear()
def press():
    screen.clear()
    screen.setPlaceholderText((en()))
def sp():
    values = screen.text().split()
    br_finder=[]
    #this is for validating the brackets
    for m in  range(0, len(values)):
            if values[m] == "(":
                br_finder.append(m)
            elif values[m] == ")":
                if len(br_finder) == 0:
                    screen.clear()
                    screen.setPlaceholderText((en()))
                    return
                else:
                    br_finder.pop()
    if len(br_finder) > 0:
        screen.clear()
        screen.setPlaceholderText((en()))
        return
    #and here is where it is solved 
    for m in range(0, len(values)):
        for m in range(0, len(values)):
            if values[m] == "(":
                br_finder.append(m)
            elif values[m] == ")":
                br = br_finder.pop()
                values_br = values[br + 1: m]
                answer=conversion(values_br)
                #replace even the brackets
                values[br: m+1]=answer
                break
    for m in range (0, len(values)):
        answer=conversion(values)

    answer=bidmas(answer)
    screen.clear()
    screen.setText(str(answer[0]))

def conversion(values):
        for m in range(0, len(values)):
            try:
                values[m] = float(values[m])
            except:
                pass
        return values
#def validation():

def bidmas(values):
    while len(values) != 1:
        for m in range(0, len(values)):
            if values[m] == 'x':
                print(type(values[m - 1]))
                v = [float(values[m - 1]) * values[m + 1]]
                values[m - 1:m + 2] = v
                break

            elif values[m] == '÷':
                if values[m + 1] == 0:
                    screen.clear()
                    screen.setPlaceholderText((en()))
                    return
                else:
                    v = [values[m - 1] / values[m + 1]]
                    values[m - 1:m + 2] = v
                    break

        for m in range(0, len(values)):
            if values[m] == '+':
                v = [values[m - 1] + values[m + 1]]
                values[m - 1:m + 2] = v
                break

            elif values[m] == '-':
                v = [values[m - 1] - values[m + 1]]
                values[m - 1:m + 2] = v
                break

    return values

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
multi_button.clicked.connect(lambda: calc_num(" x ") )
divi_button = QPushButton(" ÷ ")
divi_button.clicked.connect(lambda: calc_num(" ÷ ") )
dot = QPushButton(".")
dot.clicked.connect(lambda: calc_num(".") )
left_br = QPushButton("(")
left_br.clicked.connect(lambda: calc_num(" ( ") )
right_br = QPushButton(")")
right_br.clicked.connect(lambda: calc_num(" ) ") )
equals = QPushButton(" = ")
equals.clicked.connect(sp)
press_me=QPushButton("Press me!")
press_me.clicked.connect(press)
title= QLabel("This is my first personal mini project! ")
title.setObjectName("title")
whole_layout = QVBoxLayout()
whole_layout.addWidget(title)
whole_layout.addWidget(date)
whole_layout.addWidget(time)
title.setAlignment(Qt.AlignmentFlag.AlignCenter)

whole_layout.addWidget(screen)
whole_layout.addWidget(cleared)
buttons_layout= QGridLayout()
buttons_layout.addWidget(seven, 0,0)
buttons_layout.addWidget(eight, 0, 1)
buttons_layout.addWidget(nine, 0, 2)
buttons_layout.addWidget(divi_button, 0, 3)
buttons_layout.addWidget(four, 1, 0)
buttons_layout.addWidget(five, 1, 1)
buttons_layout.addWidget(six, 1, 2)
buttons_layout.addWidget(multi_button, 1, 3)
buttons_layout.addWidget(one, 2, 0)
buttons_layout.addWidget(two,2, 1)
buttons_layout.addWidget(three, 2, 2)
buttons_layout.addWidget(subtraction_button, 2, 3)
buttons_layout.addWidget(zero, 3,1)
buttons_layout.addWidget(dot ,3, 2)
buttons_layout.addWidget(addition_button,3, 3)

buttons_layout.addWidget(press_me, 3, 0)
buttons_layout.addWidget(left_br, 4, 0)
buttons_layout.addWidget(right_br, 4, 1)
buttons_layout.addWidget(equals, 4, 2, 1,2)

whole_layout.addLayout(buttons_layout)
window.setLayout(whole_layout)

window.setStyleSheet(""" QWidget {background-color: #A6425B;
                                  color: black } 
                      QPushButton { background-color: pink;
                                    color: #A6425B ;
                                    font-weight: bold;
                                    border: 1.5px solid #BD6073; 
                                    border-radius: 8px;
                                    } 
                       QPushButton:pressed { background-color: #FAEDED} 
                       QPushButton:hover { background-color: #FAEDED}             
                       QLabel { color : white ;
                                font-weight: bold ; 
                                font-family: Lucida Console }
                       QLabel#title{color : black ;
                                font-size: 13px;
                                 font-family : Lucida Calligraphy}
                       QLineEdit{
                                color : white ;
                                font-weight: bold;
                                border:  0.5px solid #BD6073;
                                border-radius: 8px;
                                font-family: Lucida Console} 
                       QLineEdit::placeholder { color: white;
                                               font-weight: bold} """ )
window.setFixedSize(300, 300)
window.show()

my_app.exec()


