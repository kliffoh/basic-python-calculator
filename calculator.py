def calculate(num1, num2, operation):
    """Performs the requested mathematical operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero inside the calculation function
        if num2 == 0:
            return "🚫 Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "❌ Invalid operation."

def advanced_calculator():
    """
    An advanced, looping calculator with a personalized greeting.
    """
    # 1. Personalized Greeting
    user_name = input("What is your name? ")
    print(f"\nHello **{user_name.title()}**! clive otieno is here for your calculation assistance. 🤖")
    print("Type 'quit' or 'exit' at any time to stop the calculator.")

    # Main Calculation Loop
    while True:
        print("\n-------------------------------------------")

        # 2. Collect and Validate First Number
        first_input = input("Enter the first number (or 'quit'): ").lower()
        if first_input in ['quit', 'exit']:
            break
        
        try:
            num1 = float(first_input)
        except ValueError:
            print("🛑 Invalid input. Please enter a valid number.")
            continue # Restart the loop for valid input

        # 3. Collect and Validate Operation
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ['quit', 'exit']:
            break
        
        # 4. Collect and Validate Second Number
        second_input = input("Enter the second number (or 'quit'): ").lower()
        if second_input in ['quit', 'exit']:
            break
            
        try:
            num2 = float(second_input)
        except ValueError:
            print("🛑 Invalid input. Please enter a valid number.")
            continue # Restart the loop

        # 5. Perform Calculation and Display Result
        result = calculate(num1, num2, operation)

        # Check if the result is an error message (string) or a number
        if isinstance(result, str):
            print(result) # Print the error message
        else:
            # Print the successful equation and result
            print(f"\nCalculation: {num1} {operation} {num2} = **{result}**")

    print("\nThank you for using the calculator! Goodbye. 👋")

# Run the advanced function
advanced_calculator()