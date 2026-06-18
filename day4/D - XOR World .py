def main():
    print("=== Welcome to the XOR World ===")
    
    try:
        num1 = int(input("Enter first integer (A): "))
        num2 = int(input("Enter second integer (B): "))
    except ValueError:
        print("Invalid input! Please enter whole numbers (integers) only.")
        return

    xor_result = num1 ^ num2
    print("\n--- XOR World Results ---")
    print(f"Decimal Result: {num1} ^ {num2} = {xor_result}")
    print(f"Binary A:       {bin(num1)[2:]:>10} (Decimal {num1})")
    print(f"Binary B:       {bin(num2)[2:]:>10} (Decimal {num2})")
    print("-" * 35)
    print(f"Binary XOR:     {bin(xor_result)[2:]:>10} (Decimal {xor_result})")
    
    print("\n--- The XOR Magic Property (A ^ B ^ B = A) ---")
    restored_num = xor_result ^ num2
    print(f"Decrypting:     {xor_result} ^ {num2} = {restored_num} (Back to A!)")


if __name__ == "__main__":
    main()
