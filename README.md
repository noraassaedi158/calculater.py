## PySide6 Calculator
# My first ever mini project!
its a simple calculator application built with Python and PySide6.
My project started of as a basic terminal calculator and I later redesigned it as graphical desktop application.
The goal was to practice GUI development, event handling, and connecting user interactions with program logic.
I found this easy as I had practice with JavaFX this year in my advanced programming course
I used minimal AI, this is purely my work-I only used AI for debugging, searching syntax structure of python since I mainly use Java and AI helping me write my ReadMe (keyword-helping, I revised and edited )
## ✨ Features
* Addition, subtraction, multiplication, and division
* Graphical user interface built with PySide6
* Button-based input
* Expression parsing using a simple `number operator number` format
* Handles division by zero
* Displays random encouraging messages from a JSON file (hehe)
* Clear button to reset the calculator (that also displays a random message when clicked
* Displays the current date and time, and the time on my calculator updates with the current time
## Calculator GUI

  <img width="372" height="412" alt="Screenshot 2026-07-11 182446" src="https://github.com/user-attachments/assets/3e4bbf17-859d-4531-8243-d256ffb966a0" />
  
## 🛠️ Technologies Used
* Python
* PySide6 (Qt for Python)
* JSON
## 📚 What I Learned
While building this project, I practiced:
* Creating desktop GUIs with PySide6
* Working with Qt signals and slots
* Connecting buttons to functions
* Managing user input from GUI components
* Converting between strings and numbers
* Parsing mathematical expressions
* Separating user interface logic from calculation logic
* using python lambdas (I was so happy to discover they are similiar to Java's)
## 🚀 Future Improvements
Possible improvements I would like to add:
* Support for longer expressions (example: `5 + 3 + 2`)
* Keyboard input support
* Better error handling for invalid expressions
* A more advanced calculator engine
* Improved UI styling (I'd love to make light/dark mode)
* maybe I'd add more operations like sin, cos..etc
## 💻 Running the Project

 Install PySide6:

```bash on your cmd
pip install PySide6
```
then,
Run the application:
```bash
python main.py
```
## updates:
### Version 1.1:
- console based calculator
- Supports basic arithmetic operations between two numbers.

### Version 1.2
- Added a graphical user interface (GUI) using PySide6
- Replaced the console interface with a more user-friendly design

### Version 1.3
- Added a live date and time display
- Clock updates in real time while the application is running

### Version 1.4
- Calculator can now evaluate expressions with multiple operations.
- Improved division-by-zero error handling.

## Version 1.5
- Added support for evaluating expressions using the correct order of operations (BIDMAS).

## Version 1.6
- Redesigned the user interface using Qt Style Sheets (QSS).
- Added a custom color palette, fonts, rounded buttons, and improved overall visual consistency.
