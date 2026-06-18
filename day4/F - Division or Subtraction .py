def show_subtraction(num1, num2):
    """Performs and explains subtraction operations."""
    print("\n--- Subtraction Results ---")
    print(f"Standard Subtraction ({num1} - {num2}) = {num1 - num2}")
    print(f"Reversed Subtraction ({num2} - {num1}) = {num2 - num1}")


def show_division(num1, num2):
    """Performs and explains all types of division operations."""
    print("\n--- Division Results ---")
    
    # Check for division by zero error before proceeding
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        return

    print(f"Standard Division ({num1} / {num2}) = {num1 / num2}")
    print(f"Floor Division    ({num1} // {num2}) = {num1 // num2} (Whole number)")
    print(f"Modulo/Remainder  ({num1} % {num2}) = {num1 % num2} (Leftover)")


def main():
    print("=== Division or Subtraction Demo ===")
    
    # 1. Get user input for numbers
    try:
        a = float(input("Enter first number (A): "))
        b = float(input("Enter second number (B): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # 2. Get user input for the chosen operation
    print("\nChoose an operation:")
    print("S - Subtraction")
    print("D - Division")
    choice = input("Your choice (S/D): ").strip().upper()

    # 3. Route to the correct function based on choice
    if choice == 'S':
        show_subtraction(a, b)
    elif choice == 'D':
        show_division(a, b)
    else:
        print("Invalid choice! Please select 'S' or 'D'.")


if __name__ == "__main__":
    main()
