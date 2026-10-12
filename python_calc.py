def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def check_even_odd(num):
    # Checking using integer conversion just in case a float is passed
    n = int(num)
    if n % 2 == 0:
        return f"{n} is Even."
    else:
        return f"{n} is Odd."

def calculate_percentage(part, total):
    if total == 0:
        return "Error: Total cannot be zero."
    return (part / total) * 100

def display_menu():
    print("\n--- Python Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Check Even or Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

def main():
    while True: # Loop to allow multiple calculations
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice in ('1', '2', '3', '4', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
                
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} ÷ {num2} = {result}")
            elif choice == '6':
                result = calculate_percentage(num1, num2)
                print(f"Result: {num1} is {result}% of {num2}")
                
        elif choice == '5':
            try:
                num = float(input("Enter a number to check even/odd: "))
                print(f"Result: {check_even_odd(num)}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid choice! Please select a valid option from 1 to 7.")

if __name__ == "__main__":
    main()
