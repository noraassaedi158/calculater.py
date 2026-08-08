# PySide6 Calculator

## My first ever mini project (heheheheh)!

A calculator application built with Python and PySide6.

My project started as a basic terminal calculator and later I redesigned it as a graphical desktop application. The goal was to practice GUI development, event handling, and connecting user interactions with program logic.

I found the GUI development easier because I had previous experience with JavaFX from my Advanced Programming course and my background with Java helped me grasp Python quickly.

AI was used as a learning and debugging tool. It helped explain Python syntax, discuss programming logic, and troubleshoot issues. **All code was implemented by me, and I understand and can explain every part of the project.**

## ✨ Features I added:
* Addition, subtraction, multiplication, and division
* Decimal number support
* Graphical user interface built with PySide6
* Button-based input (maybe keyboard in the future?)
* Expression parsing and evaluation
* Correct order of operations using BIDMAS
* Parentheses and nested expressions
* Implicit multiplication around parentheses
* Unary positive and negative numbers
* Expression validation
* Expression normalization
* Division-by-zero handling
* Random encouraging messages loaded from a JSON file (hehe)
* Clear button with randomized messages
* Live date and time display
* Custom GUI styling using Qt Style Sheets (QSS)
  
## 🧠 Calculator Engine
The calculator does not use Python's `eval()` to evaluate expressions.
Instead, expressions go through several stages:

1. **Conversion** — converts valid numeric values from strings into floats.
2. **Validation** — checks whether the expression follows the calculator's rules.
3. **Normalization** — handles unary `+` and `-` signs and converts them into signed numbers.
4. **BIDMAS evaluation** — evaluates multiplication and division before addition and subtraction.
5. **Parentheses** — bracketed expressions are evaluated separately, including nested parentheses.

This was one of the main learning parts of the project, as I gradually developed the calculator's own expression-processing logic, it was difficult but I learnt alot.

## 📸 Calculator GUI

<img width="378" height="412" alt="Screenshot 2026-07-24 160135" src="https://github.com/user-attachments/assets/2a202552-e917-46a1-ba29-13671d28d5de" />


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
* Implementing BIDMAS/order of operations
* Working with stacks for parentheses
* Handling nested expressions
* Separating different stages of expression processing
* Using Python lambdas
* Working with JSON files
* Debugging and testing edge cases
* Thinking about validation and parser design

## 💻 Running the Project
Install PySide6:
```bash
pip install PySide6
```

Then run the application:
```bash
python main.py
```

# 📋 Updates
## Version 1.1

* Created a console-based calculator
* Supported basic arithmetic operations between two numbers

## Version 1.2

* Added a graphical user interface (GUI) using PySide6
* Replaced the console interface with a desktop GUI

## Version 1.3

* Added a live date and time display
* Clock updates in real time while the application is running

## Version 1.4

* Added support for evaluating expressions with multiple operations
* Improved division-by-zero error handling

## Version 1.5

* Added support for evaluating expressions using the correct order of operations (BIDMAS)

## Version 1.6

* Redesigned the user interface using Qt Style Sheets (QSS)
* Added a custom color palette, fonts, rounded buttons, and improved visual consistency

## Version 1.7

* Added decimal number support
* Added bracket buttons
* Added the "Press Me!" button to generate random encouraging messages

## Version 1.8

* Implemented bracket evaluation
* Added support for nested expressions
* Added a stack-based system to detect matching parentheses
* Added validation for expressions inside parentheses
* Added implicit multiplication around parentheses

## Version 1.9

* Added a dedicated conversion stage for processing numeric values
* Added expression validation
* Added expression normalization
* Added support for unary positive and negative numbers
* Improved handling of operator combinations
* Improved the overall expression-processing pipeline
* Strengthened the calculator's handling of invalid expressions
fore applying the remaining operations.

## Version 2 (Soon)

* Refactor the code using OOP and the MVC architecture
* Rename and reorganize functions and variables for clearer structure
* Add a dark mode



  
