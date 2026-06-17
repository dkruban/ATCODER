def check_lucky_number():
    # Read the car number input from the user
    car_no = input("Enter the car no:")
    
    # Check if the string consists of exactly 4 digits
    if len(car_no) != 4 or not car_no.isdigit():
        print(f"{car_no} is not a valid car number")
        return
        
    # Safeguard against the "0000" edge case as problem notes "positive numbers"
    if int(car_no) <= 0:
        print(f"{car_no} is not a valid car number")
        return

    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in car_no)

    # Check if the sum is divisible by 3, 5, or 7
    if digit_sum % 3 == 0 or digit_sum % 5 == 0 or digit_sum % 7 == 0:
        print("Lucky Number")
    else:
        print("Sorry its not my lucky number")

# Run the function
if __name__ == "__main__":
    check_lucky_number()
