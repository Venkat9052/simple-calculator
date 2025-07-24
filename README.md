# simple-calculator
# 🧮 Simple Command-Line Calculator with History (Python)

This is a simple command-line **calculator** program written in Python that allows users to perform basic arithmetic operations and **keeps a history** of calculations in a text file. Users can view or clear the history, and perform operations using a simple 3-character format (e.g., `3+5`).

---

## 🔧 Features

- Supports **basic operations**: `+`, `-`, `*`, `/`, `%`
- Maintains a **history of all calculations**
- Allows users to:
  - View history (`history`)
  - Clear history (`clear`)
  - Exit the program (`exit`)
- Stores history in a file: `calculator_history.txt`
- Handles division by zero and invalid operators

---

## 📦 File Structure

## ▶️ How to Run

1. Make sure Python (version 3+) is installed on your system.
2. Save the code in a file, e.g., `calculator.py`.
3. Open your terminal or command prompt.
4. Run the program:
   ```bash
   python calculator.py

## example of code run
Enter calculation (eg. 2+3) or COMMAND (history,clear,exit): 2+5
Result: 7

Enter calculation (eg. 2+3) or COMMAND (history,clear,exit): 8/0
Error: Division by Zero is not allowed.

Enter calculation (eg. 2+3) or COMMAND (history,clear,exit): history
2+5 = 7

Enter calculation (eg. 2+3) or COMMAND (history,clear,exit): clear
History cleared.

Enter calculation (eg. 2+3) or COMMAND (history,clear,exit): exit
Exiting the calculator.
Thank you for using calculator.

