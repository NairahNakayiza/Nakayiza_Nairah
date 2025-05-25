while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division is:", result)
        break  # Exit loop if successful
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
