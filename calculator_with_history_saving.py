HISTORY = "calculator_history.txt" 


def show_history():
    data = open(HISTORY,"r")
    lines = data.readlines()
    if (len(lines) == 0):
        print("No history available.")
    else:
        for line in reversed(lines):
            print(line.strip())
    
    data.close()


def clear_history():
    with open(HISTORY, "w") as file:
        file.write("")  # Clear the file by writing an empty string
    print("History cleared.")

def save_to_history(expression, result):
    with open(HISTORY, "a") as data:
        data.write(f"{expression} = {result}\n")


def calculate(user_input):
    user_input = user_input.strip()
    num1 = float(user_input[0])
    op = user_input[1]
    num2= float(user_input[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error:Division by Zero is not allowed .")
            return
        result = num1 / num2
    elif op == "%":
        result = num1 % num2
    else:
        print("Invalid operator. Please use one of +, -, *, /, % . ")
        return

    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")
    save_to_history(user_input, result)
        

    
def main():
    print("---------------SIMPLE CALCULATOR--------------------\n")
    while True:
        user_input = input("Enter calculation (eg. 2+3) or COMMAND (history,clear,exit): ").strip()

        if user_input.lower() == "exit":
            print("Exiting the calculator.")
            print("Thank you for using calculator")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            if len(user_input) != 3 :
                print("Invalid input format. please use the format: number operator number (e.g., 2+3).")

            calculate(user_input)


main()
